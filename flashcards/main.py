from tkinter import Tk, PhotoImage, Button, Label, Canvas
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
FILENAME = "data/french_words.csv"

df = pandas.read_csv(FILENAME)
words_dict = df.to_dict(orient="records")
print(words_dict)

##### UI ######
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", fill="black",
                   font=(FONT, 40, "italic"))

canvas.create_text(400, 263, text="Word", fill="black",
                   font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_img, highlightthickness=0,
    border=0,
    bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)


window.mainloop()
