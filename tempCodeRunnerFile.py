import pygame
from settings import *
from snake import Snake

YELLOW = '#ffcc00'
ORANGE = '#ffa900'

class Main:
    def __init__(self):
        self.Rows = ROWS
        self.Cols = COLS
        self.Wh = WINDOW_HEIGHT
        self.Ww = WINDOW_WIDTH
        self.CellSize = CELL_SIZE
        self.Screen = Screen
        self.bg_rects = self.create_bg_rects(self.Rows,self.Cols)
        self.snake = Snake()

    def create_bg_rects(self,ROWS,COLS):
        rects = [pygame.Rect((col + int(row%2 == 0)) * self.CellSize,row*self.CellSize,self.CellSize,self.CellSize) for col in range(0,COLS,2) for row in range(ROWS)]
        return rects

    def draw_board(self):
        for rect in self.bg_rects:
            pygame.draw.rect(self.Screen, ORANGE, rect)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.VIDEORESIZE:
                    resize_screen(event.w, event.h)
                    print(self.Rows)
                    self.bg_rects = self.create_bg_rects(self.Rows,self.Cols)
                    

            self.Screen.fill(YELLOW)
            self.draw_board()
            pygame.display.update()