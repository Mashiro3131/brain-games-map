# This will be the account page for the user that is logged in. if he's not logged in, he will show the login page.

import os
from database import Database
from login import Login
import customtkinter
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkFont, CTkButton, CTkImage

class Account(CTkFrame):
    
    def setup_window(self):
        pass