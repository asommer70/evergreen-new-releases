import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sys


# http://colorhunt.co/c/107892
red = '#970747'
white = '#FEF4E8'
blue = '#1989AC'
dark_blue = '#283E56'

banner_font = ('Carter One', 24)
body_font = ('Kingsland', 16)
DEFAULT_GAP = 60 * 25
DEFAULT_GAP = 5


class NewReleases:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.timer_text = tkinter.StringVar()
        self.timer_text.trace('w', self.build_timer)
        self.time_left = tkinter.IntVar()
        self.time_left.set(DEFAULT_GAP)
        self.time_left.trace('w', self.alert)
        self.running = False

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()
        self.build_menu()
        self.master.config(menu=self.menubar)

        self.update()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_menu(self):
        # create a toplevel menu
        self.menubar = tkinter.Menu(self.master, tearoff=0)
        # self.menubar.add_command(label="Hello!", command=hello)
        self.menubar.add_cascade(label="Quit!", command=self.master.quit)

    def build_banner(self):
        banner_frame = tkinter.Frame(self.mainframe)
        banner_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        banner_frame.columnconfigure(0, weight=1)
        banner_frame.columnconfigure(1, weight=1)

        icon = ImageTk.PhotoImage(Image.open("img/evergreen_new_releases_logo.png"))
        # icon = tkinter.PhotoImage(file="evergreen_new_releases_logo.png")
        banner = tkinter.Label(
            banner_frame,
            # bg=white,
            # fg=white,
            # # text='Evergreen New Releases',
            image=icon,
            font=banner_font
        )
        banner.grid(row=0, column=0, sticky='nsew')

        # options_icon = ImageTk.PhotoImage(Image.open("./img/options-icon.jpg"))
        # self.overflow_button = tkinter.Button(
        #     banner_frame,
        #     image=options_icon,
        #     font=body_font,
        # )
        # self.overflow_button.grid(row=0, column=1, sticky='ew')

    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.start_button = tkinter.Button(
            buttons_frame,
            text='Start',
            font=body_font,
            command=self.start_timer
        )
        self.stop_button = tkinter.Button(
            buttons_frame,
            text='Stop',
            font=body_font,
            command=self.stop_timer
        )
        self.stop_button.config(state=tkinter.DISABLED)

        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')

    def build_timer(self, *args):
        timer = tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(),
            font=body_font
        )
        timer.grid(row=1, column=0, sticky='nsew')

    def start_timer(self):
        self.time_left.set(DEFAULT_GAP)
        self.running = True
        self.stop_button.config(state=tkinter.NORMAL)
        self.start_button.config(state=tkinter.DISABLED)

    def stop_timer(self):
        self.running = False
        self.stop_button.config(state=tkinter.DISABLED)
        self.start_button.config(state=tkinter.NORMAL)

    def alert(self, *args):
        if not self.time_left.get():
            messagebox.showinfo('Timer done!', 'Your timer is done!')

    def minutes_seconds(self, seconds):
        return int(seconds/60), int(seconds%60)

    def update(self):
        time_left = self.time_left.get()

        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set('{:0>2}:{:0>2}'.format(minutes, seconds))
            self.time_left.set(time_left - 1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.timer_text.set('{:0>2}:{:0>2}'.format(minutes, seconds))
            self.stop_timer()

        self.master.after(1000, self.update)


if __name__ == '__main__':
    root = tkinter.Tk()
    icon = ImageTk.PhotoImage(Image.open("img/evergreen_new_releases_logo.gif"))
    # icon = Image.open("img/evergreen_new_releases_logo.png")
    # image=photo
    # root.tk.call('wm', 'iconbitmap', self._w, '-default', icon)
    root.geometry('800x600')
    root.title("Evergreen New Releases")
    # img = TK.PhotoImage(file=icon_path)
    # root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage("img/evergreen_new_releases_logo.png"))
    # root.iconbitmap('./img/evergreen_new_releases_logo.gif')
    # root.iconbitmap(icon)

    imgicon = tkinter.PhotoImage(file='./img/evergreen_new_releases_logo.gif')
    root.tk.call('wm', 'iconphoto', root._w, imgicon)
    # root.iconbitmap(imgicon)

    NewReleases(root)
    root.mainloop()
