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


    """ CRUD for teachers """

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
    def update_result(self, cursor, user_id, result_id, new_duration=None, new_nbtrials=None, new_nbok=None):
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
        
        cursor.execute(update_query, tuple(parameters))
        print(Fore.GREEN + "Result updated successfully.")

    @with_connection
    def delete_result(self, cursor, user_id, result_id):
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
    def is_user_exist(self, cursor, pseudo):
        """Check if a user already exists in the database."""
        check_user_query = "SELECT 1 FROM users WHERE pseudo = %s"
        cursor.execute(check_user_query, (pseudo,))
        return cursor.fetchone() is not None   
    


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
            # Check if user already exists (Efficient existence check)
            if self.is_user_exist(pseudo):
                print(Fore.RED + "Username already taken.")
                return False

            # Hash the password (Secure password handling)
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Insert new user (Database insertion)
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
            # Generate a unique guest username with a hash-like style
            random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            guest_username = f"guest_{hashlib.md5(random_str.encode()).hexdigest()[:10]}"

            # Generate a random password
            guest_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Create guest account with a default guest role (assuming role_id for guest is 3)
            if self.register_user(cursor, guest_username, guest_password, role_id=3):
                print(Fore.GREEN + f"Guest account created. Username: {guest_username}, Password: {guest_password}")
                return guest_username, guest_password
            else:
                print(Fore.RED + "Failed to create guest account.")
                return None, None

        except mysql.connector.Error as error:
            print(Fore.RED + f"Error in guest account creation: {error}")
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