"""
created on : 10/01/20
@author JAJA

"""

from tkinter import *
from gtts import gTTS
from playsound import playsound

win = Tk()
win.title("Text2Speech")
win.geometry("400x100")


def text_to_speech():
    text = entry.get()
    speech = gTTS(text=text, lang="en")
    speech.save(r'audio.mp3')
    playsound(r'audio.mp3')


label = Label(win, text="Enter Here :")
entry = Entry(win)
button = Button(win, text="Go", command=text_to_speech)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)


win.mainloop()
