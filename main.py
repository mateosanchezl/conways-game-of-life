import pygame
import numpy as np

### RULES
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.

# Any live cell with two or three live neighbours lives on to the next generation.

# Any live cell with more than three live neighbours dies, as if by overpopulation.

# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
class Button:
    def __init__(self) -> None:
        self.x = 1
    
class Game:
    pygame.init()
    def __init__(self):
        self.SCREEN_SIZE = (800, 500)
        self.BLOCK_SIZE = 5
        self.BG_COLOUR = (8, 0, 66, 1)
        self.CELL_COLOUR = (4, 255, 140, 1)
        self.grid = np.zeros(shape=(int(self.SCREEN_SIZE[0] / self.BLOCK_SIZE), int(self.SCREEN_SIZE[1] / self.BLOCK_SIZE)))
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True
        
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

    def create_life(self, n):
        rows, cols = self.grid.shape
        idxs = np.random.randint(np.abs(rows-cols), size=(2, n))

        for i in range(n):
            for j in range(n):
                self.grid[idxs[0][i]][idxs[1][j]] = 1
        
    def run(self):
        self.create_life(30)        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(self.BG_COLOUR)

            self.step()
            # RENDER YOUR GAME HERE
            for i in range(len(self.grid[:, 0])):
                for j in range(len(self.grid[0])):
                    x = i * self.BLOCK_SIZE
                    y = j * self.BLOCK_SIZE
                    cell = pygame.Rect(x, y, self.BLOCK_SIZE, self.BLOCK_SIZE)
                    # if cell not in self.cells:
                    #     self.cells.append(cell)
                    pygame.draw.rect(self.screen, self.CELL_COLOUR if self.alive(self.grid[i][j], self.check_live_neighbours(i, j)) else self.BG_COLOUR, width=5, rect=cell)
            # flip() the display to put your work on screen
                
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()



    
if __name__ == "__main__":
    game = Game()
    game.run()
    