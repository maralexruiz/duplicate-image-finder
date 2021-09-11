
import tkinter as tk
from ui import Application

# Example gpg more
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')
    app = Application(master=root)
    app.mainloop()
