# Conway's Game of Life

A Python implementation of Conway's Game of Life with interactive pygame visualization.

## About

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. It's a zero-player game where the evolution is determined by its initial state.

### Rules

1. Any live cell with 2-3 live neighbors survives
2. Any dead cell with exactly 3 live neighbors becomes alive
3. All other cells die or stay dead

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the simulation:

```bash
python main.py
```

## Controls

- **SPACE**: Pause/Resume simulation
- **R**: Randomize the grid
- **C**: Clear the grid
- **G**: Place a glider pattern at mouse position
- **Click**: Toggle individual cells
- **Q/ESC**: Quit

## Features

- Interactive pygame visualization with green cells on black background
- Real-time generation and population counter
- Pause/resume functionality
- Click to toggle cells manually
- Randomize grid with adjustable probability
- Pre-defined patterns (glider, blinker, toad, beacon, pulsar)
- Wrapping grid edges (toroidal topology)

## Project Structure

- `game.py`: Core Game of Life logic and rules engine
- `main.py`: Pygame visualization and user interaction
- `requirements.txt`: Python dependencies

## Customization

You can adjust these constants in `main.py`:

- `GRID_WIDTH`, `GRID_HEIGHT`: Grid dimensions
- `CELL_SIZE`: Size of each cell in pixels
- `FPS`: Simulation speed (frames per second)

## License

MIT
