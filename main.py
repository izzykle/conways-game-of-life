"""Main entry point for Conway's Game of Life with pygame visualization."""
import pygame
import sys
from game import GameOfLife, PATTERNS


# Configuration
GRID_WIDTH = 80
GRID_HEIGHT = 60
CELL_SIZE = 10
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
GREEN = (0, 255, 0)


def main():
    """Run the Game of Life simulation."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()
    
    game = GameOfLife(GRID_WIDTH, GRID_HEIGHT)
    game.randomize(probability=0.25)
    
    running = True
    paused = False
    
    print("Controls:")
    print("  SPACE: Pause/Resume")
    print("  R: Randomize grid")
    print("  C: Clear grid")
    print("  G: Place glider at mouse")
    print("  Click: Toggle cell")
    print("  Q/ESC: Quit")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                    print("Paused" if paused else "Running")
                elif event.key == pygame.K_r:
                    game.randomize(probability=0.25)
                    print("Grid randomized")
                elif event.key == pygame.K_c:
                    game.clear()
                    print("Grid cleared")
                elif event.key == pygame.K_g:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x = mouse_x // CELL_SIZE
                    grid_y = mouse_y // CELL_SIZE
                    if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                        game.set_pattern(PATTERNS['glider'], grid_x, grid_y)
                        print(f"Glider placed at ({grid_x}, {grid_y})")
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = mouse_x // CELL_SIZE
                grid_y = mouse_y // CELL_SIZE
                if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                    game.grid[grid_y, grid_x] = 1 - game.grid[grid_y, grid_x]
        
        # Update simulation
        if not paused:
            game.step()
        
        # Draw
        screen.fill(BLACK)
        
        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if game.grid[y, x] == 1:
                    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, 
                                     CELL_SIZE - 1, CELL_SIZE - 1)
                    pygame.draw.rect(screen, GREEN, rect)
        
        # Draw info
        font = pygame.font.Font(None, 24)
        info_text = f"Gen: {game.generation}  Alive: {game.get_alive_count()}"
        if paused:
            info_text += "  [PAUSED]"
        text_surface = font.render(info_text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (5, 5)
        
        # Draw background for text
        bg_rect = text_rect.inflate(10, 6)
        pygame.draw.rect(screen, BLACK, bg_rect)
        screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()