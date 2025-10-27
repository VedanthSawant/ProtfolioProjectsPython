from tkinter import *
import pandas as pd
import random, os

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
FILE_PATH = "data/french_words.csv"
card_dtl = {}
flip_timer = None
file_data = {}


def front_data_dtls(button_type):
    global card_dtl, flip_timer, file_data
    if button_type == "RIGHT":
        file_data.remove(card_dtl)
        new_dataframe = pd.DataFrame(file_data)
        if new_dataframe.empty:
            os.remove("data/words_to_learn.csv")
        else:
            new_dataframe.to_csv("data/words_to_learn.csv", index=False)

    if not os.path.exists("data/words_to_learn.csv"):
        dataframe = pd.read_csv(FILE_PATH)
    else:
        dataframe = pd.read_csv("data/words_to_learn.csv")
    file_data = dataframe.to_dict(orient="records")
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    card_dtl = random.choice(file_data)
    canvas.itemconfig(title_word, text="French", fill="black")
    canvas.itemconfig(french_word, text=card_dtl['French'], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_word, text="English", fill="white")
    canvas.itemconfig(french_word, text=card_dtl['English'], fill="white")
    canvas.itemconfig(canvas_image, image=back_card)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 326, image=front_card)
title_word = canvas.create_text(400, 250, text="Title", font=(FONT_NAME, 40, "italic"), fill="black")
french_word = canvas.create_text(400, 373, text="word", font=(FONT_NAME, 40, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

my_right_btn = PhotoImage(file="images/right.png")
right_button = Button(image=my_right_btn, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0,
                      command=lambda: front_data_dtls("RIGHT"))
right_button.grid(row=1, column=0)

my_wrong_btn = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_wrong_btn, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0,
                      command=lambda: front_data_dtls("WRONG"))
wrong_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
front_data_dtls("START")

window.mainloop()
