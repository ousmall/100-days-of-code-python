from tkinter import *


def button_clicked():
    new_value = mile_input.get()
    output_label.config(text=float(new_value) * 1.609)
    # km = float(new_value) * 1.609
    # output_label.config(text=f"{km}") 老师把value转换成str再显示


window = Tk()
window.title("Mile to KM Converter")
window.minsize(100, 80)
window.config(padx=50, pady=40)

# entry setting
mile_input = Entry(width=7)
mile_input.grid(column=2, row=1)
mile_input.focus()
mile_input.insert(END, "0")


# label setting
equality_label = Label(text="is equal to")
equality_label.grid(column=1, row=2)

KM_label = Label(text="KM")
KM_label.grid(column=3, row=2)

output_label = Label(text="0")
output_label.grid(column=2, row=2)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=1)

# button setting
cal_button = Button(text="Calculate", command=button_clicked)
cal_button.grid(column=2, row=3)


window.mainloop()