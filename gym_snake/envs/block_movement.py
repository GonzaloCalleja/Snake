
import tkinter as t

class block(object):

    def __init__(self, previous_x, previous_y):

        self.previous_x = previous_x
        self.previous_y = previous_y

        self.new_coords()

    def new_coords(self):




tk = t.Tk()

blocks = []

x = 100
y = 100
size = 10

c = t.Canvas(tk, bg="#000000", width=480, height=360)
c.pack()


for i in range(3):
    blocks.append(c.create_rectangle(x - size*i, y, x+size-size*i, y+size, fill="blue"))

tk.mainloop()
