#!/usr/bin/env python3
"""
Simple AI playground demo script.
Generates text-based patterns and outputs them.
"""

import random
import sys
from datetime import datetime

def generate_ascii_art(width=40, height=10, seed=None):
    if seed is not None:
        random.seed(seed)

    chars = "░▒▓█"
    lines = []
    for i in range(height):
        row = ''.join(random.choice(chars) for _ in range(width))
        lines.append(row)
    return '\n'.join(lines)

def generate_pattern(seed=None):
    if seed is not None:
        random.seed(seed)

    patterns = [
        "████░░░░████░░░░████",
        "░░████░░░░████░░░░██",
        "██████░░░░░░░░░██████",
        "░░░░████████████░░░░",
    ]
    return random.choice(patterns)

def generate_spiral(size=15, seed=None):
    if seed is not None:
        random.seed(seed)

    spiral = []
    for y in range(size):
        row = []
        for x in range(size):
            dist = min(x, y, size-1-x, size-1-y)
            if dist % 2 == 0:
                row.append("●")
            else:
                row.append("○")
        spiral.append(row)
    return '\n'.join(''.join(row) for row in spiral)

def generate_maze(width=21, height=11, seed=None):
    if seed is not None:
        random.seed(seed)

    maze = []
    for y in range(height):
        row = []
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                row.append("█")
            elif random.random() < 0.3:
                row.append("█")
            else:
                row.append(" ")
        maze.append(row)

    maze[1][1] = "S"
    maze[height-2][width-2] = "E"

    return '\n'.join(''.join(row) for row in maze)

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] AI Playground v1.2")
    print("-" * 40)

    count = 10
    mode = "patterns"
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            mode = sys.argv[1]

    if mode == "ascii":
        for i in range(count):
            print(f"\n--- Generation {i+1} ---")
            print(generate_ascii_art(seed=i))
    elif mode == "maze":
        for i in range(count):
            print(f"\n--- Maze {i+1} ---")
            print(generate_maze(seed=i))
    elif mode == "spiral":
        for i in range(count):
            print(f"\n--- Spiral {i+1} ---")
            print(generate_spiral(seed=i))
    else:
        for i in range(count):
            pattern = generate_pattern(seed=i)
            print(f"{i+1:3d}: {pattern}")

    print("-" * 40)
    print("Generation complete!")

if __name__ == "__main__":
    main()