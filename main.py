import tkinter 
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System") # Dark/Light mode 
customtkinter.set_default_color_theme("blue") # Color scheme

# App Frame
app = customtkinter.CTk() # Initialize custom tkinter object 
app.geometry("720x480")
app.title("YouTube Downloader")

# Run app
app.mainloop()