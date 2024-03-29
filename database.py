import mysql.connector
import contextlib
import functools
import bcrypt
import random
import string
import colorama
from colorama import Fore
import datetime
import hashlib

colorama.init(autoreset=True)

""" Database structure (mysql)

--
-- Structure of database creatoion and usage `braingames_db`
--

CREATE DATABASE IF NOT EXISTS `braingames_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `braingames_db`;

--
-- Structure of table `results`
--

CREATE TABLE IF NOT EXISTS `results` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `exercise` VARCHAR(50) NOT NULL,
  `date_hour` DATETIME NOT NULL,
  `duration` TIME NOT NULL,
  `nbtrials` INT(11) NOT NULL,
  `nbok` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
);



--
-- Structure of table `roles`
--

CREATE TABLE IF NOT EXISTS `roles` (
  `id` INT(11) PRIMARY KEY NOT NULL,
  `name` VARCHAR(50) NOT NULL
);



--
-- Structure of table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pseudo` VARCHAR(50) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
);



"""



class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.init(*args, **kwargs)
        return cls._instance

    def init(self, host, port, user, password, database):
        self.config = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': database,
            'buffered': True,
            'autocommit': True
        }

    @contextlib.contextmanager
    def connect(self):
        connection = mysql.connector.connect(**self.config)
        cursor = connection.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def with_connection(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            with self.connect() as cursor:
                return func(self, cursor, *args, **kwargs)
        return wrapper

    @with_connection
    def fetch_game_statistics(self, cursor, pseudo=None, exercise=None, start_date=None, end_date=None, page=1, page_size=20):
        try:
            # Building the WHERE clause
            where_clauses = []
            params = []
            if pseudo:
                where_clauses.append("users.pseudo = %s")
                params.append(pseudo)
            if exercise:
                where_clauses.append("results.exercise = %s")
                params.append(exercise)
            if start_date:
                where_clauses.append("results.date_hour >= %s")
                params.append(start_date)
            if end_date:
                where_clauses.append("results.date_hour <= %s")
                params.append(end_date)

            where_statement = " AND ".join(where_clauses) if where_clauses else "1=1"

            # Pagination setup
            offset = (page - 1) * page_size
            limit_statement = "LIMIT %s OFFSET %s"
            params.extend([page_size, offset])

            # Construct and execute the main query
            main_query = f"""
                SELECT users.pseudo, results.exercise, results.date_hour, results.duration, results.nbtrials, results.nbok
                FROM results
                JOIN users ON users.id = results.user_id
                WHERE {where_statement}
                ORDER BY results.date_hour DESC
                {limit_statement}
            """
            cursor.execute(main_query, params)
            results = cursor.fetchall()

            # Construct and execute the count query
            count_query = f"""
                SELECT COUNT(*)
                FROM results
                JOIN users ON users.id = results.user_id
                WHERE {where_statement}
            """
            cursor.execute(count_query, params[:-2])  # Exclude pagination parameters
            total = cursor.fetchone()[0]

            return results, total

        except mysql.connector.Error as error:
            print(Fore.RED + f"Error fetching results: {error}")
            return [], 0
      
    @with_connection
    def get_exercices(self, cursor):
        try:
            query = "SELECT DISTINCT exercise FROM results"
            cursor.execute(query)
            exercises = cursor.fetchall()

            exercise_names = [exercise[0] for exercise in exercises]
            return exercise_names
        except mysql.connector.Error as error:
            print(Fore.RED + f"Error fetching exercises: {error}")
            return []
    
    
      
      
      
      
      
    # This will be used in the home menu page to display the statistics of the user    
    @with_connection 
    def get_statistics_for_user(self, pseudo=None, exercise=None, start_date=None, end_date=None, page=1, page_size=20):
        return self.fetch_game_statistics(pseudo=pseudo, exercise=exercise, start_date=start_date, end_date=end_date, page=page, page_size=page_size)

    """ USERS """

    @with_connection
    def check_user_role(self, cursor, user_id, required_role):
        query = "SELECT role_id FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result and result[0] == required_role


    """ Display Statistics - CRUD for teachers """

    @with_connection
    def create_new_result(self, cursor, user_id, exercise, date_hour, duration, nbtrials, nbok):
        if not self.check_user_role(cursor, user_id, 2):  # Assuming role_id 2 is for teachers
            print(Fore.RED + "Unauthorized: Only teachers can create results.")
            return False

        insert_query = """
            INSERT INTO results (user_id, exercise, date_hour, duration, nbtrials, nbok) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (user_id, exercise, date_hour, duration, nbtrials, nbok))
        print(Fore.GREEN + "New result added successfully.")
    
    @with_connection
    def add_game_result(self, cursor, pseudo, exercise, duration, nbtrials, nb_success):
        # Convert pseudo to user_id
        user_id_query = "SELECT id FROM users WHERE pseudo = %s"
        cursor.execute(user_id_query, (pseudo,))
        user_id_result = cursor.fetchone()
        if user_id_result is None:
            print(Fore.RED + "User not found")
            return False
        user_id = user_id_result[0]

        # Insert data into results table
        insert_query = '''
        INSERT INTO results (user_id, exercise, date_hour, duration, nbok, nbtrials)
        VALUES (%s, %s, NOW(), %s, %s, %s)
        '''
        values = (user_id, exercise, duration, nbtrials, nb_success)
        try:
            cursor.execute(insert_query, values)
            print(Fore.GREEN + "Game result added successfully.")
            return True
        except mysql.connector.Error as error:
            print(Fore.RED + "Error adding game result: ", error)
            return False








    @with_connection
    def update_game_results(self, cursor, user_id, result_id, new_duration=None, new_nbtrials=None, new_nbok=None):
        if not self.check_user_role(cursor, user_id, 2):
            print(Fore.RED + "Unauthorized: Only teachers can update results.")
            return False

        update_query = "UPDATE results SET "
        parameters = []
        if new_duration:
            update_query += "duration = %s, "
            parameters.append(new_duration)
        if new_nbtrials:
            update_query += "nbtrials = %s, "
            parameters.append(new_nbtrials)
        if new_nbok:
            update_query += "nbok = %s, "
            parameters.append(new_nbok)
        
        update_query = update_query.rstrip(', ')
        update_query += " WHERE id = %s"
        parameters.append(result_id)

        try:
            cursor.execute(update_query, tuple(parameters))
            print(Fore.GREEN + "Result updated successfully.")
        except mysql.connector.Error as error:
            print(Fore.RED + "Error updating results: ", error)

    @with_connection
    def delete_game_results(self, cursor, user_id, result_id):
        if not self.check_user_role(cursor, user_id, 2):
            print(Fore.RED + "Unauthorized: Only teachers can delete results.")
            return False

        delete_query = "DELETE FROM results WHERE id = %s"
        cursor.execute(delete_query, (result_id,))
        print(Fore.GREEN + "Result deleted successfully.")

    @with_connection
    def get_results_for_user(self, cursor, user_id):
        query = "SELECT * FROM results WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        return cursor.fetchall()


    
    @with_connection
    def register_user_with_role(self, cursor, pseudo, password, role_id):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        insert_query = """
            INSERT INTO users (pseudo, password, role_id) VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (pseudo, hashed_password, role_id))
        print(Fore.GREEN + f"User {pseudo} registered successfully with role {role_id}.")

    @with_connection
    def assign_role_to_user(self, cursor, user_id, new_role_id):
        update_query = "UPDATE users SET role_id = %s WHERE id = %s"
        cursor.execute(update_query, (new_role_id, user_id))
        print(Fore.GREEN + f"User with ID {user_id} assigned role {new_role_id}.")



    """ LOGIN """
    
    @with_connection
    def is_user_exist(self, pseudo):
        try:
            check_user_query = "SELECT 1 FROM users WHERE pseudo = %s"
            self.cursor.execute(check_user_query, (pseudo,))
            return self.cursor.fetchone() is not None
        except mysql.connector.Error as error:
            print(Fore.RED + f"Error checking user existence: {error}")
        return False
    
    def is_user_exist(self, cursor, username):
        try:
            check_user_query = "SELECT COUNT(*) FROM users WHERE pseudo = %s"
            cursor.execute(check_user_query, (username,))
            result = cursor.fetchone()
            return result[0] > 0
        except mysql.connector.Error as error:
            print(Fore.RED + f"Error checking user existence: {error}")
            return False

    @with_connection
    def login_user(self, cursor, pseudo, password):
        try:
            # Query to find user by pseudo
            user_query = "SELECT id, password FROM users WHERE pseudo = %s"
            cursor.execute(user_query, (pseudo,))
            user = cursor.fetchone()

            # Check if user exists
            if user:
                user_id, hashed_password = user
                # Verify the password
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                    print(Fore.GREEN + "Login successful.")
                    # Return user data
                    return user_id
                else:
                    # Incorrect password
                    print(Fore.RED + "Incorrect password.")
                    return None
            else:
                # User not found
                print(Fore.RED + "User not found.")
                return None

        except mysql.connector.Error as error:
            print(Fore.RED + f"Error during login: {error}")
            return None


    @with_connection
    def register_user(self, cursor, pseudo, password, role_id):
        try:
            # Check if user already exists
            if self.is_user_exist(cursor, pseudo):
                print(Fore.RED + "Username already taken.")
                return False

            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Insert new user into the users table
            insert_user_query = """
                INSERT INTO users (pseudo, password, role_id) VALUES (%s, %s, %s)
            """
            cursor.execute(insert_user_query, (pseudo, hashed_password, role_id))

            print(Fore.GREEN + "User registered successfully.")
            return True

        except mysql.connector.Error as error:
            print(Fore.RED + f"Error registering user: {error}")
            return False
    
    
    

    @with_connection
    def continue_as_guest(self, cursor):
        try:
            while True:
                # Generate a random string and create an MD5 hash from it
                random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                md5_hash = hashlib.md5(random_str.encode('utf-8')).hexdigest()
                guest_username = f"guest_{md5_hash}"

                if not self.is_user_exist(cursor, guest_username):
                    break

            # Generate a random password
            guest_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Hash the password
            hashed_password = bcrypt.hashpw(guest_password.encode('utf-8'), bcrypt.gensalt())

            # Insert new guest into the users table with guest role_id (assuming it's 3)
            insert_guest_query = """
                INSERT INTO users (pseudo, password, role_id) VALUES (%s, %s, 3)
            """
            cursor.execute(insert_guest_query, (guest_username, hashed_password))

            print(Fore.GREEN + f"Guest account created. Username: {guest_username}")
            return guest_username, guest_password

        except mysql.connector.Error as error:
            print(Fore.RED + f"Error in creating guest account: {error}")
            return None, None



    @with_connection
    def logout_user(self, cursor, username):
        try:
            # Check if the user is a guest
            if username.startswith("guest_"):
                # Delete guest account
                delete_query = "DELETE FROM users WHERE pseudo = %s"
                cursor.execute(delete_query, (username,))
                print(Fore.GREEN + f"Guest account {username} deleted successfully.")
            else:
                # Handle logout for regular users (for ex: invalidate session token)
                print(Fore.GREEN + f"User {username} logged out successfully.")

            # Additional logout procedures can be added here if necessary
            return True

        except mysql.connector.Error as error:
            print(Fore.RED + f"Error during logout: {error}")
            return False


if __name__ == "__main__":
    Database(host='127.0.0.1', port='3306', user='root', password='root', database='brain_games_db')