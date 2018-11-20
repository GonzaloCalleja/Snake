
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

        self.size = 15
        self.blocks = list()
        self.blocks.append(t.Canvas(master, bg="blue", highlightthickness=0, width=self.size, height=self.size))
        self.blocks[0].grid(row=self.x, column=self.y)
        self.blocks[0].place(x=self.x, y=self.y)

        for i in range(15):
            self.blocks.append(t.Canvas(master, bg="blue", highlightthickness=0, width=self.size, height=self.size))
            self.blocks[i].place(x=self.x - self.size, y=self.y)

        self.temp1 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        self.temp2 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        self.temp3 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        self.temp4 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)

        self.blocks[0].focus_set()
        self.blocks[0].bind("<KeyPress>", self.key_press)
        #self.blocks[0].bind("<KeyRelease>", self.key_release)

        self.move()

    def move(self):

        self.x += self.velx
        self.y += self.vely

        if self.vely or self.velx:

            self.blocks[0].place(x=self.x, y=self.y)

            self.blocks = self.blocks[len(self.blocks)-1:len(self.blocks)] + self.blocks[0:len(self.blocks)-1]



        if self.x + self.size > self.total_width:
            self.temp1.place(x=self.x - self.total_width, y=self.y)
            if self.x > self.total_width:
                self.temp1.destroy()
                self.temp1 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.x = 0
                self.c.place(x=self.x, y=self.y)

        if self.x < 0:
            self.temp2.place(x=self.x + self.total_width, y=self.y)
            if self.x + self.size < 0:
                self.temp2.destroy()
                self.temp2 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.x = self.total_width - self.size
                self.c.place(x=self.x, y=self.y)

        if self.y + self.size > self.total_height:
            self.temp3.place(x=self.x, y=self.y - self.total_height)
            if self.y > self.total_height:
                self.temp3.destroy()
                self.temp3 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.y = 0
                self.c.place(x=self.x, y=self.y)

        if self.y < 0:
            self.temp4.place(x=self.x, y=self.y + self.total_height)
            if self.y + self.size < 0:
                self.temp4.destroy()
                self.temp4 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
                self.y = self.total_height - self.size
                self.c.place(x=self.x, y=self.y)

        tk.after(100, self.move)

    def key_press(self, event):

        pr = event.keysym
        change = 15

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

    def key_release(self, event):
        self.velx = 0
        self.vely = 0


if __name__ == "__main__":

    tk = t.Tk()

    screen = 500
    tk.geometry(str(screen) + "x" + str(screen))

    f = t.Frame(tk, bg="grey", width=screen, height=screen)
    f.pack(fill=t.BOTH, expand=1)

    snake = SnakeBlock(f)

    tk.mainloop()
