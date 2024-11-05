# Grid Game - User vs Computer

This project is a college group assignment created using Python and Pygame. It’s a grid-based game where the user competes against a computer opponent. The game supports 3x3, 4x4, and 5x5 grid sizes and tracks the number of wins for both the user and the computer. The computer opponent uses advanced game theory algorithms, specifically Negamax and Minimax, to provide challenging gameplay.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Gameplay Options](#gameplay-options)
- [Algorithms Used](#algorithms-used)

## Features
- **Multiple Grid Sizes:** Choose between 3x3, 4x4, and 5x5 grid configurations.
- **User vs Computer:** Engage in a battle against a computer player.
- **Smart Computer AI:** The computer uses Negamax and Minimax algorithms to make strategic moves.
- **Win Tracking:** The program keeps track of the wins for both the user and the computer.

## Installation

To run the game, ensure that you have Python and Pygame installed.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/grid-game
   cd grid-game
   ```

2. **Install Pygame:**
   ```bash
   pip install pygame
   ```

3. **Run the Game:**
   ```bash
   python main.py
   ```

## How to Play
1. Choose the grid size (3x3, 4x4, or 5x5).
2. Take turns with the computer to place your symbol on the grid.
3. The game ends when one player achieves the winning condition for the chosen grid size or if there is a tie.
4. The program will track and display the number of wins for each player.

## Gameplay Options
- **Grid Sizes:** 
  - 3x3
  - 4x4
  - 5x5
- **AI Algorithms:** The computer’s moves are determined by either Negamax or Minimax logic, creating a challenging experience for the user.

## Algorithms Used
- **Minimax:** A recursive algorithm that evaluates all possible moves, aiming to minimize potential loss for a worst-case scenario.
- **Negamax:** An optimization of Minimax commonly used in two-player games that evaluates moves in terms of a single value, simplifying code and calculations.
