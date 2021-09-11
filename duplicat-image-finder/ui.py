import tkinter as tk
from tkinter import filedialog


# image_name = "004.jpg"
# base_folder = path.realpath(path.dirname(__file__))
# img_folder = path.join(base_folder, 'imgs')
# img_path = path.join(img_folder, image_name)
# print(base_folder)
# print(img_folder)
# print(img_path)
# tkinter
# # Get image
# im = resize_image(img_path)
# found_similars(im, img_folder)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Label 'Path'
        self.lbl_path = tk.Label(self, text="")
        self.lbl_path.pack(side="top")

        # Button 'open'
        self.btn_open = tk.Button(self)
        self.btn_open["text"] = "Select folder"
        self.btn_open["command"] = self.get_directory
        self.btn_open.pack(side="bottom")

        # Button 'quit'
        # self.btn_quit = tk.Button(
        #     self,
        #     text="QUIT",
        #     fg="red",
        #     command=self.master.destroy
        # )
        # self.btn_quit.pack(side="bottom")

    def get_directory(self):
        folder_selected = filedialog.askdirectory()
        self.lbl_path['text'] = folder_selected
