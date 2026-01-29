# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Conway's Game of Life implementation in Python with interactive pygame visualization. This is a zero-player cellular automaton simulation with a clean separation between game logic and UI.

## Setup and Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

Dependencies: `numpy>=1.24.0`, `pygame>=2.5.0`

## Running the Application

```bash
# Run the simulation
python main.py
```

Interactive controls are displayed in the terminal on startup.

## Architecture

### Core Components

**`game.py`** - Pure game logic layer
- `GameOfLife` class: Manages grid state and simulation rules
- Core methods: `step()` (advance generation), `count_neighbors()` (toroidal wrapping)
- No UI dependencies - can be used standalone or tested independently
- Stores grid as NumPy array for efficient computation
- Includes predefined patterns in `PATTERNS` dict (glider, blinker, toad, beacon, pulsar)

**`main.py`** - Pygame visualization and interaction layer
- Handles all pygame rendering (green cells on black background)
- Event loop for user input (keyboard/mouse)
- Configurable via constants: `GRID_WIDTH`, `GRID_HEIGHT`, `CELL_SIZE`, `FPS`
- Maintains separation of concerns: never directly implements game rules

### Key Design Patterns

**Separation of Concerns**: Game logic (`game.py`) is completely decoupled from visualization (`main.py`). The `GameOfLife` class has no pygame dependencies and can be used in other contexts (CLI, web, tests).

**Toroidal Grid**: The grid wraps at edges (see `count_neighbors()` using modulo operator), creating an infinite-like plane where patterns can travel continuously.

**State Management**: Game state (grid, generation counter) lives entirely in the `GameOfLife` instance. The main loop only reads state for rendering.

## Configuration

All visual/performance settings in `main.py`:
- `GRID_WIDTH`, `GRID_HEIGHT`: Simulation dimensions
- `CELL_SIZE`: Pixel size per cell (affects window size)
- `FPS`: Simulation speed
- Color constants: `BLACK`, `GREEN`, `WHITE`, `GRAY`

## Testing

No test framework is currently configured. When adding tests:
- Test `game.py` logic independently from pygame
- Focus on Conway's rules implementation in `step()`
- Verify edge cases in `count_neighbors()` (grid wrapping)
- Test pattern placement with `set_pattern()`
