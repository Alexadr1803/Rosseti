import tkinter as tk
import tkintermapview
from PIL import Image, ImageTk
from customtkinter import *
import sqlite3

def charger_render(map):
    notwork_icon = ImageTk.PhotoImage(Image.open("asets\\NotWork.png").resize((40, 40)))
    wait_icon = ImageTk.PhotoImage(Image.open("asets\\Wait.png").resize((40, 40)))
    free_icon = ImageTk.PhotoImage(Image.open("asets\\Free.png").resize((40, 40)))
    status = {'wait': wait_icon, 'notwork': notwork_icon, 'free': free_icon}
    con = sqlite3.connect("chargers.db")
    cur = con.cursor()
    chargers = list(cur.execute("SELECT * FROM charger_list"))
    for charge in chargers:
        map.set_marker(float(charge[1]), float(charge[2]), text="45 руб", icon=status[charge[0]])

def get_info():
    pass
# create map widget
def map_create(page):
    map_widget = tkintermapview.TkinterMapView(page, width=300, height=300, corner_radius=10)
    map_widget.place(relx=0.38, rely=0.25, anchor=tk.CENTER)
    map_widget.set_zoom(15)
    map_widget.set_position(44.256659, 38.819511)
    charger_render(map_widget)
class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"{450}x{750}")
        self.title("Заправки")
        self.reg_page()
    def reg_page(self):
        main_frame = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row=0, column=0, padx=10, pady=10)

        # Login Window title
        title = CTkLabel(master=main_frame, text="Login Window")
        title.grid(row=0, column=0, pady=(0, 20))

        # Username label and entry box
        user_label = CTkLabel(master=main_frame,
                                            text="Username:")
        user_label.grid(row=1, column=0, sticky="w", pady=(0, 10))
        user_entry = CTkEntry(master=main_frame)
        user_entry.grid(row=1, column=1, pady=(0, 10), padx=10)

        # Password label and entry box
        pass_label = CTkLabel(master=main_frame, text="Password:")
        pass_label.grid(row=2, column=0, sticky="w", pady=(0, 10))
        pass_entry = CTkEntry(master=main_frame, show="*")
        pass_entry.grid(row=2, column=1, pady=(0, 10), padx=10)

        # Remember Me check button
        remember_me = CTkCheckBox(master=main_frame, text="Remember Me")
        remember_me.grid(row=3, column=1, pady=(0, 10))
        # Login button
        login_button = CTkButton(master=main_frame, text="Login",
                                 command=lambda:[main_frame.destroy(), self.start_page()])
        login_button.grid(row=4, column=1, pady=(0, 20), sticky="e")
    def start_page(self):
        map_create(self)

app = App()
app.mainloop()