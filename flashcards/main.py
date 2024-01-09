from tkinter import Tk, PhotoImage, Button

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

button = Button(image=card_back_img, highlightthickness=0)
button.grid(row=0, column=0, columnspan=3)


window.mainloop()
