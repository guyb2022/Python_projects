from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def button_reset_clicked():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_count, text="00:00")
    my_label.config(text="Timer", fg=GREEN)
    my_label2.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def button_start_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_work_sec = SHORT_BREAK_MIN*60
    long_work_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_work_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_work_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = count//60
    seconds = count % 60
    global timer
    if int(seconds) < 10:
        seconds = '0' + str(seconds)
    canvas.itemconfig(timer_count, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = canvas.after(1000, count_down, count - 1)
    else:
        button_start_clicked()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        my_label2.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=300, height=200)
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00",fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
my_label = Label(text="Timer", font=("Ariel", 40), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

button_start = Button(text='Start', command=button_start_clicked, bg=YELLOW, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', command=button_reset_clicked, bg=YELLOW, highlightthickness=0)
button_reset.grid(column=2, row=2)

my_label2 = Label(font=("Ariel", 20), fg=GREEN, bg=YELLOW)
my_label2.grid(column=1, row=3)

window.mainloop()
