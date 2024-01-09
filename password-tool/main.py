from tkinter import (Tk, PhotoImage, messagebox,
                     Canvas, Label, Entry, Button, StringVar, END)
import random
import pyperclip
import json

PASSWORD_FILE = "passwords.json"
DEFAULT_EMAIL = "ck@pm.me"
FONT_NAME = "Arial"


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# ---------------- PASSWORD GENERATOR --------------- #


def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!#$%&()*+"
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [random.choice(chars) for _ in range(nr_letters)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pw_list = pw_letters + pw_numbers + pw_symbols
    shuffled_pw = shuffle_list(pw_list)
    clear_password_entry()
    password_entry.insert(0, string=shuffled_pw)
    pyperclip.copy(shuffled_pw)


def shuffle_list(char_list):
    random.shuffle(char_list)
    shuffled_string = ''.join(char_list)
    return shuffled_string


def clear_password_entry():
    content = password_entry.get()
    if content:
        password_entry.delete(0, END)


# ------------------ SAVE PASSWORD ------------------ #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:   {
            "email": username,
            "password": password,
        }
    }

    if website and username and password:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered:\nEmail: {username}\nPassword: {password} \n\nIs it OK to save?")
        if is_ok:
            try:
                with open(PASSWORD_FILE, "r") as file:
                    data = json.load(file)
                    # Not just appending, we need a valid json structure
                    data.update(new_data)
            except FileNotFoundError:
                write_json(new_data)
            else:
                write_json(data)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                info_msg("Password saved.")

    else:
        alert_msg("Not all fields\n are filled.")


def write_json(data):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ------------------ UI SETUP --------------------- #


def reset_msg():
    message_label.config(text="")


def alert_msg(text):
    message_label.config(text=text,
                         fg=RED, font=(FONT_NAME, 18, "bold"))
    messagebox.showerror(title="ERROR", message=text)


def info_msg(text):
    message_label.config(text=text,
                         fg=GREEN, font=(FONT_NAME, 18, "normal"))
    messagebox.showinfo(title="INFO", message=text)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

mypass_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(120, 100, image=mypass_img)
# timer_text = canvas.create_text(
#    100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=0, column=1)


message_label = Label(text="", font=(FONT_NAME))
message_label.grid(row=0, column=0)

website_label = Label(text="Website:", font=(FONT_NAME))
website_label.grid(row=1, column=0)
website = StringVar()
website_entry = Entry(width=35, textvariable=website)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")

username_label = Label(text="Email/Username:", font=(FONT_NAME))
username_label.grid(row=2, column=0)
username = StringVar()
username_entry = Entry(width=35, textvariable=username)
username_entry.insert(0, DEFAULT_EMAIL)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")


password_label = Label(text="Password:", font=(FONT_NAME))
password_label.grid(row=3, column=0)
password = StringVar()
password_entry = Entry(width=21, textvariable=password)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36,
                    highlightthickness=0, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
