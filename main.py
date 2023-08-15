import tkinter
import tkinter as tk
import tkintermapview
from PIL import Image, ImageTk
from customtkinter import *
import sqlite3
from geopy.geocoders import Nominatim

def charger_render(map):
    notwork_icon = ImageTk.PhotoImage(Image.open("asets\\NotWork.png").resize((40, 40)))
    wait_icon = ImageTk.PhotoImage(Image.open("asets\\Wait.png").resize((40, 40)))
    free_icon = ImageTk.PhotoImage(Image.open("asets\\Free.png").resize((40, 40)))
    status = {'wait': wait_icon, 'notwork': notwork_icon, 'free': free_icon}
    con = sqlite3.connect("chargers.db")
    cur = con.cursor()
    chargers = list(cur.execute("SELECT * FROM charger_list"))
    for charge in chargers:
        map.set_marker(float(charge[1]), float(charge[2]), text=f"{charge[4]} р.", icon=status[charge[0]])

class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radiobutton_frame = None
        self.geometry(f"{450}x{750}")
        self.title("Заправки")
        self.reg_page()
        self.geolocator = Nominatim(user_agent="Rosseti")

    def settings(self):
        pass

    def reg_page(self):
        if list(sqlite3.connect("chargers.db").cursor().execute("SELECT * FROM settings")):
            self.start_page()
            return 0
        main_frame = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row=0, column=0, padx=100, pady=100)

        # Username label and entry box
        user_label = CTkLabel(master=main_frame,
                              text="Имя пользователя:")
        user_label.grid(row=1, column=0, sticky="w", pady=(0, 10))
        user_entry = CTkEntry(master=main_frame)
        user_entry.grid(row=1, column=1, pady=(0, 10), padx=10)

        # Password label and entry box

        pass_label = CTkLabel(master=main_frame, text="Пароль:")
        pass_label.grid(row=2, column=0, sticky="w", pady=(0, 10))
        pass_entry = CTkEntry(master=main_frame, show="*")
        pass_entry.grid(row=2, column=1, pady=(0, 10), padx=10)

        # Remember Me check button
        remember_me = CTkCheckBox(master=main_frame, text="Запомнить меня")
        remember_me.grid(row=4, column=1, pady=(0, 10))
        car_label = CTkLabel(master=main_frame,
                              text="Модель машины:")
        car_label.grid(row=3, column=0, sticky="w", pady=(0, 10))
        car_entry = CTkEntry(master=main_frame)
        car_entry.grid(row=3, column=1, pady=(0, 10), padx=10)
        # Login button
        login_button = CTkButton(master=main_frame, text="Войти", command=lambda: [main_frame.destroy(), self.start_page()])
        login_button.grid(row=5, column=1, pady=(0, 10), sticky="e", )

    def start_page(self):
        if not list(sqlite3.connect("chargers.db").cursor().execute("SELECT * FROM settings")):
            sqlite3.connect("chargers.db").cursor().execute("INSERT INTO settings VALUES(1);")

        def charger_render(map):
            def marker_callback(marker):
                map.set_position(marker.position[0], marker.position[1])
                map.set_zoom(20)
                con = sqlite3.connect("chargers.db")
                cur = con.cursor()
                charger = list(cur.execute(f"SELECT * FROM charger_list WHERE posx={marker.position[0]} AND posy={marker.position[1]}"))[0]
                colum = 0
                for i in self.radiobutton_frame.winfo_children():
                    try:
                        i.destroy()
                    except:
                        print(1)
                        continue
                location = str(self.geolocator.reverse(f"{marker.position[0]},{marker.position[1]}")).split(", ")
                print(location)
                name = CTkLabel(master=self.radiobutton_frame,
                                             text="Зарядная станция")
                name.place(x=160, y=5)
                loc = "Локация: " + ", ".join(location[:3])
                if len(loc) >= 60:
                    loc = loc[:60] + "..."
                locate = CTkLabel(master=self.radiobutton_frame,
                                                  text=loc)
                locate.place(x=10, y=30)
                label_radio_group = CTkLabel(master=self.radiobutton_frame,
                                                                text="Доступные разьемы и мощности:")
                label_radio_group.place(x=10, y=60)
                chargers = [10, 90]
                if charger[5] == 'yes':
                    charger1 = CTkButton(self.radiobutton_frame, width=90, height=90, text='Charge 1\n40 Вт')
                    charger1.place(x=chargers[0], y=chargers[1])
                    chargers[0] += 110
                    colum += 1
                if charger[6] == 'yes':
                    charger2 = CTkButton(master=self.radiobutton_frame, width=90, height=90, text='Charge 2')
                    charger2.place(x=chargers[0], y=chargers[1])
                    chargers[0] += 110
                if charger[7] == 'yes':
                    charger3 = CTkButton(self.radiobutton_frame, width=90, height=90, text='Charge 3')
                    charger3.place(x=chargers[0], y=chargers[1])
                    chargers[0] += 110
                if charger[8] == 'yes':
                    charger4 = CTkButton(master=self.radiobutton_frame, width=90, height=90, text='Charge 4')
                    charger4.place(x=chargers[0], y=chargers[1])
                    chargers[0] += 110
                if charger[9] == 'yes':
                    charger5 = CTkButton(self.radiobutton_frame, width=90, height=90, text='Charge 5')
                    charger5.place(x=chargers[0], y=chargers[1])
                    chargers[0] += 110
                if charger[10] == 'yes':
                    charger6 = CTkButton(master=self.radiobutton_frame, width=90, height=90, text='Charge 6')
                    charger6.place(x=chargers[0], y=chargers[1])


            notwork_icon = ImageTk.PhotoImage(Image.open("asets\\NotWork.png").resize((40, 40)))
            wait_icon = ImageTk.PhotoImage(Image.open("asets\\Wait.png").resize((40, 40)))
            free_icon = ImageTk.PhotoImage(Image.open("asets\\Free.png").resize((40, 40)))
            status = {'wait': wait_icon, 'notwork': notwork_icon, 'free': free_icon}
            con = sqlite3.connect("chargers.db")
            cur = con.cursor()
            chargers = list(cur.execute("SELECT * FROM charger_list"))
            for charge in chargers:
                map.set_marker(float(charge[1]), float(charge[2]), text=f"{charge[4]} р.", icon=status[charge[0]], command=marker_callback)

        set = CTkImage(Image.open("asets\\settings.png").resize((60, 60)))
        map_widget = tkintermapview.TkinterMapView(self, width=552, height=400, corner_radius=25)
        map_widget.place(x=5, y=5)
        map_widget.set_zoom(15)
        map_widget.set_position(44.256659, 38.819511)
        self.radiobutton_frame = CTkFrame(self, width=440, height=360)
        self.radiobutton_frame.place(x=5, y=330)
        self.radiobutton_frame.grid_propagate(False)
        #self.label_radio_group = CTkLabel(master=self.radiobutton_frame,
                  #                        text="Доступные разьемы и мощности:")
        #self.label_radio_group.place(x=10, y=10)
        charger_render(map_widget)
        set_button = CTkButton(self, width=40, height=40, text='', image=set, command=self.settings())
        set_button.place(x=400, y=700)

        charger1 = CTkButton(self, width=80, height=80, text='Charge 1', image=set)
        charger2 = CTkButton(master=self, width=80, height=80, text='Charge 2', image=set)




app = App()
app.mainloop()
