from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from bomb import Bomb
from scoreboard import Scoreboard
from sounds import play_sound
import turtle
import tkinter as tk
from tkinter import Button

GRID_SIZE = 20


class GridExample:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("grey")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()

        self.bomb = Bomb()
        self.scoreboard = Scoreboard()

        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

        self.draw_grid()

        self.game_is_on = True

    def draw_grid(self):
        grid_turtle = Turtle()
        grid_turtle.speed(0)
        grid_turtle.color("white")
        grid_turtle.penup()

        for x in range(-300, 300, GRID_SIZE):
            grid_turtle.goto(x, -300)
            grid_turtle.pendown()
            grid_turtle.goto(x, 300)
            grid_turtle.penup()

        for y in range(-300, 300, GRID_SIZE):
            grid_turtle.goto(-300, y)
            grid_turtle.pendown()
            grid_turtle.goto(300, y)
            grid_turtle.penup()

    def exit_turtle_window(self):
        self.screen.bye()

    def update_game1(self):
        self.game_is_on = True
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            # Detect collision with food
            if self.snake.head.distance(self.food) < 13:
                play_sound("archivo.mp3")
                self.food.refresh()
                self.snake.extend()
                self.bomb.refresh()
                self.scoreboard.increase_score()

            # Detect collision with bomb
            if self.snake.head.distance(self.bomb) < 13:
                play_sound("sound.mp3")
                self.food.refresh()
                self.bomb.refresh()
                self.scoreboard.decrease_score()
                if self.scoreboard.score <= 0:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    self.screen.clear()
                    self.scoreboard.another()

            # Detect collision with wall
            if (
                    self.snake.head.xcor() > 290
                    or self.snake.head.xcor() < -290
                    or self.snake.head.ycor() > 290
                    or self.snake.head.ycor() < -290
            ):
                self.game_is_on = False
                self.scoreboard.game_over()
                self.screen.clear()
                self.screen.bgcolor("black")

            # Detect collision with tail
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    self.screen.clear()
                    self.scoreboard.another()
                    self.scoreboard.game_over()
                    self.screen.clear()


        self.screen.exitonclick()

    def update_game2(self):
        self.game_is_on = True
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.06)
            self.snake.move()

            # Detect collision with food
            if self.snake.head.distance(self.food) < 13:
                play_sound("archivo.mp3")
                self.food.refresh()
                self.snake.extend()
                self.bomb.refresh()
                self.scoreboard.increase_score()

            # Detect collision with bomb
            if self.snake.head.distance(self.bomb) < 13:
                play_sound("sound.mp3")
                self.food.refresh()
                self.bomb.refresh()
                self.scoreboard.decrease_score()
                if self.scoreboard.score <= 0:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    self.screen.clear()
                    self.screen.bgcolor("black")

            # Detect collision with wall
            if (
                    self.snake.head.xcor() > 290
                    or self.snake.head.xcor() < -290
                    or self.snake.head.ycor() > 290
                    or self.snake.head.ycor() < -290
            ):
                self.game_is_on = False
                self.scoreboard.game_over()
                self.screen.clear()
                self.screen.bgcolor("black")

            # Detect collision with tail
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    self.screen.clear()
                    self.screen.bgcolor("black")

        self.screen.exitonclick()

    def update_game3(self):
        self.game_is_on = True
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.03)
            self.snake.move()

            # Detect collision with food
            if self.snake.head.distance(self.food) < 13:
                play_sound("archivo.mp3")
                self.food.refresh()
                self.snake.extend()
                self.bomb.refresh()
                self.scoreboard.increase_score()

            # Detect collision with bomb
            if self.snake.head.distance(self.bomb) < 13:
                play_sound("sound.mp3")
                self.food.refresh()
                self.bomb.refresh()
                self.scoreboard.decrease_score()
                if self.scoreboard.score <= 0:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    self.screen.clear()
                    self.screen.bgcolor("black")

            # Detect collision with wall
            if (
                    self.snake.head.xcor() > 290
                    or self.snake.head.xcor() < -290
                    or self.snake.head.ycor() > 290
                    or self.snake.head.ycor() < -290
            ):
                self.game_is_on = False
                self.scoreboard.game_over()
                self.screen.clear()
                self.screen.bgcolor("black")

            # Detect collision with tail
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.scoreboard.game_over()
                    self.screen.clear()
                    self.screen.bgcolor("black")

        self.screen.exitonclick()
def level1():
    start = GridExample()
    start.update_game1()

def level2():
    start2 = GridExample()
    start2.update_game2()

def level3():
    start = GridExample()
    start.update_game3()

root = tk.Tk()
root.title("M")
root.geometry("500x500")

button1 = Button(root, text="LEVEL1", command=level1)
button1.pack(pady=30)

button2 = Button(root, text="LEVEL2", command=level2)
button2.pack(pady=60)

button3 = Button(root, text="LEVEL3", command=level2)
button3.pack(pady=70)

root.mainloop()

if __name__ == "__main__":
    level2()

if __name__ == "__main__":
    game = GridExample()
    game.update_game()

