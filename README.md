# Pitcher-Game
## Overview
The Pitcher Game is an AI-powered Python application designed to solve the classic pitcher puzzle. The goal of the game is to measure out a specific amount of water using a set of pitchers with different capacities. This project leverages the A* algorithm to explore the state space dynamically, estimate heuristic costs, and find the most efficient path to achieve the target water volume.

## Features
Dynamic State Space Exploration: Efficiently explores possible states using the A* algorithm.
Heuristic Cost Estimation: Utilizes heuristic functions to estimate the cost to reach the goal state.
Efficient Pathfinding: Finds the minimum steps required to achieve the target water volume.
User-Friendly Interface: Provides an intuitive command-line interface for user interaction.

## Requirements
- Python 3.x
- Required Python libraries: numpy

## Installation
1. Clone the repository:
``` git clone https://github.com/K-Boomika/Pitcher-Game.git```

``` cd Pitcher-Game```

2. Install the required dependencies:
``` pip install numpy ```

3. Run the pitcher_game.py script:
``` python pitcher_game.py filename.txt``` 

Replace filename.txt with the name of your input file containing the pitcher capacities and target volume.

## Example
Suppose you have pitchers with capacities 5 and 3 liters, and you need to measure exactly 4 liters. 

Create a text file named example.txt with the following content:

5,3

4

The program will find the minimum steps required to achieve the target volume using the A* algorithm.

## Algorithm Explanation
The A* algorithm is used for its efficiency in finding the shortest path to the goal. It combines the strengths of Dijkstra's algorithm and Greedy Best-First-Search, using both the actual distance from the start and the estimated distance to the goal to prioritize states.

The program works by representing the state space as a tree, where each node represents a state (combination of water levels in the pitchers). The algorithm starts from the initial state (all pitchers empty) and explores possible actions (filling a pitcher, emptying a pitcher, pouring water from one pitcher to another) to reach the goal state (a specific water level in one of the pitchers).

The algorithm uses a heuristic function to estimate the cost of reaching the goal from a given state. This heuristic guides the search process, allowing the algorithm to prioritize nodes that are more likely to lead to the goal quickly. The algorithm continues exploring nodes until it reaches the goal state, finding the shortest path to achieve the target water volume.

The program then prints the shortest path, which is the minimum number of steps required to achieve the target volume, along with the intermediate states and actions taken at each step.
