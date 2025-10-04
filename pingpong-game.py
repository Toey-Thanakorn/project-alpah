import tkinter as tk

WIDTH = 500
HEIGHT = 400
BALL_SIZE = 20
PAD_WIDTH = 80
PAD_HEIGHT = 10
SPEED = 5

class PingPongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Pong Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.ball = self.canvas.create_oval(WIDTH//2, HEIGHT//2, WIDTH//2+BALL_SIZE, HEIGHT//2+BALL_SIZE, fill="white")
        self.pad = self.canvas.create_rectangle(WIDTH//2-PAD_WIDTH//2, HEIGHT-PAD_HEIGHT-10,
                                                WIDTH//2+PAD_WIDTH//2, HEIGHT-10, fill="blue")
        self.ball_dx = SPEED
        self.ball_dy = -SPEED
        self.score = 0
        self.running = True
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.update_game()

    def move_left(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.pad)
        if x1 > 0:
            self.canvas.move(self.pad, -20, 0)

    def move_right(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.pad)
        if x2 < WIDTH:
            self.canvas.move(self.pad, 20, 0)

    def update_game(self):
        if not self.running:
            return
        self.move_ball()
        self.root.after(20, self.update_game)

    def move_ball(self):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        pad_x1, pad_y1, pad_x2, pad_y2 = self.canvas.coords(self.pad)
        # Ball movement
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        x1 += self.ball_dx
        x2 += self.ball_dx
        y1 += self.ball_dy
        y2 += self.ball_dy
        # Wall collision
        if x1 <= 0 or x2 >= WIDTH:
            self.ball_dx = -self.ball_dx
        if y1 <= 0:
            self.ball_dy = -self.ball_dy
        # Paddle collision
        if y2 >= pad_y1 and pad_x1 < x2 and pad_x2 > x1:
            self.ball_dy = -self.ball_dy
            self.score += 1
        # Game over
        if y2 >= HEIGHT:
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text=f"Game Over!\nScore: {self.score}", font=("Arial", 24), fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = PingPongGame(root)
    root.mainloop()
