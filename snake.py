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
direction = "right"


class Food:
    def __init__(self):
        self.x = random.randint(0, int((GAME_WIDTH-1)/SPACE_SIZE)) * SPACE_SIZE
        self.y = random.randint(0, int((GAME_HEIGHT-1)/SPACE_SIZE)) * SPACE_SIZE
        
        self.pic = canvas.create_oval(self.x, self.y, self.x + SPACE_SIZE, self.y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        

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


def new_turn(snake, food):
    x,y = snake.coordinates[0]
    global score
    
    if direction == 'down':
        y += SPACE_SIZE
    elif direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, [x, y])
    new_square =canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="shneke")
    snake.squares.insert(0, new_square)
    
    if x == food.x and y == food.y:
        score += 1
        label.config(text="Score:{}".format(score))
         
        canvas.delete(food.pic)
        food = Food()
    else:
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        del snake.coordinates[-1]
    
    if check_collision(snake):
        endgame()
        
    window.after(SPEED, new_turn, snake, food)

def change_dir(new_dir):
    global direction
    
    if (new_dir == 'left') and direction != 'right':
        direction = new_dir
        
    elif (new_dir == 'right') and direction != 'left':
        direction = new_dir
        
    elif (new_dir == 'up') and direction != 'down':
        direction = new_dir
        
    elif (new_dir == 'down') and direction != 'up':
        direction = new_dir

def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def endgame():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

window = Tk()
window.title("Snake game")

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.grid()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.grid()

snake = Snake()
food = Food() 
window.update()

window.bind('<Left>', lambda event: change_dir('left'))
window.bind('<Right>', lambda event: change_dir('right'))
window.bind('<Up>', lambda event: change_dir('up'))
window.bind('<Down>', lambda event: change_dir('down'))


new_turn(snake,food)
window.mainloop()