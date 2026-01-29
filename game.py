"""Conway's Game of Life implementation."""
import numpy as np
from typing import Tuple


class GameOfLife:
    """Conway's Game of Life simulator.
    
    Rules:
    1. Any live cell with 2-3 live neighbors survives
    2. Any dead cell with exactly 3 live neighbors becomes alive
    3. All other cells die or stay dead
    """
    
    def __init__(self, width: int = 50, height: int = 50):
        """Initialize the game grid.
        
        Args:
            width: Grid width
            height: Grid height
        """
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.generation = 0
    
    def randomize(self, probability: float = 0.3):
        """Populate grid with random live cells.
        
        Args:
            probability: Chance of each cell being alive (0.0 to 1.0)
        """
        self.grid = np.random.choice([0, 1], size=(self.height, self.width), 
                                     p=[1-probability, probability])
        self.generation = 0
    
    def set_pattern(self, pattern: np.ndarray, x: int = 0, y: int = 0):
        """Place a pattern on the grid at specified position.
        
        Args:
            pattern: 2D array representing the pattern
            x: X coordinate (column)
            y: Y coordinate (row)
        """
        h, w = pattern.shape
        self.grid[y:y+h, x:x+w] = pattern
    
    def count_neighbors(self, x: int, y: int) -> int:
        """Count live neighbors for a cell.
        
        Args:
            x: X coordinate (column)
            y: Y coordinate (row)
            
        Returns:
            Number of live neighbors (0-8)
        """
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                count += self.grid[ny, nx]
        return count
    
    def step(self):
        """Advance the simulation by one generation."""
        new_grid = np.zeros_like(self.grid)
        
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current = self.grid[y, x]
                
                # Apply Conway's rules
                if current == 1 and neighbors in [2, 3]:
                    new_grid[y, x] = 1
                elif current == 0 and neighbors == 3:
                    new_grid[y, x] = 1
        
        self.grid = new_grid
        self.generation += 1
    
    def get_alive_count(self) -> int:
        """Return the number of living cells."""
        return np.sum(self.grid)
    
    def clear(self):
        """Clear all cells."""
        self.grid = np.zeros((self.height, self.width), dtype=int)
        self.generation = 0


# Common patterns
PATTERNS = {
    'glider': np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]),
    'blinker': np.array([
        [1, 1, 1]
    ]),
    'toad': np.array([
        [0, 1, 1, 1],
        [1, 1, 1, 0]
    ]),
    'beacon': np.array([
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]),
    'pulsar': np.array([
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
    ])
}