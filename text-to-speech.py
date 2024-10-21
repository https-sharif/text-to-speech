from gtts import gTTS
from io import BytesIO
import pygame
import tkinter as tk
from tkinter import messagebox

def speak(event=None):
    text = text_entry.get()

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    try:
        tts = gTTS(text=text, lang='en')
        audio = BytesIO()
        tts.write_to_fp(audio)

        audio.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(audio, 'mp3')
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_text():
    text_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Text to Speech")


text_label = tk.Label(root, text="Enter text to speak:")
text_label.pack(pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=5, padx=25)


text_entry = tk.Entry(entry_frame, width=30)
text_entry.pack(side=tk.LEFT)

clear_button = tk.Button(entry_frame, text="X", command=clear_text, fg='black')
clear_button.pack(side=tk.LEFT, padx=5) 

speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack(pady=20)

text_entry.bind("<Return>", speak)

root.mainloop()
