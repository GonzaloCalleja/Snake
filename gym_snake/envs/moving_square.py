
import tkinter as t


def grow(timer):
    global length
    if timer % 10 == 0:
        length += 1


def borderless():

    global x, y

    if x + size > 480:
        c.create_rectangle(0, y, x + size - 480, y+size, fill="blue")
        if x > 480:
            x = 0

    if x < 0:
        c.create_rectangle(x + 480, y, x + size + 480, y+size, fill="blue")
        if x + size < 0:
            x = 480 - size

    if y + size > 360:
        c.create_rectangle(x, 0, x + size, y + size - 360, fill="blue")
        if y > 360:
            y = 0

    if y < 0:
        c.create_rectangle(x, y + 360, x + size, y + size + 360, fill="blue")
        if y + size < 0:
            y = 360 - size

    if x + size > 480 and y + size > 360:
        c.create_rectangle(0, 0, x + size - 480, y + size - 360, fill="blue")
        if x > 480 and y > 360:
            x = 0
            y = 0

    if x < 0 and y < 0:
        c.create_rectangle(x + 480, y + 360, x + size + 480, y+size + 360, fill="blue")
        if x + size < 0 and y + size < 0:
            x = 480 - size
            y = 360 - size

    if x + size > 480 and y < 0:
        c.create_rectangle(0, y + 360, x + size - 480, y + size + 360, fill="blue")
        if x > 480 and y < 0:
            x = 0
            y = 360 - size

    if x < 0 and y + size > 360:
        c.create_rectangle(x + 480, 0, x + size + 480, y + size - 360, fill="blue")
        if x + size < 0 and y + size < 0:
            x = 480 - size
            y = 0

def move():
    global x
    global y
    global rects

    if velx:
        c.delete("all")
        x += velx
        for i in range(length):
            rects.pop(i)
            rects.insert(i, c.create_rectangle(x + size * i, y, x + size + size * i, y + size, fill="blue"))

    if vely:
        c.delete("all")
        y += vely
        for i in range(length):
            rects.pop(i)
            rects.insert(i, c.create_rectangle(x , y+ size * i, x + size , y + size+ size * i, fill="blue"))

    no_borders = True

    if no_borders:
        borderless()

    # grow(timer)
    # timer += 1

    tk.after(10, move)


def key_press(event):

    global velx, vely
    pr = event.keysym
    change = 1

    if pr == "Left":
        velx = -change
        vely = 0
    elif pr == "Right":
        #if y % rows == 0:
        velx = change
        vely = 0

    elif pr == "Down":
        velx = 0
        vely = change
    elif pr == "Up":
        velx = 0
        vely = -change


# def key_release(event):
#     global vely, velx
#     vely=0
#     velx=0
#     pass


tk = t.Tk()

x = 240
y = 180
velx = 0
vely = 0
length = 10
timer = 0
size = 10
rows = 36
columns = 48

# c = t.Canvas(tk, bg="#000000", bd=0, width=480, height=360)
c = t.Canvas(tk, bg="#000000", width=480, height=360)

rects = []

for i in range(length):
    rects.append(c.create_rectangle(x +i*size, y, x+size +i*size, y+size, fill="blue"))

c.focus_set()

move()
c.bind("<KeyPress>", key_press)
# c.bind("<KeyRelease>", key_release)
c.pack()
tk.mainloop()

# on the id returned when creating a rectangle
# canvas.coords
# canvas.delete


# for x in range(300):
#     y = x = 1
#     time.sleep(0.01)
#     canvas.move(rc1, x, -y)
#     canvas.move(rc2, x, y)
#     canvas.update()
# root.mainloop()