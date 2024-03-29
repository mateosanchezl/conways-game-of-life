# Conway's Game of Life

## Introduction
Conway's Game of Life is a zero-player cellular automaton game devised by John Horton Conway, a British mathematician.  

The game consists of 4 rules, by which cells can die, be born and reproduce:

- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

This implementation uses NumPy for efficient state management, as well as Pygame for rendering the simulation.

<img width="993" alt="Screenshot 2024-03-29 at 13 00 07" src="https://github.com/mateosanchezl/conways-game-of-life/assets/146749266/686eb6ae-599c-4e12-a172-43f65795c8ce">

<img width="999" alt="Screenshot 2024-03-29 at 13 00 29" src="https://github.com/mateosanchezl/conways-game-of-life/assets/146749266/52a8573f-97ca-460f-a8d3-e05cca7d514a">

## Features

The simple implementation allows users to:

- Visualise the simulation of Conway's Game of life
- Interactive controls to pause/resume, reset game state and increase/decrease the number of cells in the simulation.

## Getting Started

This section provides instructions for setting up and running Conway's Game of Life on your system.

### Prerequisites

- Python 3.x
- Git (for cloning the repository)

### Setup

**Clone this repository using**:
```bash
git clone https://github.com/your-username/conways-game-of-life.git
cd conways-game-of-life
```

### On macOS/Linux:
**Make the setup script executable and then run it using**:
```bash
chmod +x run_game.sh
./run_game.sh
```
### On Windows:
**Double click the `run_game.bat` file.**

