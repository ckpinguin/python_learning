from tkinter import Tk, PhotoImage, Canvas

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Arial"
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

mypass_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=mypass_img)
# timer_text = canvas.create_text(
#    100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


window.mainloop()
