from tkinter import messagebox
from tk_root import root
def on_closing():
    if messagebox.askokcancel("Quit", "Вы действительно хотите выйти?"):
        root.quit()
