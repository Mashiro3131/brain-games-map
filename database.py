import mysql.connector
import contextlib
import functools
import bcrypt
import random
import string
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import datetime
import hashlib



class Database:
    def __init__(self, host, port, user, password, database):
        self.config = {
            '127.0.0.1': host,
            '3306': port,
            'root': user,
            'root': password,
            'brain_games_db': database,
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

    def with_connection(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            with self.connect() as cursor:
                return func(self, cursor, *args, **kwargs)
        return wrapper


    """ BRAIN GAMES """





    """ LOGIN"""
    
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
                    # Handle login state here (e.g., creating a session token)
                    # Return user_id or any other required user information
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


    
    def register_user(self, cursor, pseudo, password, role_id):
        try:
            # Check if user already exists (Efficient existence check)
            if self.is_user_exist(cursor, pseudo):
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
            guest_username = f"guest{hashlib.md5(random_str.encode()).hexdigest()[:10]}"

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
            if username.startswith("guest"):
                # Delete guest account
                delete_query = "DELETE FROM users WHERE pseudo = %s"
                cursor.execute(delete_query, (username,))
                print(Fore.GREEN + f"Guest account {username} deleted successfully.")
            else:
                # Handle logout for regular users (e.g., invalidate session token)
                print(Fore.GREEN + f"User {username} logged out successfully.")

            # Additional logout procedures can be added here if necessary
            return True

        except mysql.connector.Error as error:
            print(Fore.RED + f"Error during logout: {error}")
            return False


