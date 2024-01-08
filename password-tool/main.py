from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pw_length = 10
    chars = "abcdefghijklmnopqrstuvwxyz1234567890_?!"
    pw = ""
    for _ in range(0, pw_length):
        pw += random.choice(chars)
    clear_password_entry()
    password_entry.insert(END, string=pw)


def clear_password_entry():
    content = password_entry.get()
    if content:
        password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
PASSWORD_FILE = "passwords.txt"


def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{website} / {username}: {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Arial"
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

mypass_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(120, 100, image=mypass_img)
# timer_text = canvas.create_text(
#    100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=(FONT_NAME))
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

username_label = Label(text="Email/Username:", font=(FONT_NAME))
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")


password_label = Label(text="Password:", font=(FONT_NAME))
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36,
                    highlightthickness=0, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
