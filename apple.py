from settings import *
from random import choice

class Apple:
    def __init__(self,snake):
        self.pos = pygame.Vector2(0,0)
        self.Screen = pygame.display.get_surface()
        self.snake = snake
        self.set_pos()
        
    def set_pos(self):
        avaiable_pos = [pygame.Vector2(x,y) for x in range(COLS) for y in range(ROWS) if pygame.Vector2(x,y) not in self.snake.body]
        self.pos = choice(avaiable_pos)
        
    def draw(self):
        pygame.draw.rect(self.Screen, 'blue', pygame.Rect(self.pos.x * CELL_SIZE,self.pos.y * CELL_SIZE,CELL_SIZE,CELL_SIZE))
        