from tkinter import *
from tkinter import ttk
import random as rd
import sys
import time

class App(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.geometry('1250x800')
        self.resizable(False, False)
        self.title('AIM training')

        self.space_image = PhotoImage(file='backgrounds\\space.gif')
        self.magic_image = PhotoImage(file='backgrounds\\magic.gif')
        self.land_image = PhotoImage(file='backgrounds\\land.gif')
        self.black_image = PhotoImage(file='backgrounds\\black_bg.gif')
        self.colors_image = PhotoImage(file='backgrounds\\colors.gif')
        self.lightnings_image = PhotoImage(file='backgrounds\\lightnings.gif')
        self.mountains_image = PhotoImage(file='backgrounds\\mountains.gif')
        self.cubes_image = PhotoImage(file='backgrounds\\cubes.gif')
        self.hexagons_image = PhotoImage(file='backgrounds\\hexagons.gif')

        self.title_image = PhotoImage(file='title.png')

        self.button_play_image = PhotoImage(file='buttons\\play_button.gif')
        self.button_settings_image = PhotoImage(file='buttons\\settings_button.gif')
        self.button_resume_image = PhotoImage(file='buttons\\resume_image.png')
        self.button_exit_image = PhotoImage(file='buttons\\exit_button.gif')
        self.button_goback_image = PhotoImage(file='buttons\\goback_button.gif')
        self.button_start_image = PhotoImage(file='buttons\\start_button.gif')
        self.button_catch_image = PhotoImage(file='buttons\\catch_button.gif')

        self._3_image = PhotoImage(file='nums\\3....png')
        self._2_image = PhotoImage(file='nums\\2....png')
        self._1_image = PhotoImage(file='nums\\1....png')

        self.list_coords = (
        0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95
        )

        self.list_of_backgrounds = (
            self.space_image, self.magic_image, self.land_image, self.black_image,
            self.colors_image, self.lightnings_image, self.mountains_image,
            self.cubes_image, self.hexagons_image
        )
        self.current_image = rd.choice(self.list_of_backgrounds)

        self.current_background_id = 0

        self.set_background_id()

        self.current_score = 0
        self.current_seconds = 0
        self.current_minutes = 0
        self.check_timer_count = 0

        self.make_menu_window()

    def set_background_id(self):

        if self.current_image == self.space_image:
            self.current_background_id = 0
        elif self.current_image == self.magic_image:
            self.current_background_id = 1
        elif self.current_image == self.land_image:
            self.current_background_id = 2
        elif self.current_image == self.black_image:
            self.current_background_id = 3
        elif self.current_image == self.colors_image:
            self.current_background_id = 4
        elif self.current_image == self.lightnings_image:
            self.current_background_id = 5
        elif self.current_image == self.mountains_image:
            self.current_background_id = 6
        elif self.current_image == self.cubes_image:
            self.current_background_id = 7
        elif self.current_image == self.hexagons_image:
            self.current_background_id = 8

    def make_menu_window(self):

        self.destroy_window()

        self.canvas = Canvas(self, width=1250, height=800, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.current_image, anchor=NW)
        self.canvas.pack()

        self.canvas.create_image(210, 50, image=self.title_image, anchor=NW)

        self.button_play = Button(self.canvas, bg='blue', image=self.button_play_image, command=self.button_play_click)
        self.button_play.place(rely=0.6, relx=0.2, anchor=CENTER)

        self.button_settings = Button(self.canvas, bg='orange', image=self.button_settings_image, command=self.button_settings_click)
        self.button_settings.place(anchor=CENTER, rely=0.6, relx=0.5)

        self.button_exit = Button(self.canvas, bg='gray', image=self.button_exit_image, command=self.button_exit_click)
        self.button_exit.place(anchor=CENTER, rely=0.6, relx=0.8)

    def make_game_window(self):

        self.canvas1 = Canvas(self, width=1250, height=800, highlightthickness=0)
        self.canvas1.create_image(0, 0, image=self.current_image, anchor=NW)
        self.canvas1.pack()

        self.goback_button = Button(self.canvas1, image=self.button_goback_image, bg='black', command=self.goback_button_clicked)
        self.goback_button.place(relx=0, rely=0, anchor=NW)

        self.start_button = Button(self.canvas1, image=self.button_start_image, bg='lime', command=self.start_game)
        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def start_game(self):

        self.destroy_window()
        self.canvas2 = Canvas(self, width=1250, height=800, highlightthickness=0)
        self.canvas2.create_image(0, 0, image=self.current_image, anchor=NW)
        self.canvas2.pack()

        self.canvas2.create_image(500, 350, image=self._3_image, anchor=NW)
        self.update()
        time.sleep(1)

        self.canvas2.create_image(500, 420, image=self._2_image, anchor=NW)
        self.update()
        time.sleep(1)

        self.canvas2.create_image(500, 500, image=self._1_image, anchor=NW)
        self.update()
        time.sleep(1)

        self.destroy_window()
        self.canvas2 = Canvas(self, width=1250, height=800, highlightthickness=0)
        self.canvas2.create_image(0, 0, image=self.current_image, anchor=NW)
        self.canvas2.pack()

        # ______________________________________________________________________________________________________________

        self.current_score = 0
        self.label_score = Label(self.canvas2, text=f'Score: {self.current_score}', font=70, bg='black', fg='white')
        self.label_score.place(relx=0, rely=0, anchor=NW)

        self.label_time = Label(self.canvas2, text=f'Time: {self.current_seconds}', font=70, bg='black', fg='white')
        self.label_time.place(relx=1, rely=0, anchor=NE)

        self.list_nums = (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95)
        self.catch_button = Button(self.canvas2, bg='white', image=self.button_catch_image, command=self.catch_button_click)
        self.catch_button.place(relx=rd.choice(self.list_coords), rely=rd.choice(self.list_coords), anchor=CENTER)

        self.pause_button = Button(self.canvas2, text='pause', fg='white', font='70', bg='black',
                                  command=self.pause_button_clicked)
        self.pause_button.place(relx=0, rely=1, anchor=SW)

    def resume_game(self):

        self.destroy_window()

        self.canvas2 = Canvas(self, width=1250, height=800, highlightthickness=0)
        self.canvas2.create_image(0, 0, image=self.current_image, anchor=NW)
        self.canvas2.pack()

        self.label_score = Label(self.canvas2, text=f'Score: {self.current_score}', font=70, bg='black', fg='white')
        self.label_score.place(relx=0, rely=0, anchor=NW)

        self.label_time = Label(self.canvas2, text=f'Time: {self.current_seconds}', font=70, bg='black', fg='white')
        self.label_time.place(relx=1, rely=0, anchor=NE)

        self.list_nums = (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95)
        self.catch_button = Button(self.canvas2, bg='white', image=self.button_catch_image, command=self.catch_button_click)
        self.catch_button.place(relx=rd.choice(self.list_coords), rely=rd.choice(self.list_coords), anchor=CENTER)

        self.pause_button = Button(self.canvas2, text='pause', fg='white', font='70', bg='black', command=self.pause_button_clicked)
        self.pause_button.place(relx=0, rely=1, anchor=SW)

    def pause_button_clicked(self):

        self.destroy_window()
        self.canvas2 = Canvas(self, width=1250, height=800, highlightthickness=0)
        self.canvas2.create_image(0, 0, image=self.current_image, anchor=NW)
        self.canvas2.pack()

        self.resume_button = Button(self.canvas2, image=self.button_resume_image, bg='black', command=self.resume_game)
        self.resume_button.place(relx=0, rely=0, anchor=NW)

        self.menu_button = Button(self.canvas2, text='go to menu', fg='white', font='70', activebackground='red', bg='black', command=self.make_menu_window)
        self.menu_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.choose_background = ttk.Combobox(self.canvas2, values=['space', 'magic', 'land', 'black', 'colorful',
                                                                    'thunder', 'mountains', 'cubes', 'hexagons'])
        self.choose_background.current(self.current_background_id)
        self.choose_background.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.choose_background.bind('<<ComboboxSelected>>', self.choise_combobox)



    def catch_button_click(self):

        self.colors = ('red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'pink', 'magenta', 'purple')
        self.catch_button['bg'] = rd.choice(self.colors)
        self.catch_button.place(relx=rd.choice(self.list_coords), rely=rd.choice(self.list_coords), anchor=CENTER)
        self.current_score += 1
        self.label_score['text'] = f'Score: {self.current_score}'

    def button_settings_click(self):

        self.destroy_window()
        self.canvas2 = Canvas(self, width=1250, height=800, highlightthickness=0)
        self.canvas2.create_image(0, 0, image=self.current_image, anchor=NW)
        self.canvas2.pack()

        self.goback_button2 = Button(self.canvas2, image=self.button_goback_image, bg='black', command=self.goback_button_clicked)
        self.goback_button2.place(relx=0, rely=0, anchor=NW)

        self.check_timer = Checkbutton(self.canvas2, text='timer', font=40, command=self.check_timer_click)
        self.check_timer.place(rely=0.5, relx=0.5, anchor=CENTER)

        self.check_score = Checkbutton(self.canvas2, text='score counter', font=40, command=self.check_score_click)
        self.check_score.place(rely=0.5, relx=0.59, anchor=CENTER)


        self.choose_background = ttk.Combobox(self.canvas2, values=['space', 'magic', 'land', 'black', 'colorful',
                                                                    'thunder', 'mountains', 'cubes', 'hexagons'])
        self.choose_background.current(self.current_background_id)
        self.choose_background.place(relx=0.4, rely=0.5, anchor=CENTER)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.choose_background.bind('<<ComboboxSelected>>', self.choise_combobox)


    def choise_combobox(self, event):

        if self.choose_background.current() == 1:
            self.canvas2.create_image(0, 0, image=self.magic_image, anchor=NW)
            self.current_image = self.magic_image
            self.current_background_id = 1

        elif self.choose_background.current() == 2:
            self.canvas2.create_image(0, 0, image=self.land_image, anchor=NW)
            self.current_image = self.land_image
            self.current_background_id = 2

        elif self.choose_background.current() == 3:
            self.canvas2.create_image(0, 0, image=self.black_image, anchor=NW)
            self.current_image = self.black_image
            self.current_background_id = 3

        elif self.choose_background.current() == 4:
            self.canvas2.create_image(0, 0, image=self.colors_image, anchor=NW)
            self.current_image = self.colors_image
            self.current_background_id = 4

        elif self.choose_background.current() == 5:
            self.canvas2.create_image(0, 0, image=self.lightnings_image, anchor=NW)
            self.current_image = self.lightnings_image
            self.current_background_id = 5

        elif self.choose_background.current() == 6:
            self.canvas2.create_image(0, 0, image=self.mountains_image, anchor=NW)
            self.current_image = self.mountains_image
            self.current_background_id = 6

        elif self.choose_background.current() == 7:
            self.canvas2.create_image(0, 0, image=self.cubes_image, anchor=NW)
            self.current_image = self.cubes_image
            self.current_background_id = 7

        elif self.choose_background.current() == 8:
            self.canvas2.create_image(0, 0, image=self.hexagons_image, anchor=NW)
            self.current_image = self.hexagons_image
            self.current_background_id = 8

        elif self.choose_background.current() == 0:
            self.canvas2.create_image(0, 0, image=self.space_image, anchor=NW)
            self.current_image = self.space_image
            self.current_background_id = 0




    def enter_mouse(self, event):
        pass

    def check_timer_click(self):

        self.check_timer_count += 1
        if self.check_timer_count % 2 != 0:
            pass
        elif self.check_timer_count % 2 == 0:
            pass

    def check_score_click(self):
        pass

    def destroy_window(self):
        for i in self.winfo_children(): i.destroy()

    def goback_button_clicked(self):
        self.make_menu_window()

    def button_exit_click(self):
        self.destroy_window()
        sys.exit()

    def button_play_click(self):
        self.destroy_window()
        self.make_game_window()

    def timer_start(self):
        while True:
            if self.seconds > 59:
                self.current_minutes += 1
                self.seconds = 0
            self.seconds += 1
            self.label_time['text'] = f'Time: {self.current_minutes}:{self.current_seconds}.'
            self.update()
            time.sleep(1)

if __name__=='__main__': App().mainloop()