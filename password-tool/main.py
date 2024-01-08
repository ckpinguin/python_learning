from tkinter import Tk, PhotoImage, Label, Canvas
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Arial"
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

mypass_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(200, 189, image=mypass_img, )
timer_text = canvas.create_text(
    100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
