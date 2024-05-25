from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
learn={}
current_card={}
#to save the progress
try:
    df = pd.read_csv(filepath_or_buffer='data/words_to_learn.csv')
except FileNotFoundError:
    #if the words to learn file doesn't exist, we resume with our original list
    df = pd.read_csv(filepath_or_buffer='data/french_words.csv')
    # Convert the DataFrame to a list of dictionaries
    learn = df.to_dict(orient="records")
else:
    learn = df.to_dict(orient="records")


def show_english():
    canvas.itemconfig(create, image=canvas_back_img)
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=current_card["English"],fill="white")
    window.after(3000, next_card)

def next_card():
    global current_card,timer
    window.after_cancel(timer)
    current_card = random.choice(learn)
    canvas.itemconfig(create, image=canvas_front_img)
    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(word, text=current_card["French"],fill="black")
    timer = window.after(3000, show_english)

def is_known():
    #to remove the words that the user already knows from the list
    #need to update the csv
    learn.remove(current_card)
    data_new=pd.DataFrame(learn)
    data_new.to_csv("data/words_to_learn.csv")

    next_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, show_english)

# Use canvas to place multiple things
canvas = Canvas(width=800, height=500)
canvas_front_img = PhotoImage(file='images/card_front.png')
canvas_back_img = PhotoImage(file='images/card_back.png')
create = canvas.create_image(400, 263, image=canvas_front_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text='', font=('Ariel', 40, "italic"))
word = canvas.create_text(400, 263, text='', font=('Ariel', 60, "bold"))

correct_image = PhotoImage(file='images/right.png')
corr_button = Button(image=correct_image, command=is_known)
corr_button.grid(row=1, column=0)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.grid(row=1, column=1)

# Start the flash card cycle
next_card()

window.mainloop()
