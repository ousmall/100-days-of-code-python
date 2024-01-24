from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
circulation = 0  # repetitions
time_count = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(time_count)
    top_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00", fill="white")
    check_mark.config(text="")
    global circulation
    circulation = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global circulation
    circulation += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    # short break at 2nd/4th/6th round
    if circulation % 2 == 0:
        count_down(short_break)
        top_title.config(text="Break", fg=PINK)

    # long break at 8th round
    elif circulation % 8 == 0:
        count_down(long_break)
        top_title.config(text="Rest", fg=PINK)

    #  work time at 1st/3rd/5th/7th round
    else:
        count_down(work)
        top_title.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)  # 向下取整
    count_sec = count % 60
    '''if count_sec < 10:
        count_sec = f"0{count_sec}"'''  # 这个是老师的方法

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    # canvas.itemconfig(item_id, option1=value1, option2=value2, ...),用于配置和修改Canvas上的图形项（item）
    # f"{number:02d}"显示两位数字
    if count > 0:
        global time_count
        time_count = window.after(1000, count_down, count - 1)
        # window.after(delay, callback, *args, **kwargs),安排一个函数在指定的毫秒数之后执行，实现定时操作
        canvas.itemconfig(timer_text, fill="white")
    if count < 60:
        canvas.itemconfig(timer_text, fill="RED")
    if count == 0:
        canvas.itemconfig(timer_text, fill="white")
        start_count()
        marks = ""
        work_session = math.floor(circulation / 2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Todo 1: set up a window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Todo 2: set up the tomato with canvas
# use 'highlightthickness' keyword to remove the border
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
# PhotoImage() is a class in Tk to show images data
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=2, row=2)


# Todo 3: set up labels, buttons
top_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
top_title.grid(column=2, row=1)

check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column=2, row=4)

start = Button(text="Start", highlightthickness=0, command=start_count)  # actually, I can't see that white border
start.grid(column=1, row=3)

reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.grid(column=3, row=3)


window.mainloop()
