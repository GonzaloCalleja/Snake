
# C:\Users\gonza\PycharmProjects\Snake\grid.py
# Program to define the Grid object in a snake game

from tkinter import *
import snake


class Grid(Frame):

    def __init__(self, master, tile_number=10, side_len=400):

        # The frame the game will be played in (maybe should extend Frame instead of containing it)
        # self.frame = Frame(master=master, bg="red")
        super().__init__(master=master, bg="red")

        # stop internal elements from resizing it
        self.pack_propagate(0)

        # Place in the center of whatever the container is
        self.place(in_=master, anchor="c", relx=.5, rely=.5)

        # Making it listen to cursor events
        self.bind('<Left>', self.left_key)
        self.bind('<Right>', self.right_key)
        self.bind('<Up>', self.up_key)
        self.bind('<Down>', self.down_key)

        # self.focus_set()

        # VARIABLES FROM ARGUMENTS:

        # Number fo tiles, by default it is 10 - For more advanced levels, it can be more
        self.tile_number = tile_number
        # Total side length of the canvas - same as the Frame iself
        self.side_len = side_len

        # VARIABLES CALCULATED IN __init():

        # Initialize the canvas where the game is drawn
        self.game_canvas = Canvas(master=self, bg="yellow", height=self.side_len, width=self.side_len)
        # Constrain it to the size of frame
        self.game_canvas.grid(row=0, column=0)
        # self.game_canvas.attributes("-alpha", .30)
        # Doesn't work, both frame and canvas cannot be seen
        # self.game_canvas.pack(fill=BOTH, expand=YES)

        # Declare the border width for the game tiles - maybe of game element
        self.border = 1

        # Initialize snake
        #self.snake = snake.Snake()

        # Calculate the individual tile size depending on the total space, the number of tiles necessary
        # and the border each tile has
        self.tile_size = self.side_len // self.tile_number - (2 * self.border)

        # Test Drawing on the canvas created
        self.game_canvas.create_rectangle(10, 10, 100, 100, fill="blue")
        # self.game_canvas.create_line(100, 10, 100, 100, fill="white")
        # self.game_canvas.create_line(10, 10, 10, 100, fill="white")
        # self.game_canvas.create_line(10, 10, 100, 10, fill="white")
        # self.game_canvas.create_line(10, 100, 100, 100, fill="white")

        # Declare a two dimensional list(I found 2 possible ways):
        # 1)
        # self.canvas_array = [[None for x in range(self.size)] for y in range(self.size)]
        # 2)
        self.canvas_array = [[None] * self.tile_number for row in range(self.tile_number)]

        # The function list() is necessary to turn the range() from an iterable into a list
        # However, this populates the list with the elements indexes
        # self.canvas_array = [list(range(self.size)) for y in range(self.size)]
        # This one doesn't work because int cannot be turned into list
        # self.canvas_array = list(list(range(self.size)))
        # This doesn't work because it copies the same list -> When one is modified, they all are
        # self.canvas_array = [[None] * self.size] * self.size

        # from (0,0) to (9,9)
        # for y, row in enumerate(self.canvas_array):
        #     for x, tile in enumerate(row):
        #         self.game_canvas.create_rectangle(x*self.tile_size + self.border * 2, y*self.tile_size + self.border * 2,
        #                                           x*self.tile_size+self.tile_size + self.border * 2, y*self.tile_size + self.tile_size + self.border * 2,
        #                                           fill="blue")

        # for i in range(self.tile_number):
        #     for j in range(self.tile_number):
        #         self.canvas_array[i][j] = Canvas(master=self, bg="black", width=self.tile_size, height=self.tile_size,
        #                                          highlightthickness=self.border, highlightbackground="green")
        #         self.canvas_array[i][j].grid(row=i, column=j)

    def right_key(self, event):
        self.snake.change("East")
        print("hello")

    def left_key(self, event):
        self.snake.change("West")

    def down_key(self, event):
        self.snake.change("South")

    def up_key(self, event):
        self.snake.change("North")


# For testing purposes:
if __name__ == "__main__":

    tk = Tk()
    tk.title("Test Grid")
    size = 300
    tk.geometry(str(size)+"x"+str(size))

    # from 20 to 30 it lags and after it is unmanageable
    grid = Grid(tk, 10, size)

    tk.mainloop()
