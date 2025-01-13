from tkinter import *
import random

GAME_WIDTH = 500
GAME_HEIGHT = 250
SPEED = 65
SPACE_SIZE = 25
BODY_PARTS = 4
SNAKE_COLOR = "#FF0000"
FOOD_COLOR = "#FF00FF"
BACKGROUND_COLOR = "#00FF00"
score = 0
direction = "left"

class Food:
    def __init__(self):
        self.x = random.randint(0, int((GAME_WIDTH-1)/SPACE_SIZE)) * SPACE_SIZE
        self.y = random.randint(0, int((GAME_HEIGHT-1)/SPACE_SIZE)) * SPACE_SIZE
        
        canvas.create_oval(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        

class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="shneke")
                self.squares.append(square)

def new_turn():
    pass

def change_dir():
    pass

def check_collision():
    pass

def endgame():
    pass

window = Tk()
window.title("Snake game")

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.grid()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.grid()

snake = Snake()
food = Food() 
window.update()

window.mainloop()