from tkinter import Tk
from screens import render_main_screen

if __name__ == '__main__':
    tk = Tk()
    tk.geometry('600x600')
    tk.title('My GUI Product Shop')
    render_main_screen(tk)
    tk.mainloop()
