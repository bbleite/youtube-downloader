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

# Add UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link") # Title label
title.pack(padx=10, pady=10) # Padding

# Link input
link = customtkinter.CTkEntry(app,  width=350, height=40)
link.pack()
# Run app
app.mainloop()