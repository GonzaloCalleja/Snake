
import tkinter as t


class SnakeBlock(object):

    def __init__(self, master):

        self.velx = 0
        self.vely = 0
        self.x = 50
        self.y = 50

        self.master = master
        self.total_height = self.master.winfo_reqheight()
        self.total_width = self.master.winfo_reqwidth()

        self.size = 100
        self.c = t.Canvas(master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        self.c.grid(row=self.x, column=self.y)
        self.c.place(x=self.x, y=self.y)

        self.temp = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)

        self.c.focus_set()
        self.c.bind("<KeyPress>", self.key_press)

        self.move()

    def move(self):

        self.x += self.velx
        self.y += self.vely

        self.c.place(x=self.x, y=self.y)

        if self.x + self.size > self.total_width:
            self.temp.place(x=self.x - self.total_width, y=self.y)
            if self.x > self.total_width:
                self.temp.destroy()
                self.temp = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.x = 0
                self.c.place(x=self.x, y=self.y)

        if self.x < 0:
            self.temp.place(x=self.x + self.total_width, y=self.y)
            if self.x + self.size < 0:
                self.temp.destroy()
                self.temp = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.x = self.total_width - self.size
                self.c.place(x=self.x, y=self.y)

        if self.y + self.size > self.total_height:
            self.temp.place(x=self.x, y=self.y - self.total_height)
            if self.y > self.total_height:
                self.temp.destroy()
                self.temp = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.y = 0
                self.c.place(x=self.x, y=self.y)

        if self.y < 0:
            self.temp.place(x=self.x, y=self.y + self.total_height)
            if self.y + self.size < 0:
                self.temp.destroy()
                self.temp = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.y = self.total_height - self.size
                self.c.place(x=self.x, y=self.y)


        tk.after(10, self.move)

    def key_press(self, event):

        pr = event.keysym
        change = 1

        if pr == "Left":
            self.velx = -change
            self.vely = 0
        elif pr == "Right":
            self.velx = change
            self.vely = 0
        elif pr == "Down":
            self.velx = 0
            self.vely = change
        elif pr == "Up":
            self.velx = 0
            self.vely = -change


if __name__ == "__main__":

    tk = t.Tk()

    screen = 500
    tk.geometry(str(screen) + "x" + str(screen))

    f = t.Frame(tk, bg="grey", width=screen, height=screen)
    f.pack(fill=t.BOTH, expand=1)

    snake = SnakeBlock(f)

    tk.mainloop()
