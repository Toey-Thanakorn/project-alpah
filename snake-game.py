import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
SEG_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()
        self.direction = "Right"
        self.snake = [(SEG_SIZE*2, SEG_SIZE*2), (SEG_SIZE, SEG_SIZE*2), (0, SEG_SIZE*2)]
        self.food = None
        self.running = True
        self.score = 0
        self.create_food()
        self.draw_snake()
        self.root.bind("<Up>", lambda e: self.change_direction("Up"))
        self.root.bind("<Down>", lambda e: self.change_direction("Down"))
        self.root.bind("<Left>", lambda e: self.change_direction("Left"))
        self.root.bind("<Right>", lambda e: self.change_direction("Right"))
        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="green", tag="snake")

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
            y = random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
            if (x, y) not in self.snake:
                self.food = (x, y)
                break
        self.canvas.delete("food")
        self.canvas.create_oval(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="red", tag="food")

    def move_snake(self):
        if not self.running:
            return
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y-SEG_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y+SEG_SIZE)
        elif self.direction == "Left":
            new_head = (head_x-SEG_SIZE, head_y)
        else:
            new_head = (head_x+SEG_SIZE, head_y)
        # Check collision
        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over()
            return
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.create_food()
        else:
            self.snake.pop()
        self.draw_snake()
        self.root.after(100, self.move_snake)

    def change_direction(self, dir):
        opposite = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if dir != opposite.get(self.direction):
            self.direction = dir

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text=f"Game Over!\nScore: {self.score}", font=("Arial", 24), fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
