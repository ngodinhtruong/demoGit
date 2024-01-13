from tkinter import *
import tkinter as tk
from main import *

windowTK = tk.Tk()
def center_window(width,height,window,x_pos,y_pos):
    x_screen = window.winfo_screenwidth()
    y_screen = window.winfo_screenheight()
    x_mid_screen = (x_screen - width) // x_pos
    y_mid_screen = (y_screen - height) // y_pos
    return x_mid_screen,y_mid_screen

def window_caution(s):
    # Check if the label already exists
    if hasattr(window_caution, 'caution_label'):
        # Update the text of the existing label
        window_caution.caution_label.config(text=f"{s}")
    else:
        # Create a new label
        window_caution.caution_label = tk.Label(windowTK, text=f"{s}", font=("Consolas", 10, 'bold'), fg='red')
        window_caution.caution_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


def center_window_main(width, height, window):
    global cookie_value
    x,y = center_window(width,height,window,2,4)

    window.geometry(f'{width}x{height}+{x}+{y}')
    cookieLabel = Label(window, text="INPUT COOKIE: ", fg='black', font=("Consolas", 10, "bold"))
    cookieLabel.place(x=10, y=10)

    cookie_value = StringVar()
    EnCookie = Entry(window, textvariable=cookie_value, font=("Consolas", 10), borderwidth=3, width=15)
    EnCookie.place(x=cookieLabel.winfo_reqwidth() + 10, y=10)


    options = Button(window,text = 'Options',font=("consolas",8,'bold'), command=window_options)
    options.place(relx=0.02,rely=0.41)
    submit_button_clicked_with_param = lambda: submit_button_clicked(cookie_value)
    submitButton = Button(window, text="Submit", fg='white', bg="#01a133", command=submit_button_clicked_with_param,
                          font=("Consolas", 12, "bold"))
    submitButton.place(x=110, y=45)


    devBy = Label(window,text='Dev by: NT_Dinh',font=('calibri',7,'italic'))
    devBy.place(x=300-devBy.winfo_reqwidth(),y=130-devBy.winfo_reqheight())

    window.mainloop()

def window_options():
    window_op = tk.Tk()
    window_op.title(string="Option")
    x,y = center_window(250,100, window_op, 2, 3)
    window_op.geometry(f"{300}x{200}+{x}+{y}")

    choice = ['A. Hoàn toàn không đồng ý', 'B. Không đồng ý', 'C. Phân vân', 'D. Đồng ý', 'E. Hoàn toàn đồng ý']
    choice_value = StringVar(window_op)
    choice_value.set(choice[-2])
    options_choice = OptionMenu(window_op, choice_value, *choice)
    options_choice.pack()

    label_idead = Label(window_op,text="Ý kiến của bạn:",fg='red',font=('calibri',10,'bold'))
    label_idead.place(relx=0.077,rely=0.23)
    text = Text(window_op,height=4,width=25)
    text.insert(END, "Welcome to IUH")
    text.place(relx=0.08,rely=0.35)
    submit_done = Button(window_op, text='Done', command= lambda: [
                                            options_button_clicked(text.get("1.0", END), choice_value.get()),
                                            window_op.destroy()])
    submit_done.place(relx=0.4,rely=0.77)
    window_op.mainloop()
def thongbao():
    print("thongbao")
def start():
    windowTK.title(string="Skip survey of IUH")
    center_window_main(300, 130, windowTK)
