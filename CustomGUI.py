import pyttsx3
import customtkinter as ctk
from tkinter import font
import threading

from customtkinter import CTkLabel

# Initialize customtkinter
ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

def speak_text():
    def speak():
        text = text_entry.get("1.0", "end").strip()
        if text:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        speak_button.configure(state="normal")

    speak_button.configure(state="disabled")
    speak_thread = threading.Thread(target=speak)
    speak_thread.start()

def change_font():
    select_font = font_var.get()
    text_entry.configure(font=(select_font, font_size.get()))

def increase_font_size(size):
    text_entry.configure(font=(font_var.get(), int(size)))

def background_color(choice):
    color = color_dict[choice]
    #ctk.set_appearance_mode(color)
    window.configure(fg_color=color)
    text_entry.configure(fg_color=color)
    font_button_frame.configure(fg_color=color)


#Function that adjusts the spacing between words in the text entry
def increase_word_spacing(value):
    current_text = text_entry.get("1.0", "end").strip()  # Get the current text
    words = current_text.split()  # Split the text into words

    # Add spaces between words based on the slider value
    space_factor = int(value)
    spaced_text = (' ' * space_factor).join(words)

    # Update the text entry with the newly spaced text while preserving line breaks
    text_entry.delete("1.0", "end")
    text_entry.insert("1.0", spaced_text)  # Insert the newly formatted text


# Main Window
window = ctk.CTk()
window.title("HCI Final Project: Incredible Eels")
window.geometry("800x900")

# Custom Font for the Widgets
custom_font = font.Font(family="Helvetica", size=16)

# Text Entry Section
text_label = ctk.CTkLabel(window, text="Enter Text Here:", font=("Helvetica", 24, "bold"))
text_label.grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky="n")  # Center the label

# Text Entry Section with Black Outline
text_frame = ctk.CTkFrame(window, fg_color="black", corner_radius=0)  # Black border frame
text_frame.grid(row=1, column=0, columnspan=2, pady=(5, 10), padx=10)

text_entry = ctk.CTkTextbox(text_frame, height=300, width=600, font=("Helvetica", 16))
text_entry.grid(row=0, column=0, padx=2, pady=2)  # Add padding to simulate border thickness

# Speak Button
speak_button = ctk.CTkButton(window, text="Speak", fg_color="blue", text_color="white", command=speak_text)
speak_button.grid(row=2, column=0, columnspan=2, pady=(0, 20))

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)


#Background Options
color_listbox_label = ctk.CTkLabel(window, text="Select a Background Color:", font=("Helvetica", 24, "bold"))
color_listbox_label.grid(row=3, column = 0, pady=50)

color_dict = {

    "White" : "White",
    "Soft Yellow": "#fff49b",
    "Yellow": "yellow",
    "Light Cream": "#FFFDD0",
    "Light Blue": "#add8e6",
    "Peach": "#FFDAB9",
    "Light Grey": "#D3D3D3",
    "Orange": "#FFA500",
}
color_var = ctk.StringVar(value="None")
color_listbox = ctk.CTkOptionMenu(window, variable=color_var, values=list(color_dict.keys()), command=background_color, text_color="black", font=("Helvetica", 24, "bold"), dropdown_font=("Helvetica", 24, "bold"), button_color="grey", fg_color="light grey")
color_listbox.grid(row=4, column=0, pady=(0,150))


#Font Options
radioButton_fontLabel = ctk.CTkLabel(window, text="Select a Font:", font=("Helvetica", 24, "bold"))
radioButton_fontLabel.grid(row=3, column = 1, padx=20, pady=(0, 0))

font_var = ctk.StringVar(value="Helvetica")
fonts = ["Helvetica", "Arial", "Verdana", "Calibri", "Comic Sans MS", "Century Gothic"]
font_button_frame = ctk.CTkFrame(window)
font_button_frame.grid(row=4, column=1,pady=(0, 20))

for i, font_name in enumerate(fonts):
    ctk.CTkRadioButton(font_button_frame, text=font_name, variable=font_var, value=font_name, command=change_font, fg_color="black", font=("Helvetica", 24, "bold")).grid(row=i, column=0, sticky="w")



#Font Slider
fontResize_label = ctk.CTkLabel(window, text= "Increase/Decrease Font Size:", font=("Helvetica", 24, "bold"))
fontResize_label.grid(row=5, column=0, columnspan=2, sticky="n")
font_size = ctk.IntVar(value=16)
font_scale = ctk.CTkSlider(window, from_=14, to=42, variable=font_size, command=increase_font_size, button_color="black")
font_scale.grid(row=6, column =0, columnspan =2)


#Label for word spacing slider
word_spacing_label = ctk.CTkLabel(window, text="Adjust Word Spacing:", font=("Helvetica", 24, "bold"))
word_spacing_label.grid(row=7, column=0, columnspan=2, pady=(20, 5))  # Added below font slider

# Line Spacing Slider
word_spacing = ctk.IntVar(value=1)
word_spacing_slider = ctk.CTkSlider(window, from_=1, to=5, variable=word_spacing,command=increase_word_spacing, button_color="black")
word_spacing_slider.grid(row=8, column=0, columnspan=2, pady=(0, 20))


window.mainloop()
