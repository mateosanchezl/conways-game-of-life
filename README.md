# Conway's Game of Life

## Introduction
Conway's Game of Life is a zero-player cellular automaton game devised by John Horton Conway, a British mathematician.  

The game consists of 4 rules, by which cells can die, be born and reproduce:

- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

This implementation uses NumPy for efficient state management, as well as Pygame for rendering the simulation.

## Features

The simple implementation allows users to:

- Visualise the simulation of Conway's Game of life
- Interactive controls to pause/resume, reset game state and increase/decrease the number of cells in the simulation.

## Getting Started

