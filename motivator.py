import tkinter
from tkinter import ttk
from playsound import playsound
from PIL import ImageTk


def play_sound(victory):
    if victory:
        playsound("victory.mp3")

    else:
        playsound("sadtrombone.mp3")


class App:
    def __init__(self, root, window_title):
        self.root = root
        self.root.title(window_title)

        self.button_one = ttk.Button(self.root, text="I have thing to do", command=self.do_the_thing)
        self.button_two = ttk.Button(self.root, text="I have not yet done the thing",
                                     command=self.fail)
        self.status = ttk.Label(self.root)
        self.image = ttk.Label(self.root)

        for item in (self.status, self.image, self.button_one):
            item.pack()

        self.root.mainloop()

    def fail(self):
        play_sound(False)

    def do_the_thing(self):
        img = ImageTk.PhotoImage(file="dothething.gif")
        self.image.configure(image=img)

        self.status.configure(text="")

        self.button_two.pack()

        self.button_one.configure(text="I did the thing", command=self.did_the_thing)

    def did_the_thing(self):
        img = ImageTk.PhotoImage(file="reward.gif")
        self.image.configure(image=img)

        self.button_two.forget()

        self.status.configure(text="Good job! Reward yourself!")
        play_sound(True)
        self.button_one.configure(text="I have another thing to do", command=self.do_the_thing)


if __name__ == '__main__':
    App(tkinter.Tk(), "Motivator")
