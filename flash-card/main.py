from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# GENERATE RANDOM WORD
def generate_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text='French', fill='Black')
    canvas.itemconfig(word, text=current_card['French'], fill='Black')
    canvas.itemconfig(background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


# FLIP CARD
def flip_card():
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')
    canvas.itemconfig(background, image=back_img)


# REMOVE KNOWN WORD
def is_known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv('./data/words_to_learn.csv', index=False)
    generate_random_word()


# UI
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
background = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

button_right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)
button_wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=generate_random_word)
button_wrong.grid(row=1, column=0)

generate_random_word()

window.mainloop()
