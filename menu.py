# """ Old version of menu.py, kept for reference

# import os
# from customtkinter import *
# import customtkinter as ctk
# from customtkinter import *
# from CTkTable import CTkTable
# from PIL import Image
# from tkinter import font
# import matplotlib.pyplot as plt
# import geo01, info02, info05
# from new_display_results import Statistics

        # # assets_folder_home = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "home")
        # # assets_folder_sidebar_icons = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sidebar")

# assets_folder_sidebar_icons = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
# assets_folder_home = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "home")


# app = CTk()
# app.title("Brain Games")
# app.iconbitmap(os.path.join(assets_folder_sidebar_icons,"braingames_dark_ico.ico"))
# app.geometry("856x645")
# app.resizable(0,0)
# app.configure(fg_color="#00002E")

# braingames_title_font = CTkFont(family="Test Söhne Kräftig", size=40, weight="bold")
# braingames_subtitle_font = CTkFont(family="Test Söhne", size=40)
# braingames_regular_font = CTkFont(family="Test Söhne", size=14)
# braingames_sidebar_button_font = CTkFont(family="Test Söhne ", size=15, weight="bold")
# set_appearance_mode("dark")


# """ --- Fonts --- """
# # Sidebar Font --> Sharp Grotesk Medium 20
# # Title Font --> Söhne Kräftig Bold
# # Regular Text Font --> Söhne  20

# """ --- Colors --- """
# # Purple --> #400241
# # Dull Lime --> #51d743
# # Background Blue --> #00002E
# # Text Light Lavender --> #d292ff
# # Button Color --> #0000ff
# # Button Hover Color --> #3c46ff

# # TODO Créer les images dans adobe illustrator et ajouter les images den light et dark si possible ainsi que le texte en blanc et noir
# # TODO Couleurs : Loulou purple (#400241) for the BG and Dull Lime (#51d743) for text and logos, Gris --> #E5E5E5, Blanc --> #FFFFFF, Noir --> #000000

# """ Images """ # TODO if needed, add the dark mode images if the switch theme is still on the app

# # Main Brain Games Logo in Sidebar
# braingames_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "braingames_logo.png"))
# # braingames_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "braingames_dark.png"))
# braingames_img = CTkImage(dark_image=braingames_img_light_data, light_image=braingames_img_light_data, size=(87.68, 83,78))

# # Home (Menu) Icon in Sidebar
# home_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "home_light.png"))
# home_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "home_light.png")) # home_dark.png
# home_img = CTkImage(dark_image=home_img_dark_data, light_image=home_img_light_data)

# # Geo01 (GeoGame) Icon in Home Frame
# geo01_img_light_data = Image.open(os.path.join(assets_folder_home, "geo01_button.png"))
# geo01_img_dark_data = Image.open(os.path.join(assets_folder_home, "geo01_button.png"))
# geo01_img = CTkImage(dark_image=geo01_img_dark_data, light_image=geo01_img_light_data, size=(236, 283))

# # Info02 (InfoGame) Icon in Home Frame
# info02_img_light_data = Image.open(os.path.join(assets_folder_home, "info02_button.png"))
# info02_img_dark_data = Image.open(os.path.join(assets_folder_home, "info02_button.png"))
# info02_img = CTkImage(dark_image=info02_img_dark_data, light_image=info02_img_light_data, size=(315, 122))

# # Info05 (InfoGame) Icon in Home Frame
# info05_img_light_data = Image.open(os.path.join(assets_folder_home, "info05_button.png"))
# info05_img_dark_data = Image.open(os.path.join(assets_folder_home, "info05_button.png"))
# info05_img = CTkImage(dark_image=info05_img_dark_data, light_image=info05_img_light_data,  size=(315, 122))

# # Statistics (display_results) Icon in Sidebar
# statistics_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "analytics_icon.png"))
# statistics_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "analytics_icon.png")) # TODO Changer l'image
# statistics_img = CTkImage(dark_image=statistics_img_light_data, light_image=statistics_img_light_data)

# # Orders (user_list_icon) Icon in Sidebar (it will only be visible for the admin and the teachers that have a role number "2", from there we can CRUD the users (students)))
# users_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "user_list_icon.png"))
# users_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "user_list_icon.png")) # TODO Changer l'image
# users_img = CTkImage(dark_image=users_img_light_data, light_image=users_img_light_data)

# # Settings Icon in Sidebar (the user can then change his password, his username, his name, his profile picture, etc...)
# settings_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "settings_icon.png"))
# settings_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "settings_icon.png")) # TODO Changer l'image
# settings_img = CTkImage(dark_image=settings_img_light_data, light_image=settings_img_light_data)

# # Account Icon in Sidebar (the user can then visualize his profile, his username, his profile picture, and his average score that he got in the games)
# person_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "account_icon.png"))
# person_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "account_icon.png")) # TODO Changer l'image
# person_img = CTkImage(dark_image=person_img_light_data, light_image=person_img_light_data)


# """ --- Frames --- """


# def select_frame_by_name(frame_name):
#     frames = {
#         "home": (home_frame, "856x645"),
#         "geo01": (game_geo01_frame, "1200x645"),
#         "info02": (game_info02_frame, "1200x645"),
#         "info05": (game_info05_frame, "1200x645"),
#         "statistics": (statistics_frame, "856x645"),
#         "users": (users_frame, "856x645"),
#         "settings": (settings_frame, "856x645"),
#         "account": (account_frame, "856x645")
#     }

#     for name, (frame, size) in frames.items():
#         if name == frame_name:
#             frame.configure(fg_color=("gray75", "#00002E"))
#             app.geometry(size)
#             frame.pack(fill="both", expand=True)
#         else:
#             frame.configure(fg_color="transparent")
#             frame.pack_forget()


# """  Sidebar  """

# # Sidebar Frame
# sidebar_frame = CTkFrame(master=app, fg_color="#400241",  width=176, height=650, corner_radius=0)
# sidebar_frame.pack_propagate(0)
# sidebar_frame.pack(fill="y", anchor="w", side="left")


# # App Theme
# # def switch_theme():
# #     if sidebar_switch_theme_changer.get() == 1:
# #         set_appearance_mode("dark") # Dark Mode
# #         sidebar_switch_theme_changer.configure(progress_color="#663466", text_color="#51d743", button_color="#393939", button_hover_color="#5C5C5C")
# #     else:
# #         set_appearance_mode("light") # Light Mode
# #         sidebar_switch_theme_changer.configure(fg_color="#663466", text_color="#fff", button_color="#393939", button_hover_color="#5C5C5C")


# # Main Logo in Sidebar
# sidebar_frame_label = CTkLabel(master=sidebar_frame, text="", image=braingames_img)
# sidebar_frame_label.pack(pady=(38, 0), anchor="center")


# # --- Sidebar Buttons --- # TODO Ajouter les command= pour les boutons

# # Home (Menu) Button in Sidebar
# def home_button_event():
#     select_frame_by_name("home")
    
# sidebar_frame_home_button = CTkButton(master=sidebar_frame, image=home_img, text="Home", fg_color="transparent", text_color=("white","white"), font=braingames_sidebar_button_font, hover_color=("#000000"), anchor="w", command=home_button_event)
# sidebar_frame_home_button.pack(anchor="center", ipady=5, pady=(60, 0))

# # Create the Statistics Frame
# statistics_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)
# # Statistics (display_results) Button in Sidebar
# def statistics_button_event():
#     select_frame_by_name("statistics")
#     for widget in statistics_frame.winfo_children():
#         widget.destroy()
#     statistics_instance = Statistics(statistics_frame)
#     statistics_instance.pack(expand=True, fill='both')

# sidebar_frame_statistics_button = CTkButton(master=sidebar_frame, image=statistics_img, text="Statistics", fg_color="transparent", text_color=("white","white"), font=braingames_sidebar_button_font, hover_color="#000000", anchor="w", command=statistics_button_event)
# sidebar_frame_statistics_button.pack(anchor="center", ipady=5, pady=(16, 0))


# # Orders (User List)
# def users_button_event():
#     select_frame_by_name("users")
    
# sidebar_frame_users_button = CTkButton(master=sidebar_frame, image=users_img, text="Users", fg_color="transparent", text_color=("white","white"), font=braingames_sidebar_button_font, hover_color="#000000", anchor="w", command=users_button_event)
# sidebar_frame_users_button.pack(anchor="center", ipady=5, pady=(16, 0))


# # Settings Button in Sidebar
# def settings_button_event():
#     select_frame_by_name("settings")
    
# sidebar_frame_settings_button = CTkButton(master=sidebar_frame, image=settings_img, text="Settings", fg_color="transparent", text_color=("white","white"), font=braingames_sidebar_button_font, hover_color="#000000", anchor="w", command=settings_button_event)
# sidebar_frame_settings_button.pack(anchor="center", ipady=5, pady=(16, 0))


# # Account Button in Sidebar
# def account_button_event():
#     select_frame_by_name("account")
    
# sidebar_frame_account_button = CTkButton(master=sidebar_frame, image=person_img, text="Account", fg_color="transparent", text_color=("white","white"), font=braingames_sidebar_button_font, hover_color="#000000", anchor="w", command=account_button_event)
# sidebar_frame_account_button.pack(anchor="center", ipady=5, pady=(160, 0))


# # Switch Theme Button in Sidebar
# # sidebar_switch_theme_changer = CTkSwitch(master=sidebar_frame, command=switch_theme, fg_color="#663466", bg_color="transparent", button_color="#393939", button_hover_color="#5C5C5C", corner_radius=10, border_width=1, border_color="black", width=50, height=25, text_color="#fff", text="Dark Mode", font=braingames_sidebar_button_font)
# # sidebar_switch_theme_changer.pack(anchor="center", padx=(0,30), pady=(16, 0))

# # Author Label in Sidebar at the level as the switch but the switch ins't there for now
# sidebar_frame_author_label = CTkLabel(master=sidebar_frame, text="Made by Nico Mengisen", font=CTkFont(family="Sharp Grotesk Medium 20", size=12), text_color="#50d142")
# sidebar_frame_author_label.pack(anchor="center",  pady=(16, 0))


# """# --- Main View (Right Side) Frames ---"""


# """ Home Frame"""

# home_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)
# home_frame.pack_propagate(0)

# home_frame_title = CTkLabel(master=home_frame, fg_color="transparent", text="Welcome to Brain Games", font=braingames_title_font, text_color="#d292ff")
# home_frame_title.pack(anchor="w", padx=(63, 0), pady=(25, ))

# # Container for the statistics in Home Frame
# home_frame_stats_container = CTkFrame(master=home_frame, fg_color="transparent", width=464, height=70)
# home_frame_stats_container.pack_propagate(0)
# home_frame_stats_container.pack(anchor="center", padx=(0, 0), pady=(0, 0))

# # Time Played Frame
# home_frame_stats_time_played = CTkFrame(master=home_frame_stats_container, fg_color="#0000ff", width=132, height=70, corner_radius=7)
# home_frame_stats_time_played.pack_propagate(0)
# home_frame_stats_time_played.pack(side="left", padx=(0, 10))  # Use side="left" and add some padding if you want space between the frames

# # Time Played Title
# home_frame_stats_time_played_title_label = CTkLabel(master=home_frame_stats_time_played, text="Time Played", font=(braingames_regular_font, 10), text_color="#fff")
# home_frame_stats_time_played_title_label.pack(anchor="nw", padx=(14, 0))

# # Time Played Value
# home_frame_stats_time_played_value_label = CTkLabel(master=home_frame_stats_time_played, text=(f"70 min."), justify="left",  font=(braingames_title_font, 25), text_color="#fff")
# home_frame_stats_time_played_value_label.pack(anchor="nw", padx=(14, 0))


# # Number of Games Played Frame
# # Game Played Frame
# home_frame_stats_game_played = CTkFrame(master=home_frame_stats_container, fg_color="#0000ff", width=132, height=70, corner_radius=7)
# home_frame_stats_game_played.pack_propagate(0)
# home_frame_stats_game_played.pack(anchor="center", side="left", padx=(0, 10), pady=(0,0))

# # Game Played Title
# home_frame_stats_game_played_title_label = CTkLabel(master=home_frame_stats_game_played, text="Game Played", font=(braingames_regular_font, 10), text_color="#fff")
# home_frame_stats_game_played_title_label.pack(anchor="nw", padx=(14, 0))

# # Game Played Value #TODO Change the value to the number of games played by the user from the display_results.py view_total() function
# home_frame_stats_game_played_value_label = CTkLabel(master=home_frame_stats_game_played, text=(f"10"), justify="left",  font=(braingames_title_font, 25), text_color="#fff")
# home_frame_stats_game_played_value_label.pack(anchor="nw", padx=(14, 0))


# # Average Score Frame
# home_frame_stats_avg_score = CTkFrame(master=home_frame_stats_container, fg_color="#0000ff", width=132, height=70, corner_radius=7)
# home_frame_stats_avg_score.pack_propagate(0)
# home_frame_stats_avg_score.pack(anchor="center", side="left", padx=(0, 10), pady=(0,0))

# # Average Score Title
# home_frame_stats_game_avg_score_title_label = CTkLabel(master=home_frame_stats_avg_score, text="Average Score", font=(braingames_regular_font, 10), text_color="#fff")
# home_frame_stats_game_avg_score_title_label.pack(anchor="nw", padx=(14, 0))

# #TODO Change the value to the average score of the user from the display_results.py view_total() function
# home_frame_stats_game_avg_score_value_label = CTkLabel(master=home_frame_stats_avg_score, text=(f"30%"), justify="left",  font=(braingames_title_font, 25), text_color="#fff")
# home_frame_stats_game_avg_score_value_label.pack(anchor="nw", padx=(14, 0))



# """ Home Games Frame"""
# # Home Frame Subtitle
# home_frame_subtitle = CTkLabel(master=home_frame, text="Choose a game", font=braingames_subtitle_font, text_color="#d292ff")
# home_frame_subtitle.pack(anchor="n", pady=(40, 0), padx=(0, 290)) 

# # Game Menu in Home Frame
# home_frame_games = CTkFrame(master=home_frame, fg_color="transparent")
# home_frame_games.pack(pady=(5,0), padx=(0, 0), anchor="center")

# # Home Frame Games Buttons
# # Geo01 Game
# def geo01_button_event():
#     select_frame_by_name("geo01")
#     for widget in game_geo01_frame.winfo_children():
#         widget.destroy()
#     geo_game_instance = geo01.GeoGame(game_geo01_frame)
#     geo_game_instance.pack(fill="both", expand=True)
    
# home_frame_game_geo01_button = CTkButton(master=home_frame_games, text="", fg_color="transparent", image=geo01_img, hover_color="#393939", corner_radius=7, command=geo01_button_event)
# home_frame_game_geo01_button.grid(row=0, column=0, rowspan=2, sticky="w")

# # Info02 Game
# def info02_button_event():
#     select_frame_by_name("info02")
#     for widget in game_info02_frame.winfo_children():
#         widget.destroy()
#     info_game_instance = info02.Info02Game(game_info02_frame)
#     info_game_instance.pack(fill="both", expand=True)
    
# home_frame_game_info02_button = CTkButton(master=home_frame_games, text="", fg_color="transparent",image=info02_img, hover_color="#393939", corner_radius=7, command=info02_button_event)
# home_frame_game_info02_button.grid(row=0, column=1, sticky="w", pady=(7, 0))

# # Info05 Game
# def info05_button_event():
#     select_frame_by_name("info05")
#     for widget in game_info05_frame.winfo_children():
#         widget.destroy()
#     # info_game_instance = info05.InfoGame(game_info05_frame)
#     # info_game_instance.pack(fill="both", expand=True)
    
# home_frame_game_info05_button = CTkButton(master=home_frame_games, text="", fg_color="transparent", image=info05_img, hover_color="#393939", corner_radius=7, command=info05_button_event)
# home_frame_game_info05_button.grid(row=1, column=1, sticky="w", pady=(7, 0))

# # View Statistics From Home Frame
# home_view_statistics_button = CTkButton(master=home_frame_games, text="View Statistics", fg_color="#0000ff",font=braingames_regular_font, text_color="#fff", hover_color="#3c46ff", corner_radius=7, command=statistics_button_event)
# home_view_statistics_button.grid(row=3, column=0, columnspan=2, sticky="s", pady=(20, 0), padx=(0,80))


# # Create the Geo01 Frame
# game_geo01_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)
# game_geo01_frame.pack_propagate(0)

# # Create the Info02 Frame
# game_info02_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)
# game_info02_frame.pack_propagate(0)

# # Create the Info05 Frame
# game_info05_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)
# game_info05_frame.pack_propagate(0)

# # Create the Users Frame

# users_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)

# # Create the Settings Frame

# settings_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)

# # Create the Account Frame

# account_frame = CTkFrame(master=app, fg_color="transparent", width=680, height=650, corner_radius=0)



# # Check if the user is a teacher or admin, if yes, display the users and settings buttons in the sidebar


# # Check if user is logged in, if not, display the login page

# # def user_logged_in():
# #     return True

# # if user_logged_in():
# #     sidebar_frame_users_button.pack(anchor="center", ipady=5, pady=(16, 0))
# #     sidebar_frame_settings_button.pack(anchor="center", ipady=5, pady=(16, 0))
# #     sidebar_frame_account_button.pack(anchor="center", ipady=5, pady=(16, 0))
# # else:
# #     # TODO Display the login page
# #     pass

# """ Select Home Frame by default """
# select_frame_by_name("home")


# """ Launch App"""
# app.mainloop()

# """

# Class version of menu


import os
from customtkinter import *
import customtkinter as ctk
from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from tkinter import font
import matplotlib.pyplot as plt
import geo01, info02, info05
from display_statistics import Statistics
from database import Database

class App(CTkFrame):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.theme = "dark"
    
    
        self.setup_window()
        self.setup_assets()
        self.create_sidebar_frame()
        self.create_home_frame()
        self.create_geo01_frame()
        self.create_info02_frame()
        self.create_info05_frame()
        self.create_statistics_frame()
        self.create_users_frame()
        self.create_settings_frame()
        self.create_account_frame()
        
        self.db = Database(host='127.0.0.1', port='3306', user='root', password='root', database='brain_games_db')
        
        self.select_frame_by_name("home")
        
        def user_logged_in():
            return True
        
        if user_logged_in():
            self.sidebar_frame_users_button.pack(anchor="center", ipady=5, pady=(16, 0))
            self.sidebar_frame_settings_button.pack(anchor="center", ipady=5, pady=(16, 0))
            self.sidebar_frame_account_button.pack(anchor="center", ipady=5, pady=(16, 0))
        else:
            # TODO Display the login page
            pass
        
    def setup_window(self):
        self.parent.title("Brain Games")
        self.parent.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sidebar", "braingames_dark_ico.ico"))
        self.parent.geometry("856x645")
        self.parent.resizable(0,0)
        self.parent.configure(fg_color="#00002E")
        
    def setup_assets(self):
        assets_folder_menu = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "menu")
        

        assets_folder_home = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "home")
        assets_folder_sidebar_icons = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sidebar")
        assets_folder_users = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "users")
        
        # Main Brain Games Logo in Sidebar
        self.braingames_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "braingames_logo.png"))
        # braingames_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "braingames_dark.png"))
        self.braingames_img = CTkImage(dark_image=self.braingames_img_light_data, light_image=self.braingames_img_light_data, size=(87.68, 83,78))
        
        # Home (Menu) Icon in Sidebar
        self.home_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "home_light.png"))
        self.home_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "home_light.png"))
        self.home_img = CTkImage(dark_image=self.home_img_dark_data, light_image=self.home_img_light_data)

        # Geo01 (GeoGame) Icon in Home Frame
        self.geo01_img_light_data = Image.open(os.path.join(assets_folder_home, "geo01_button.png"))
        self.geo01_img_dark_data = Image.open(os.path.join(assets_folder_home, "geo01_button.png"))
        self.geo01_img = CTkImage(dark_image=self.geo01_img_dark_data, light_image=self.geo01_img_light_data, size=(236, 283))
        
        # Info02 (InfoGame) Icon in Home Frame
        self.info02_img_light_data = Image.open(os.path.join(assets_folder_home, "info02_button.png"))
        self.info02_img_dark_data = Image.open(os.path.join(assets_folder_home, "info02_button.png"))
        self.info02_img = CTkImage(dark_image=self.info02_img_dark_data, light_image=self.info02_img_light_data, size=(315, 122))
        
        # Info05 (InfoGame) Icon in Home Frame
        self.info05_img_light_data = Image.open(os.path.join(assets_folder_home, "info05_button.png"))
        self.info05_img_dark_data = Image.open(os.path.join(assets_folder_home, "info05_button.png"))
        self.info05_img = CTkImage(dark_image=self.info05_img_dark_data, light_image=self.info05_img_light_data,  size=(315, 122))
        
        # Statistics (display_results) Icon in Sidebar
        self.statistics_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "analytics_icon.png"))
        self.statistics_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "analytics_icon.png"))
        self.statistics_img = CTkImage(dark_image=self.statistics_img_light_data, light_image=self.statistics_img_light_data)
        
        # Orders (user_list_icon) Icon in Sidebar (it will only be visible for the admin and the teachers that have a role number "2", from there we can CRUD the users (students)))
        self.users_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "user_list_icon.png"))
        self.users_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "user_list_icon.png"))
        self.users_img = CTkImage(dark_image=self.users_img_light_data, light_image=self.users_img_light_data)
        
        # Settings Icon in Sidebar (the user can then change his password, his username, his name, his profile picture, etc...)
        self.settings_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "settings_icon.png"))
        self.settings_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "settings_icon.png"))
        self.settings_img = CTkImage(dark_image=self.settings_img_light_data, light_image=self.settings_img_light_data)
        
        # Account Icon in Sidebar (the user can then visualize his profile, his username, his profile picture, and his average score that he got in the games)
        self.person_img_light_data = Image.open(os.path.join(assets_folder_sidebar_icons, "account_icon.png"))
        self.person_img_dark_data = Image.open(os.path.join(assets_folder_sidebar_icons, "account_icon.png"))
        self.person_img = CTkImage(dark_image=self.person_img_light_data, light_image=self.person_img_light_data)
        
    def create_sidebar_frame(self):
        # Sidebar Frame
        self.sidebar_frame = CTkFrame(master=self, fg_color="#400241",  width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        
        # Main Logo in Sidebar
        self.sidebar_frame_label = CTkLabel(master=self.sidebar_frame, text="", image=self.braingames_img)
        self.sidebar_frame_label.pack(pady=(38, 0), anchor="center")
        
        # --- Sidebar Buttons --- # TODO Ajouter les command= pour les boutons
        
        # Home (Menu) Button in Sidebar
        def home_button_event():
            self.select_frame_by_name("home")
            
        self.sidebar_frame_home_button = CTkButton(master=self.sidebar_frame, image=self.home_img, text="Home", fg_color="transparent", text_color=("white","white"), font=CTkFont(family="Sharp Grotesk Medium 20", size=15, weight="bold"), hover_color=("#000000"), anchor="w", command=home_button_event)
        self.sidebar_frame_home_button.pack(anchor="center", ipady=5, pady=(60, 0))
        
        # Create the Statistics Frame
        self.statistics_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        
        # Statistics (display_results) Button in Sidebar
        def statistics_button_event():
            self.select_frame_by_name("statistics")
            for widget in self.statistics_frame.winfo_children():
                widget.destroy()
            statistics_instance = Statistics(self.statistics_frame)
            statistics_instance.pack(expand=True, fill='both')
        
        self.sidebar_frame_statistics_button = CTkButton(master=self.sidebar_frame, image=self.statistics_img, text="Statistics", fg_color="transparent", text_color=("white","white"), font=CTkFont(family="Sharp Grotesk Medium 20", size=15, weight="bold"), hover_color="#000000", anchor="w", command=statistics_button_event)
        self.sidebar_frame_statistics_button.pack(anchor="center", ipady=5, pady=(16, 0))

        
        # Orders (User List)
        def users_button_event():
            self.select_frame_by_name("users")
            
        self.sidebar_frame_users_button = CTkButton(master=self.sidebar_frame, image=self.users_img, text="Users", fg_color="transparent", text_color=("white","white"), font=CTkFont(family="Sharp Grotesk Medium 20", size=15, weight="bold"), hover_color="#000000", anchor="w", command=users_button_event)
        self.sidebar_frame_users_button.pack(anchor="center", ipady=5, pady=(16, 0))
        
        
        # Settings Button in Sidebar
        def settings_button_event():
            self.select_frame_by_name("settings")
            
        self.sidebar_frame_settings_button = CTkButton(master=self.sidebar_frame, image=self.settings_img, text="Settings", fg_color="transparent", text_color=("white","white"), font=CTkFont(family="Sharp Grotesk Medium 20", size=15, weight="bold"), hover_color="#000000", anchor="w", command=settings_button_event)
        self.sidebar_frame_settings_button.pack(anchor="center", ipady=5, pady=(16, 0))
        
        
        # Account Button in Sidebar
        def account_button_event():
            self.select_frame_by_name("account")
            
        self.sidebar_frame_account_button = CTkButton(master=self.sidebar_frame, image=self.person_img, text="Account", fg_color="transparent", text_color=("white","white"), font=CTkFont(family="Sharp Grotesk Medium 20", size=15, weight="bold"), hover_color="#000000", anchor="w", command=account_button_event)
        self.sidebar_frame_account_button.pack(anchor="center", ipady=5, pady=(160, 0))
        
        # Switch Theme Button in Sidebar
        # sidebar_switch_theme_changer = CTkSwitch(master=sidebar_frame, command=switch_theme, fg_color="#663466", bg_color="transparent", button_color="#393939", button_hover_color="#5C5C5C", corner_radius=10, border_width=1, border_color="black", width=50, height=25, text_color="#fff", text="Dark Mode", font=braingames_sidebar_button_font)
        # sidebar_switch_theme_changer.pack(anchor="center", padx=(0,30), pady=(16, 0))

        # Author Label in Sidebar at the level as the switch but the switch ins't there for now
        self.sidebar_frame_author_label = CTkLabel(master=self.sidebar_frame, text="Made by Nico Mengisen", font=CTkFont(family="Sharp Grotesk Medium 20", size=12), text_color="#50d142")
        self.sidebar_frame_author_label.pack(anchor="center",  pady=(16, 0))
        
    def create_home_frame(self):
        # Home Frame
        self.home_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.home_frame.pack_propagate(0)
        
        self.home_frame_title = CTkLabel(master=self.home_frame, fg_color="transparent", text="Welcome to Brain Games", font=CTkFont(family="Test Söhne Kräftig", size=40, weight="bold"), text_color="#d292ff")
        self.home_frame_title.pack(anchor="w", padx=(63, 0), pady=(25, ))
        
        # Container for the statistics in Home Frame
        self.home_frame_stats_container = CTkFrame(master=self.home_frame, fg_color="transparent", width=464, height=70)
        self.home_frame_stats_container.pack_propagate(0)
        self.home_frame_stats_container.pack(anchor="center", padx=(0, 0), pady=(0, 0))
        
        # Time Played Frame
        self.home_frame_stats_time_played = CTkFrame(master=self.home_frame_stats_container, fg_color="#0000ff", width=132, height=70, corner_radius=7)
        self.home_frame_stats_time_played.pack_propagate(0)
        self.home_frame_stats_time_played.pack(side="left", padx=(0, 10))  # Use side="left" and add some padding if you want space between the frames
        
        # Time Played Title
        
        self.home_frame_stats_time_played_title_label = CTkLabel(master=self.home_frame_stats_time_played, text="Time Played", font=(CTkFont(family="Test Söhne", size=14), 10), text_color="#fff")
        self.home_frame_stats_time_played_title_label.pack(anchor="nw", padx=(14, 0))
        
        # Time Played Value
        self.home_frame_stats_time_played_value_label = CTkLabel(master=self.home_frame_stats_time_played, text=(f"70 min."), justify="left",  font=(CTkFont(family="Test Söhne Kräftig", size=40, weight="bold"), 25), text_color="#fff")
        self.home_frame_stats_time_played_value_label.pack(anchor="nw", padx=(14, 0))
        
        
        # Number of Games Played Frame
        # Game Played Frame
        self.home_frame_stats_game_played = CTkFrame(master=self.home_frame_stats_container, fg_color="#0000ff", width=132, height=70, corner_radius=7)
        self.home_frame_stats_game_played.pack_propagate(0)
        self.home_frame_stats_game_played.pack(anchor="center", side="left", padx=(0, 10), pady=(0,0))
        
        # Game Played Title
        self.home_frame_stats_game_played_title_label = CTkLabel(master=self.home_frame_stats_game_played, text="Game Played", font=(CTkFont(family="Test Söhne", size=14), 10), text_color="#fff")
        self.home_frame_stats_game_played_title_label.pack(anchor="nw", padx=(14, 0))
        
        # Game Played Value #TODO Change the value to the number of games played by the user from the display_results.py view_total() function
        self.home_frame_stats_game_played_value_label = CTkLabel(master=self.home_frame_stats_game_played, text=(f"10"), justify="left",  font=(CTkFont(family="Test Söhne Kräftig", size=40, weight="bold"), 25), text_color="#fff")
        self.home_frame_stats_game_played_value_label.pack(anchor="nw", padx=(14, 0))
        
        
        # Average Score Frame
        self.home_frame_stats_avg_score = CTkFrame(master=self.home_frame_stats_container, fg_color="#0000ff", width=132, height=70, corner_radius=7)
        self.home_frame_stats_avg_score.pack_propagate(0)
        self.home_frame_stats_avg_score.pack(anchor="center", side="left", padx=(0, 10), pady=(0,0))
        
        # Average Score Title
        self.home_frame_stats_game_avg_score_title_label = CTkLabel(master=self.home_frame_stats_avg_score, text="Average Score", font=(CTkFont(family="Test Söhne", size=14), 10), text_color="#fff")
        self.home_frame_stats_game_avg_score_title_label.pack(anchor="nw", padx=(14, 0))
        
        #TODO Change the value to the average score of the user from the display_results.py view_total() function
        self.home_frame_stats_game_avg_score_value_label = CTkLabel(master=self.home_frame_stats_avg_score, text=(f"30%"), justify="left",  font=(CTkFont(family="Test Söhne Kräftig", size=40, weight="bold"), 25), text_color="#fff")
        self.home_frame_stats_game_avg_score_value_label.pack(anchor="nw", padx=(14, 0))
        
        
        
        """ Home Games Frame"""
        # Home Frame Subtitle
        self.home_frame_subtitle = CTkLabel(master=self.home_frame, text="Choose a game", font=CTkFont(family="Test Söhne Kräftig", size=30, weight="bold"), text_color="#d292ff")
        self.home_frame_subtitle.pack(anchor="n", pady=(40, 0), padx=(0, 290))
        
        # Game Menu in Home Frame
        self.home_frame_games = CTkFrame(master=self.home_frame, fg_color="transparent")
        self.home_frame_games.pack(pady=(5,0), padx=(0, 0), anchor="center")
        
        
        # Home Frame Games Buttons
        # Geo01 Game
        def geo01_button_event():
            self.select_frame_by_name("geo01")
            for widget in self.game_geo01_frame.winfo_children():
                widget.destroy()
            geo_game_instance = geo01.GeoGame(self.game_geo01_frame)
            geo_game_instance.pack(fill="both", expand=True)
            
        self.home_frame_game_geo01_button = CTkButton(master=self.home_frame_games, text="", fg_color="transparent", image=self.geo01_img, hover_color="#393939", corner_radius=7, command=geo01_button_event)
        self.home_frame_game_geo01_button.grid(row=0, column=0, rowspan=2, sticky="w")
        
        # Info02 Game
        def info02_button_event():
            self.select_frame_by_name("info02")
            for widget in self.game_info02_frame.winfo_children():
                widget.destroy()
            info_game_instance = info02.Info02Game(self.game_info02_frame)
            info_game_instance.pack(fill="both", expand=True)
            
        self.home_frame_game_info02_button = CTkButton(master=self.home_frame_games, text="", fg_color="transparent",image=self.info02_img, hover_color="#393939", corner_radius=7, command=info02_button_event)
        self.home_frame_game_info02_button.grid(row=0, column=1, sticky="w", pady=(7, 0))

        # Info05 Game
        def info05_button_event():
            self.select_frame_by_name("info05")
            for widget in self.game_info05_frame.winfo_children():
                widget.destroy()
            # info_game_instance = info05.InfoGame(self.game_info05_frame)
            # info_game_instance.pack(fill="both", expand=True)
            
        self.home_frame_game_info05_button = CTkButton(master=self.home_frame_games, text="", fg_color="transparent", image=self.info05_img, hover_color="#393939", corner_radius=7, command=info05_button_event)
        self.home_frame_game_info05_button.grid(row=1, column=1, sticky="w", pady=(7, 0))
        
        # View Statistics From Home Frame
        def statistics_button_event():
            self.select_frame_by_name("statistics")
            for widget in self.statistics_frame.winfo_children():
                widget.destroy()
            statistics_instance = Statistics(self.statistics_frame)
            statistics_instance.pack(expand=True, fill='both')
                    
        self.home_view_statistics_button = CTkButton(master=self.home_frame_games, text="View Statistics", fg_color="#0000ff",font=CTkFont(family="Test Söhne Kräftig", size=15, weight="bold"), text_color="#fff", hover_color="#3c46ff", corner_radius=7, command=statistics_button_event)
        self.home_view_statistics_button.grid(row=3, column=0, columnspan=2, sticky="s", pady=(20, 0), padx=(0,80))
        
    def create_geo01_frame(self):
        # Create the Geo01 Frame
        self.game_geo01_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.game_geo01_frame.pack_propagate(0)
        
    def create_info02_frame(self):
        # Create the Info02 Frame
        self.game_info02_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.game_info02_frame.pack_propagate(0)
        
    def create_info05_frame(self):
        # Create the Info05 Frame
        self.game_info05_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.game_info05_frame.pack_propagate(0)
        
    def create_statistics_frame(self):
        # Create the Statistics Frame
        self.statistics_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.statistics_frame.pack_propagate(0)
        
    def create_users_frame(self):
        # Create the Users Frame
        self.users_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.users_frame.pack_propagate(0)
        
    def create_settings_frame(self):
        # Create the Settings Frame
        self.settings_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.settings_frame.pack_propagate(0)
        
    def create_account_frame(self):
        # Create the Account Frame
        self.account_frame = CTkFrame(master=self, fg_color="transparent", width=680, height=650, corner_radius=0)
        self.account_frame.pack_propagate(0)
        
    def select_frame_by_name(self, frame_name):
        for frame in self.winfo_children():
            if frame.winfo_name() == frame_name:
                frame.configure(fg_color="transparent")
                frame.pack(fill="both", expand=True)
            else:
                frame.configure(fg_color="transparent")
                frame.pack_forget()
                
    def switch_theme(self):
        if self.sidebar_switch_theme_changer.get() == 1:
            self.set_appearance_mode("dark")
            self.sidebar_switch_theme_changer.configure(progress_color="#663466", text_color="#51d743", button_color="#393939", button_hover_color="#5C5C5C")
        else:
            self.set_appearance_mode("light")
            self.sidebar_switch_theme_changer.configure(fg_color="#663466", text_color="#fff", button_color="#393939", button_hover_color="#5C5C5C")
            
    def set_appearance_mode(self, mode):
        if mode == "dark":
            self.parent.theme = "dark"
            self.parent.configure(bg="#00002E", fg="#fff")
            self.sidebar_frame.configure(fg_color="#400241")
            self.sidebar_frame_label.configure(image=self.braingames_img)
            self.sidebar_frame_home_button.configure(image=self.home_img, text_color=("white","white"))
            self.sidebar_frame_statistics_button.configure(image=self.statistics_img, text_color=("white","white"))
            self.sidebar_frame_users_button.configure(image=self.users_img, text_color=("white","white"))
            self.sidebar_frame_settings_button.configure(image=self.settings_img, text_color=("white","white"))
            self.sidebar_frame_account_button.configure(image=self.person_img, text_color=("white","white"))
            self.sidebar_frame_author_label.configure(text_color="#50d142")
            self.home_frame_title.configure(text_color="#d292ff")
            self.home_frame_subtitle.configure(text_color="#d292ff")
            self.home_frame_stats_time_played.configure(fg_color="#0000ff")
            self.home_frame_stats_game_played.configure(fg_color="#0000ff")
            self.home_frame_stats_avg_score.configure(fg_color="#0000ff")
            self.home_frame_stats_time_played_title_label.configure(text_color="#fff")
            self.home_frame_stats_time_played_value_label.configure(text_color="#fff")
            self.home_frame_stats_game_played_title_label.configure(text_color="#fff")
            self.home_frame_stats_game_played_value_label.configure(text_color="#fff")
            self.home_frame_stats_game_avg_score_title_label.configure(text_color="#fff")
            self.home_frame_stats_game_avg_score_value_label.configure(text_color="#fff")
            self.home_view_statistics_button.configure(fg_color="#0000ff", text_color="#fff", hover_color="#3c46ff")
            
        elif mode == "light":
            self.parent.theme = "light"
            self.parent.configure(bg="#fff", fg="#00002E")
            self.sidebar_frame.configure(fg_color="#fff")
            self.sidebar_frame_label.configure(image=self.braingames_img)
            self.sidebar_frame_home_button.configure(image=self.home_img, text_color=("black","black"))
            self.sidebar_frame_statistics_button.configure(image=self.statistics_img, text_color=("black","black"))
            self.sidebar_frame_users_button.configure(image=self.users_img, text_color=("black","black"))
            self.sidebar_frame_settings_button.configure(image=self.settings_img, text_color=("black","black"))
            self.sidebar_frame
            self.sidebar_frame_account_button.configure(image=self.person_img, text_color=("black","black"))
            self.sidebar_frame_author_label.configure(text_color="#50d142")
            self.home_frame_title.configure(text_color="#d292ff")
            self.home_frame_subtitle.configure(text_color="#d292ff")
            self.home_frame_stats_time_played.configure(fg_color="#0000ff")
            self.home_frame_stats_game_played.configure(fg_color="#0000ff")
            self.home_frame_stats_avg_score.configure(fg_color="#0000ff")
            self.home_frame_stats_time_played_title_label.configure(text_color="#fff")
            self.home_frame_stats_time_played_value_label.configure(text_color="#fff")
            self.home_frame_stats_game_played_title_label.configure(text_color="#fff")
            self.home_frame_stats_game_played_value_label.configure(text_color="#fff")
            self.home_frame_stats_game_avg_score_title_label.configure(text_color="#fff")
            self.home_frame_stats_game_avg_score_value_label.configure(text_color="#fff")
            self.home_view_statistics_button.configure(fg_color="#0000ff", text_color="#fff", hover_color="#3c46ff")
            
        else:
            raise ValueError("Invalid appearance mode")
        
    def run(self):
        self.parent.mainloop()
        
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    app.run()
                                                    
        