import glob
import tkinter as tk
from tkinter import *
import vlc

# Define a function to get the last element of a list
def last(list):
    return list[-1]

# Define a function to extract the name of the currently playing music
def music_name():
    global my_music, music_number
    return last(my_music[music_number].split('/'))

# Define a function to play music
def play_music():
    global music_number, my_music, player, instance
    to_play = my_music[music_number]
    media = instance.media_new(to_play)
    player.set_media(media)
    player.play()

# Define a function to pause music
def pause_music():
    player.pause()

# Define a function to play the next music
def next_music():
    global music_number, my_music, music_label
    if music_number < len(my_music) - 1:
        music_number += 1
    music_label.config(text=str(music_name()))

# Define a function to play the previous music
def previous_music():
    global music_number, my_music, music_label
    if music_number > 0:
        music_number -= 1
    music_label.config(text=str(music_name()))

# Initialize music number
music_number = 0

# Create a Tkinter window
window = Tk()
window.geometry('330x120')
window.resizable(False, False)
window.title('Mp3 Player')

# Initialize VLC instance and media player
instance = vlc.Instance()
player = instance.media_player_new()

# Get list of music files
my_music = glob.glob('/home/shitij_agrawal/Music/*.mp3')  # path to music folder

# Load images for buttons
play_image = PhotoImage(file='images/play.png')
pause_image = PhotoImage(file='images/pause.png')
forward_image = PhotoImage(file='images/forward.png')
backward_image = PhotoImage(file='images/backward.png')
stop_image = PhotoImage(file='images/stop.png')

# Create a label to display music name
music_label = tk.Label(window, text=music_name())

# Create buttons for controlling music playback
play = tk.Button(window, image=play_image, command=play_music)
pause = tk.Button(window, image=pause_image, command=pause_music)
forward = tk.Button(window, image=forward_image, command=next_music)
backward = tk.Button(window, image=backward_image, command=previous_music)
stop = tk.Button(window, image=stop_image, command=lambda: sys.exit())

# Place buttons and label in the window
play.place(x=130, y=50)
pause.place(x=10, y=50)
forward.place(x=190, y=50)
backward.place(x=70, y=50)
stop.place(x=250, y=50)
music_label.place(x=10, y=0)

# Start the Tkinter event loop
window.mainloop()
