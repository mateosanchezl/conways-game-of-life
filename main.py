import pygame
import numpy as np

### RULES
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.

# Any live cell with two or three live neighbours lives on to the next generation.

# Any live cell with more than three live neighbours dies, as if by overpopulation.

# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

class Button:
    def __init__(self, x, y, w, h, text, screen: pygame.surface.Surface, func):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.COLOUR_LIGHT = (106, 90, 205)
        self.COLOUR_DARK = (177, 13, 201) 
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 20)
        self.button_text = self.font.render(self.text, True, (255, 255, 255))
        self.func = func
        self.text_rect = self.button_text.get_rect(center=(x + w // 2, y + h // 2))
        self.button_rect = pygame.Rect(x, y, w, h)

    def hovering(self, mouse_x, mouse_y):
        return self.button_rect.collidepoint(mouse_x, mouse_y)

    def draw_rounded_rect(self, rect, color, radius=0.4):
        corner_radius = int(radius * min(rect.size))
        pygame.draw.rect(self.screen, color, rect, border_radius=corner_radius)

    def display(self, mouse_x, mouse_y):
        color = self.COLOUR_DARK if self.hovering(mouse_x, mouse_y) else self.COLOUR_LIGHT
        self.draw_rounded_rect(self.button_rect, color)
        self.screen.blit(self.button_text, self.text_rect)
    
class Game:
    pygame.init()
    def __init__(self):
        self.SCREEN_SIZE = (1000, 600)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.WIDTH = self.screen.get_width()
        self.HEIGHT = self.screen.get_height()
        self.BLOCK_SIZE = 5
        self.BG_COLOUR = (11, 38, 40)
        self.CELL_COLOUR = (57, 255, 20)
        self.FRAME_RATE = 60
        self.LIFE_COUNT = 500
        self.grid = np.zeros(shape=(int(self.SCREEN_SIZE[0] / self.BLOCK_SIZE), int(self.SCREEN_SIZE[1] / self.BLOCK_SIZE)))
        self.clock = pygame.time.Clock()
        self.running = True
        self.play = False
        self.font = pygame.font.SysFont('Arial', 40)
        self.generated_cell_coords = []
        self.buttons = [Button(self.WIDTH / 2 - 40,10, 110, 40,'Play/Pause', screen=self.screen, func=self.toggle_play),
                        Button(self.WIDTH / 2 + 80, 10, 60, 40, 'Reset', screen=self.screen, func=self.reset_grid),
                        Button(self.WIDTH / 2 - 90, 10, 40, 40, '+', screen=self.screen, func=self.create_life),
                        Button(self.WIDTH / 2 - 140, 10, 40, 40, '-', screen=self.screen, func=self.destroy_life)]

    def check_live_neighbours(self, row, col):
        rows, cols = self.grid.shape

        # boundaries
        top_boundary = max(0, row - 1)
        bottom_boundary = min(rows, row + 2)
        left_boundary = max(0, col - 1)
        right_boundary = min(cols, col + 2)
        
        sub_array = self.grid[top_boundary:bottom_boundary, left_boundary:right_boundary]
        return np.sum(sub_array) - self.grid[row][col]

    def alive(self, cell, live_neighbours):
        if cell == 1:
            if live_neighbours < 2:
                return False
            if live_neighbours == 2 or live_neighbours == 3:
                return True
            if live_neighbours > 3:
                return False
        if cell == 0:
            return live_neighbours == 3

    def step(self):
        for i in range(len(self.grid[:, 0])):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = 1 if self.alive(self.grid[i][j], self.check_live_neighbours(i, j)) else 0

    def toggle_play(self):
        self.play = not self.play
    
    def destroy_life(self):
        coords_length = len(self.generated_cell_coords)
        selected_idxs = [np.random.randint(0, coords_length) for i in range(50)]
        for idx in selected_idxs:
            if self.grid[self.generated_cell_coords[idx][0], self.generated_cell_coords[idx][1]] == 1:
                self.grid[self.generated_cell_coords[idx][0], self.generated_cell_coords[idx][1]] = 0
        
    def create_life(self):
        rows, cols = self.grid.shape
        self.generated_cell_coords = [(np.random.randint(0, rows), np.random.randint(0, cols)) for i in range(self.LIFE_COUNT)]
        for coord in self.generated_cell_coords:
            self.grid[coord[0], coord[1]] = 1
    
    def reset_grid(self):
        self.grid = np.zeros(shape=(int(self.SCREEN_SIZE[0] / self.BLOCK_SIZE), int(self.SCREEN_SIZE[1] / self.BLOCK_SIZE)))
    
    def run(self):
        self.create_life()   
        while self.running:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.hovering(mouse_x, mouse_y):
                            button.func()                        
                     
            self.screen.fill(self.BG_COLOUR)
            
            if self.play: 
                self.step()
              
            for i in range(len(self.grid[:, 0])):
                for j in range(len(self.grid[0])):
                    x = i * self.BLOCK_SIZE
                    y = j * self.BLOCK_SIZE
                    cell = pygame.Rect(x, y, self.BLOCK_SIZE, self.BLOCK_SIZE)
                    pygame.draw.rect(self.screen, self.CELL_COLOUR if self.alive(self.grid[i][j], self.check_live_neighbours(i, j)) else self.BG_COLOUR, width=5, rect=cell)
                    
            for button in self.buttons:
                button.display(mouse_x, mouse_y)
                    
            pygame.display.flip()

            self.clock.tick(self.FRAME_RATE) 

        pygame.quit()
        
           
if __name__ == "__main__":
    game = Game()
    game.run()
