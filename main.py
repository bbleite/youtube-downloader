import tkinter 
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get() # Get youtube link
        ytObject = YouTube(ytLink, on_progress_callback=on_progress) # Create youtube object
        video = ytObject.streams.get_highest_resolution() # Get highest resolution video
        
        download.configure(text="Downloading...")
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download() # download video
        finishLabel.configure(text="Download Complete!")
        download.configure(text="Done")
    except:
        finishLabel.configure(text="Download Error", text_color="red")
        print("Erro")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percetage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percetage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Update progress bar
    progressBar.set(float(percetage_of_completion) / 100)

# System Settings
customtkinter.set_appearance_mode("System") # Dark/Light mode 
customtkinter.set_default_color_theme("blue") # Color scheme

# App Frame
app = customtkinter.CTk() # Initialize custom tkinter object 
app.geometry("720x480")
app.title("YouTube Downloader")

# Add UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link") # Title label
title.pack(padx=10, pady=10) # .pack() makes the element show on screen

# Link input
url_var = tkinter.StringVar() # Store user's input in this variable
link = customtkinter.CTkEntry(app,  width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


# Run app
app.mainloop()