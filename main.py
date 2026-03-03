import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Intianlize Game Window and configure windows settings
window = tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#Center the game window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#Calculate X and Y Positions
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#Add X and Y to Window
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


#Initalize Game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) #Single tile for sankes head

def draw():
    global snake

    #Draw Sanke
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green")

window.mainloop()