# Maze Generator and Solver

A Python application that generates and solves mazes using Tkinter for visualization.

## Features

- Generate custom-sized mazes
- Visualize the maze generation process
- Solve generated mazes
- Display the solution path and the explored incorrect paths.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
   `git clone https://github.com/Antonvasilache/maze-solver`

3. Navigate to the project directory:
   `cd maze-solver`

## Usage

Run the main script:
`python3 main.py`

## How it works:
1. **Maze Generation**: 
   - Creates a grid based on user-specified dimensions
   - Randomly breaks down walls from a given entry point to an exit point

2. **Maze Solving**:
   - Finds a path from the entry to the exit
   - Marks the correct path with a red line
   - Highlights explored incorrect paths with a gray line

## Configuration

You can adjust the following parameters in the application:
- Grid size
- Cell width and height
- Position of the grid on the GUI
- Entry and exit points
