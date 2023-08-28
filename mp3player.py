import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root =Tk()
root.title('Music Player')
root.geometry("485x700+290+10")
root.configure(bg="#58E2D7")
root.resizable(False,False)
mixer.init()

def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_music():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

lower_frame = Frame(root, bg="#4055F6",width=485,height=180)
lower_frame.place(x=0,y=400)

image_icon = PhotoImage(file="logo png.png")
root.iconphoto(False,image_icon)

frame_count=30
frames= [PhotoImage(file="aa1.gif",format="gif -index %i" %(i))for i in range(frame_count)]


def update(index):
    frame = frames[index]
    index+=1
    if index==frame_count:
        index=0
    label.configure(image=frame)
    root.after(40,update,index)
label = Label(root)
label.place(x=0,y=0)
root.after(0,update,0)

play_button = PhotoImage(file="play1.png")
Button(root,image=play_button,bg='#FFFFFF',bd=0,height=60,width=60,command=play_music).place(x=215, y=487)

stop_button = PhotoImage(file='stop1.png')
Button(root,image=stop_button,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.stop).place(x=130, y=487)

volume_button = PhotoImage(file="volume.png")
Button(root,image=volume_button,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.unpause).place(x=20, y=487)

pause_button = PhotoImage(file="pause1.png")
Button(root,image=pause_button,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.pause).place(x=300, y=487)

menu = PhotoImage(file="menu.png")
Label(root,image=menu).place(x=0, y=580, width=485, height=120)

frame_music = Frame(root,bd=2,relief=RIDGE)
frame_music.place(x=0, y=585, width=485, height=100)
Button(root, text="Browse Music", width=59, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="#FFFFFF", command=add_music).place(x=0, y=550)

scroll = Scrollbar(frame_music)
playlist = Listbox(frame_music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=RIGHT, fill=BOTH)


root.mainloop()
