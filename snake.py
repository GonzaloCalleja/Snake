
import tkinter as t
import time


class SnakeBlock(object):

    def __init__(self, master):

        self.velx = 0
        self.vely = 0
        self.x = 100
        self.y = 100

        self.master = master
        self.total_height = self.master.winfo_reqheight()
        self.total_width = self.master.winfo_reqwidth()

        self.size = 10

        self.turn_right = False
        self.turn_left = False
        self.turn_up = False
        self.turn_down = False
        self.blocks = list()
        self.blocks.append(t.Canvas(master, bg="blue", highlightthickness=0, width=self.size, height=self.size))
        self.blocks[0].place(x=self.x, y=self.y)

        # colors = ["","red", "blue", "yellow", "green"]

        for i in range(1, 15):
            self.blocks.append(t.Canvas(master, bg="blue", highlightthickness=0, width=self.size, height=self.size))
            self.blocks[i].place(x=self.x, y=self.y)

        # self.temp = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        # self.temp2 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        # self.temp3 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        # self.temp4 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)

        self.blocks[0].focus_set()
        self.blocks[0].bind("<KeyPress>", self.key_press)
        # self.blocks[0].bind("<KeyRelease>", self.key_release)

        self.frame = 0

        self.move()

    def move(self):

        #if self.vely or self.velx:
        if True:

            if self.turn_right and self.y % self.size == 0:
                self.velx = self.change
                self.vely = 0
                self.turn_right = False
            if self.turn_left and self.y % self.size == 0:
                self.velx = -self.change
                self.vely = 0
                self.turn_left = False
            if self.turn_down and self.x % self.size == 0:
                self.velx = 0
                self.vely = self.change
                self.turn_down = False
            if self.turn_up and self.x % self.size == 0:
                self.velx = 0
                self.vely = -self.change
                self.turn_up = False

            if self.x % self.size == 0 and self.y % self.size == 0:

                self.blocks = self.blocks[len(self.blocks)-1:len(self.blocks)] + self.blocks[0:len(self.blocks)-1]

            self.x += self.velx
            self.y += self.vely

            self.blocks[0].place(x=self.x, y=self.y)

            temp_x = self.blocks[-1].winfo_x()
            temp_y = self.blocks[-1].winfo_y()

            if temp_x < self.blocks[-2].winfo_x():
                self.blocks[-1].place(x=temp_x + 1, y=temp_y)
            elif temp_x > self.blocks[-2].winfo_x():
                self.blocks[-1].place(x=temp_x - 1, y=temp_y)

            if temp_y < self.blocks[-2].winfo_y():
                self.blocks[-1].place(x=temp_x, y=temp_y+1)
            elif temp_y > self.blocks[-2].winfo_y():
                self.blocks[-1].place(x=temp_x, y=temp_y-1)

        # if self.x + self.size > self.total_width:
        #     self.temp1.place(x=self.x - self.total_width, y=self.y)
        #     if self.x > self.total_width:
        #         self.temp1.destroy()
        #         self.temp1 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        #         self.x = 0
        #         self.blocks[0].place(x=self.x, y=self.y)
        #
        # if self.x < 0:
        #     self.temp2.place(x=self.x + self.total_width, y=self.y)
        #     if self.x + self.size < 0:
        #         self.temp2.destroy()
        #         self.temp2 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        #         self.x = self.total_width - self.size
        #         self.blocks[0].place(x=self.x, y=self.y)
        #
        # if self.y + self.size > self.total_height:
        #     self.temp3.place(x=self.x, y=self.y - self.total_height)
        #     if self.y > self.total_height:
        #         self.temp3.destroy()
        #         self.temp3 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        #         self.y = 0
        #         self.blocks[0].place(x=self.x, y=self.y)
        #
        # if self.y < 0:
        #     self.temp4.place(x=self.x, y=self.y + self.total_height)
        #     if self.y + self.size < 0:
        #         self.temp4.destroy()
        #         self.temp4 = t.Canvas(self.master, bg="blue", highlightthickness=0, width=self.size, height=self.size)
        #         self.y = self.total_height - self.size
        #         self.blocks[0].place(x=self.x, y=self.y)

        self.frame += 1
        tk.after(10, self.move)

    def key_press(self, event):

        pr = event.keysym
        self.change = 1

        if pr == "Left":
            # self.velx = -self.change
            # self.vely = 0
            self.turn_left = True
        elif pr == "Right":
            # if self.blocks[0].winfo_y() % self.rows==0:
            #     self.velx = change
            #     self.vely = 0
            self.turn_right = True
        elif pr == "Down":
            # self.velx = 0
            # self.vely = self.change
            self.turn_down = True
        elif pr == "Up":
            # self.velx = 0
            # self.vely = -self.change
            self.turn_up = True

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
