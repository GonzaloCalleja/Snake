
import tkinter as t


def grow(timer):
    global length
    if timer % 10 == 0:
        length += 1


def move():
    global x
    global y
    c.delete("all")
    x += velx
    y += vely

    c.create_rectangle(x, y, x + size, y+size, fill="blue")

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

x = 50
y = 50
velx = 0
vely = 0
length = 2
timer = 0
size = 100

# c = t.Canvas(tk, bg="#000000", bd=0, width=480, height=360)
c = t.Canvas(tk, bg="#000000", width=480, height=360)

c.create_rectangle(x, y, x+size, y+size, fill="blue")

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