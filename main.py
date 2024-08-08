from settings import *
from snake import Snake
from apple import Apple

YELLOW = '#ffcc00'
ORANGE = '#ffa900'

class Main:
    def __init__(self):
        self.Screen =  pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg_rects = [pygame.Rect((col + int(row%2 == 0)) * CELL_SIZE,row * CELL_SIZE,CELL_SIZE,CELL_SIZE) for col in range(0,COLS,2) for row in range(ROWS)]
        self.snake = Snake()
        self.apple = Apple(self.snake)
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event,200)

    def draw_board(self):
        self.Screen.fill(YELLOW)
        for rect in self.bg_rects:
            pygame.draw.rect(self.Screen, ORANGE, rect)
            
    def collision(self):
        if self.snake.body[0] == self.apple.pos:
            self.snake.has_eaten = True
            self.apple.set_pos()
        elif self.snake.body[0] in self.snake.body[1:]:
            for i in range (1,len(self.snake.body)):
                if self.snake.body[0] == self.snake.body[i]:
                    self.snake.body = self.snake.body[:i]
                    break
        elif self.snake.body[0].x < 0:
            self.snake.body[0].x = COLS - 1
        elif self.snake.body[0].x > COLS - 1:
            self.snake.body[0].x = 0
        elif self.snake.body[0].y < 0:
            self.snake.body[0].y = ROWS - 1
        elif self.snake.body[0].y > ROWS - 1:
            self.snake.body[0].y = 0
            
    def input(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.snake.direction.x != -1:
                self.snake.direction = pygame.Vector2(1, 0)
            elif event.key == pygame.K_LEFT and self.snake.direction.x != 1:
                self.snake.direction = pygame.Vector2(-1, 0)
            elif event.key == pygame.K_UP and self.snake.direction.y != 1:
                self.snake.direction = pygame.Vector2(0, -1)
            elif event.key == pygame.K_DOWN and self.snake.direction.y != -1:
                self.snake.direction = pygame.Vector2(0, 1)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == self.update_event:
                    self.snake.move()
                self.input(event)
                    
            self.collision()
            self.draw_board()
            self.apple.draw()
            self.snake.draw()
            pygame.display.update()

main = Main()
main.game_loop()
