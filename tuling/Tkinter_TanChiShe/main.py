import tkinter
import random
class Food():
    def __init__(self):
        self.new_food()
    def new_food(self):
        x = random.randrange(50,480,10)
        y = random.randrange(50,480,10)
        self.positon = x,y
        self.queue.put({"food":self.positon})
class Snake():
    def move(self):
        new_snake_point =self.cal_new_pos()
        if self.food.positon == new_snake_point:
            self.points_earned += 1
            self.queue.put({"points_earned":self.points_earned})
            self.food.new_food()
        else:
            self.snake_points.pop(0)
            self.check_game_over(new_snake_point)
    def cal_new_position(self):
        last_x,last_y = self.snake_points[-1]
        if self.direction =="Up":
            new_snake_point = last_x,last_y-10
        return new_snake_point
    def key_pressed(self):
        pass



if __name__ == "__main__":
    pass