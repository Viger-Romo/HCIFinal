import pyttsx3
import tkinter as tk
import threading


def speak_text():
    def speak():
        text = text_entry.get("1.0", tk.END)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


        speak_button.config(state=tk.NORMAL)

    speak_button.config(state=tk.DISABLED)

    speak_thread = threading.Thread(target=speak)
    speak_thread.start()


window = tk.Tk()
window.title("HCI Final Project: Incredible Eels")
window.geometry("800x300")

label = tk.Label(window, text="Enter Text Here:")
label.pack()

# note: maybe change the font here? font=("Helvetica", 16) for example
text_entry = tk.Text(window, height=13, width=35)
text_entry.pack()

speak_button = tk.Button(window, text="Speak", bg="BLUE", fg="White", command=speak_text)
speak_button.pack()

window.mainloop()