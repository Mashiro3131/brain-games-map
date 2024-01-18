import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkFont, CTkButton, CTkImage, CTkOptionMenu
from PIL import Image, ImageTk
import os
from database import Database
import colorama
from colorama import Fore
colorama.init(autoreset=True)



class Session:
    def __init__(self):
        self.username = None
        self.is_authenticated = False

    def login(self, username):
        self.username = username
        self.is_authenticated = True

    def logout(self):
        self.username = None
        self.is_authenticated = False

    def is_logged_in(self):
        return self.is_authenticated
    
    def get_username(self):
        return self.username


class Login(CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.session = Session
        self.parent = parent
        self.parent.theme = "dark"
        self.setup_window()
        self.setup_assets()
        self.create_left_side_frame()
        self.create_login_frame()
        
        self.db = Database(host='127.0.0.1', port='3306', user='root', password='root', database='brain_games_db')


    def setup_window(self):
        self.parent.title("LogIn")
        self.parent.geometry("856x645")
        self.parent.resizable(False, False)


    def setup_assets(self):
        assets_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "login")
        self.braingames_logo_data = Image.open(os.path.join(assets_folder, "BrainGames-logo.png"))
        self.account_icon_data = Image.open(os.path.join(assets_folder, "account-icon.png"))
        self.password_icon_data = Image.open(os.path.join(assets_folder, "password-icon.png"))
        self.eye_open_img = ImageTk.PhotoImage(Image.open(os.path.join(assets_folder, "eye-show-icon.png")))
        self.eye_closed_img = ImageTk.PhotoImage(Image.open(os.path.join(assets_folder, "eye-hide-icon.png")))

    def create_left_side_frame(self):
        self.left_side_frame = CTkFrame(self, width=428, height=645, fg_color="#00002E")
        self.left_side_frame.pack_propagate(0)
        self.left_side_frame.pack(expand=True, side="left")

        brain_games_logo = CTkImage(dark_image=self.braingames_logo_data, light_image=self.braingames_logo_data, size=(200, 200))
        CTkLabel(self.left_side_frame, text="", image=brain_games_logo).pack(expand=True, side="top")



    def create_login_frame(self):
        self.login_frame = CTkFrame(self, width=428, height=645, fg_color="#000")
        self.login_frame.pack_propagate(0)
        self.login_frame.pack(expand=True, side="right")

        # Login title
        login_title_label = CTkLabel(self.login_frame, text="Welcome back !", text_color="#d292ff", 
                                     anchor="w", justify="left", font=CTkFont(family="Test Söhne Kräftig", size=41, weight="bold"))
        login_title_label.pack(anchor="w", pady=(75, 55), padx=(55, 0))

        self.create_login_username_entry()
        self.create_login_password_entry()
        self.setup_login_button_frame()



    def create_login_username_entry(self):
        account_icon = CTkImage(dark_image=self.account_icon_data, light_image=self.account_icon_data, size=(25,25))
        self.username_label = CTkLabel(self.login_frame, text="  Username:", text_color="#FFF", anchor="w", justify="left", 
                                       font=CTkFont(family="Test Söhne", size=14), image=account_icon, compound="left")
        self.username_label.pack(anchor="w", pady=(38, 0), padx=(55, 0))
        
        self.username_entry = CTkEntry(self.login_frame, width=300, height=35, fg_color="#EEEEEE", border_color="#d292ff", 
                                       border_width=1, text_color="#000000", font=CTkFont(family="Test Söhne", size=14))
        self.username_entry.pack(anchor="w", padx=(55, 0))



    def create_login_password_entry(self):
        password_icon = CTkImage(dark_image=self.password_icon_data, light_image=self.password_icon_data, size=(22,22))
        self.password_label = CTkLabel(self.login_frame, text="  Password:", text_color="#FFF", anchor="w", justify="left", 
                                       font=CTkFont(family="Test Söhne", size=14), image=password_icon, compound="left")
        self.password_label.pack(anchor="w", pady=(21, 0), padx=(55, 0))
        
        password_entry_frame = CTkFrame(self.login_frame, fg_color="transparent")
        password_entry_frame.pack(anchor="w", padx=(55, 0))

        self.password_entry = CTkEntry(password_entry_frame, width=300, height=35, fg_color="#EEEEEE", border_color="#d292ff", 
                                       border_width=1, text_color="#000000", show="*", font=CTkFont(family="Test Söhne", size=14))
        self.password_entry.pack(side="left")

        self.toggle_password_button = CTkButton(password_entry_frame, image=self.eye_closed_img, 
                                                command=self.toggle_password, fg_color="transparent", text="", hover_color="#1A1A1A", border_width=0, border_spacing=0)
        self.toggle_password_button.pack(side="left")
        self.toggle_password_button.configure(width=15, height=15)

        self.password_showing = False



    def toggle_password(self):
        if self.password_showing:
            self.password_entry.configure(show="*")
            self.toggle_password_button.configure(image=self.eye_closed_img, width=15, height=15)
            self.password_showing = False
        else:
            self.password_entry.configure(show="")
            self.toggle_password_button.configure(image=self.eye_open_img, width=15, height=15)
            self.password_showing = True



    def setup_login_button_frame(self):
        self.button_frame = CTkFrame(self.login_frame, fg_color="transparent")
        self.button_frame.pack(anchor="w", pady=(20, 0), padx=(55, 0))

        # Login button
        self.login_as_user_button = CTkButton(self.button_frame, text="Login", fg_color="#3c46ff", hover_color="#0000ff", 
                                              font=CTkFont(family="Test Söhne", size=14), text_color="#ffffff", width=147, height=35,
                                              command=self.login_as_user)
        self.login_as_user_button.pack(side="left", padx=(0, 5))
        
        # Register button
        self.register_new_user_button = CTkButton(self.button_frame, text="Register", fg_color="#3c46ff", hover_color="#0000ff", 
                                                  font=CTkFont(family="Test Söhne", size=14), text_color="#ffffff", width=147, height=35,
                                                  command=self.create_register_frame)
        self.register_new_user_button.pack(side="right", padx=(0, 5))
        
        # Continue as guest button
        self.guest_login_button = CTkButton(self.login_frame, text="Continue as guest", fg_color="transparent", hover_color="#000000", 
                                            font=CTkFont(family="Test Söhne", size=14), text_color="#d292ff", width=110,
                                            command=self.login_as_guest)
        self.guest_login_button.pack(anchor="w", pady=(7,0), padx=(230, 0))
    
    
    
    """ Login Functions """
        
    def login_as_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.db.login_user(username, password):  # Assuming login_user returns True on successful login
            print(f"User {username} logged in successfully")
            self.session.login(username)
        else:
            print("Login failed. Incorrect username or password.")



    def register_new_user(self):
        # Placeholder for the registration logic
        # You should collect user information like username, password, and possibly other details
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.db.register_user(username, password, role_id=1):  # role_id=1 for regular users (students)
            print(f"User {username} registered successfully")
            self.session.login(username)
            # Proceed with post-registration actions
        else:
            print("Registration failed")



    def login_as_guest(self):
        username, password = self.db.continue_as_guest()  # Assuming this method returns guest credentials
        if username and password:
            print(f"Logged in as guest: {username}")
            # Proceed with guest login actions
        else:
            print("Failed to continue as guest.")



    """ Registration Functions"""
    def create_register_frame(self):
        self.register_frame = CTkFrame(self.parent, width=856, height=645, fg_color="#000")
        self.register_frame.pack_propagate(0)
        self.register_frame.place(x=0, y=0)  # Overlay the register frame on top of the login frame

        self.login_frame.pack_forget()  # Hide the login frame
        # Register title
        # Add your code to create the register title widget

        print("Displaying registration frame.")

        # Overlay the register frame on top of the login frame
        self.login_frame.place_forget()  # Hide the login frame
        self.register_frame.place(x=0, y=0)  # Show the register frame on top
        self.create_register_main_frame()
        
    
    
    def create_register_main_frame(self):
        self.register_main_frame = CTkFrame(self.register_frame, width=428, height=645, fg_color="#000")
        self.register_main_frame.pack_propagate(0)
        self.register_main_frame.pack(expand=True)
        
        # Register title
        register_title_label = CTkLabel(self.register_main_frame, text="Register", text_color="#d292ff", 
                                        anchor="w", justify="left", font=CTkFont(family="Test Söhne Kräftig", size=41, weight="bold"))
        register_title_label.pack(anchor="w", pady=(85, 55), padx=(55, 0))
        
        self.create_register_username_entry()
        self.create_register_password_entry()
        self.setup_register_button_frame()



    def create_register_username_entry(self):
        account_icon = CTkImage(dark_image=self.account_icon_data, light_image=self.account_icon_data, size=(25,25))
        self.username_label = CTkLabel(self.register_main_frame, text="  Username:", text_color="#FFF", anchor="w", justify="left", 
                                       font=CTkFont(family="Test Söhne", size=14), image=account_icon, compound="left")
        self.username_label.pack(anchor="w", pady=(38, 0), padx=(65, 0))
        
        self.username_entry = CTkEntry(self.register_main_frame, width=300, height=35, fg_color="#EEEEEE", border_color="#d292ff", 
                                       border_width=1, text_color="#000000", font=CTkFont(family="Test Söhne", size=14))
        self.username_entry.pack(anchor="w", padx=(65, 0))
    
    
        
    def create_register_password_entry(self):
        
        password_icon = CTkImage(dark_image=self.password_icon_data, light_image=self.password_icon_data, size=(22,22))
        self.password_label = CTkLabel(self.register_main_frame, text="  Password:", text_color="#FFF", anchor="w", justify="left", 
                                       font=CTkFont(family="Test Söhne", size=14), image=password_icon, compound="left")
        self.password_label.pack(anchor="w", pady=(21, 0), padx=(65, 0))
        
        password_entry_frame = CTkFrame(self.register_main_frame, fg_color="transparent")
        password_entry_frame.pack(anchor="w", padx=(65, 0))

        self.password_entry = CTkEntry(password_entry_frame, width=300, height=35, fg_color="#EEEEEE", border_color="#d292ff", 
                                       border_width=1, text_color="#000000", show="*", font=CTkFont(family="Test Söhne", size=14))
        self.password_entry.pack(side="left")

        self.toggle_password_button = CTkButton(password_entry_frame, image=self.eye_closed_img, 
                                                command=self.toggle_password, fg_color="transparent", text="", hover_color="#1A1A1A", border_width=0, border_spacing=0)
        self.toggle_password_button.pack(side="left")
        self.toggle_password_button.configure(width=15, height=15)

        self.password_showing = False



    def setup_register_button_frame(self):
        self.register_button_frame = CTkFrame(self.register_main_frame, fg_color="transparent")
        self.register_button_frame.pack(anchor="w", pady=(30, 0), padx=(55, 0))
        
        self.register_button = CTkButton(self.register_button_frame, text="Register", fg_color="#3c46ff", hover_color="#0000ff", 
                                         font=CTkFont(family="Test Söhne", size=14), text_color="#ffffff", width=143, height=35,
                                         command=self.register_new_user)
        
        self.register_button.pack(side="left", padx=(10, 5))
        
        self.back_button = CTkButton(self.register_button_frame, text="Back", fg_color="#3c46ff", hover_color="#0000ff",
                                        font=CTkFont(family="Test Söhne", size=14), text_color="#ffffff", width=143, height=35,
                                        command=self.back_to_login)

        self.back_button.pack(side="right", padx=(10, 5))


       
    def back_to_login(self):
        self.register_frame.place_forget()
        self.login_frame.place(x=0, y=0)
        self.login_frame.pack(expand=True, side="right")
        self.register_frame.pack_forget()
        print("Back to login frame.")
        
        
    # if the user is logged in, he will be redirected to the account a
        
        
        


# To run the Login frame standalone for testing
if __name__ == "__main__":
    root = ctk.CTk()
    app = Login(root)
    app.pack()
    root.mainloop()