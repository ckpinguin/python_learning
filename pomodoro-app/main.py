from tkinter import Tk, Label, Canvas, PhotoImage, Button


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔️"

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


status_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48))
status_label.grid(row=0, column=1)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img, )
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


def start_timer():
    secs = WORK_MIN * 60
    count_down(secs)


def reset_timer():
    pass


def count_down(count):
    minutes, seconds = divmod(count, 60)
    text = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(timer_text, text=text)
    if count > 0:
        window.after(1000, count_down, count-1)


start_button = Button(text="Start", bg=YELLOW,
                      highlightbackground=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset", bg=YELLOW,
                      highlightbackground=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks_label = Label(text="✓", font=(
    FONT_NAME, 32, "bold"), bg=YELLOW, fg=GREEN)
checkmarks_label.grid(row=3, column=1)

window.mainloop()
