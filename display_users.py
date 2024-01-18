# Do exactly the same as display_statistics.py but instead of displaying the statistics, display all the users with their data (pseudo, role, etc.)

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import CTkTable
from CTkMessagebox import CTkMessagebox
from customtkinter import *
import database
from database import Database
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

class Users(CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setup_window()
        self.setup_assets()
        self.create_left_side_frame()
        self.create_users_frame()

        self.db = Database(host='127.0.0.1', port='3306', user='root', password='root', database='brain_games_db')
        
    def setup_window(self):
        self.parent.title("Display Users")
        self.parent.geometry("856x645")
        self.parent.resizable(False, False)
        
    def setup_assets(self):
        assets_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "users")
        self.braingames_logo_data = Image.open(os.path.join(assets_folder, "BrainGames-logo.png"))
        self.users_icon_data = Image.open(os.path.join(assets_folder, "users-icon.png"))
        self.search_icon_data = Image.open(os.path.join(assets_folder, "search-icon.png"))
        self.add_icon_data = Image.open(os.path.join(assets_folder, "add-icon.png"))
        self.delete_icon_data = Image.open(os.path.join(assets_folder, "delete-icon.png"))
        self.edit_icon_data = Image.open(os.path.join(assets_folder, "edit-icon.png"))
        self.refresh_icon_data = Image.open(os.path.join(assets_folder, "refresh-icon.png"))
        self.export_icon_data = Image.open(os.path.join(assets_folder, "export-icon.png"))
        self.eye_open_img = ImageTk.PhotoImage(Image.open(os.path.join(assets_folder, "eye-show-icon.png")))
        self.eye_closed_img = ImageTk.PhotoImage(Image.open(os.path.join(assets_folder, "eye-hide-icon.png")))
        
    def create_right_side_frame(self):
        self.right_side_frame = CTkFrame(self, width=556, height=645, fg_color="#00002E")
        self.right_side_frame.pack_propagate(0)
        self.right_side_frame.pack(expand=True, side="right")
        
        brain_games_logo = CTkImage(dark_image=self.braingames_logo_data, light_image=self.braingames_logo_data, size=(100, 100))
        CTkLabel(self.right_side_frame, text="", image=brain_games_logo).pack(expand=True, side="top")
        
    def create_left_side_frame(self):
        self.left_side_frame = CTkFrame(self, width=300, height=645, fg_color="#000")
        self.left_side_frame.pack_propagate(0)
        self.left_side_frame.pack(expand=True, side="left")
        
        # Users title
        users_title_label = CTkLabel(self.left_side_frame, text="Users", text_color="#d292ff", 
                                         anchor="w", justify="left", font=CTkFont(family="Test Söhne Kräftig", size=26, weight="bold"))
        users_title_label.pack(anchor="w", pady=(55, 25), padx=(25, 0))
        
        self.create_search_entry()
        self.create_users_frame()
        self.setup_button_frame()
        
    def create_search_entry(self):
        search_icon = CTkImage(dark_image=self.search_icon_data, light_image=self.search_icon_data, size=(20,20))
        self.search_label = CTkLabel(self.left_side_frame, text="  Search:", text_color="#FFF", anchor="w", justify="left", 
                                         font=CTkFont(family="Test Söhne", size=14), image=search_icon, compound="left")
        self.search_label.pack(anchor="w", pady=(38, 0), padx=(25, 0))
        
        self.search_entry = CTkEntry(self.left_side_frame, width=205, fg_color="#EEEEEE", border_color="#d292ff", 
                                         font=CTkFont(family="Test Söhne", size=14))
        self.search_entry.pack(anchor="w", pady=(5, 0), padx=(25, 0))
        
    def create_users_frame(self):
        self.users_frame = CTkFrame(self.left_side_frame, width=250, height=300, fg_color="#00002E")
        self.users_frame.pack_propagate(0)
        self.users_frame.pack(anchor="w", pady=(25, 0), padx=(25, 0))

        # Users title
        users_title_label = CTkLabel(self.users_frame, text="Users", text_color="#d292ff",
                                         anchor="w", justify="left", font=CTkFont(family="Test Söhne Kräftig", size=20, weight="bold"))
        users_title_label.pack(anchor="w", pady=(0, 25), padx=(0, 0))

        # Users table
        self.users_table = CTkTable(self.users_frame, width=250, height=300, fg_color="#00002E")
        self.users_table.pack_propagate(0)
        self.users_table.pack(anchor="w", pady=(0, 0), padx=(0, 0))

        # Users table columns
        self.users_table.add_column("Pseudo", width=100)
        self.users_table.add_column("Role", width=100)

        # Fetch users data from the database
        users_data = self.db.fetch_users_data()  # Assuming fetch_users_data() is a method in the Database class that retrieves the users' data

        # Add users data to the table
        for user in users_data:
            self.users_table.add_row(user)
            
    def setup_button_frame(self):
        self.button_frame = CTkFrame(self.left_side_frame, width=250, height=300, fg_color="#00002E")
        self.button_frame.pack_propagate(0)
        self.button_frame.pack(anchor="w", pady=(25, 0), padx=(25, 0))
        
        # Add button
        add_icon = CTkImage(dark_image=self.add_icon_data, light_image=self.add_icon_data, size=(20,20))
        self.add_button = CTkButton(self.button_frame, text="Add", text_color="#d292ff", bg_color="#00002E", fg_color="#d292ff", 
                                         border_color="#d292ff", font=CTkFont(family="Test Söhne", size=14), image=add_icon, compound="left")
        self.add_button.pack(anchor="w", pady=(0, 10), padx=(0, 0))
        
        # Delete button
        delete_icon = CTkImage(dark_image=self.delete_icon_data, light_image=self.delete_icon_data, size=(20,20))
        self.delete_button = CTkButton(self.button_frame, text="Delete", text_color="#d292ff", bg_color="#00002E", fg_color="#d292ff", 
                                         border_color="#d292ff", font=CTkFont(family="Test Söhne", size=14), image=delete_icon, compound="left")
        self.delete_button.pack(anchor="w", pady=(0, 10), padx=(0, 0))
        
        # Edit button
        edit_icon = CTkImage(dark_image=self.edit_icon_data, light_image=self.edit_icon_data, size=(20,20))
        self.edit_button = CTkButton(self.button_frame, text="Edit", text_color="#d292ff", bg_color="#00002E", fg_color="#d292ff", 
                                         border_color="#d292ff", font=CTkFont(family="Test Söhne", size=14), image=edit_icon, compound="left")
        self.edit_button.pack(anchor="w", pady=(0, 10), padx=(0, 0))
        
        # Refresh button
        refresh_icon = CTkImage(dark_image=self.refresh_icon_data, light_image=self.refresh_icon_data, size=(20,20))
        self.refresh_button = CTkButton(self.button_frame, text="Refresh", text_color="#d292ff", bg_color="#00002E", fg_color="#d292ff", 
                                         border_color="#d292ff", font=CTkFont(family="Test Söhne", size=14), image=refresh_icon, compound="left")
        self.refresh_button.pack(anchor="w", pady=(0, 10), padx=(0, 0))
        
        # Export button
        export_icon = CTkImage(dark_image=self.export_icon_data, light_image=self.export_icon_data, size=(20,20))
        self.export_button = CTkButton(self.button_frame, text="Export", text_color="#d292ff", bg_color="#00002E", fg_color="#d292ff", 
                                         border_color="#d292ff", font=CTkFont(family="Test Söhne", size=14), image=export_icon, compound="left")
        self.export_button.pack(anchor="w", pady=(0, 10), padx=(0, 0))
        
    def setup_events(self):
        pass
    
    def setup_keybindings(self):
        pass
    
    def setup_menu(self):
        pass
    
    def setup_context_menu(self):
        pass
    
    def setup_tooltip(self):
        pass
    
    def setup_statusbar(self):
        pass
    
    
        
        
        
        