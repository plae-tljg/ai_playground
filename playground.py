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

def generate_mandala(size=17, seed=None):
    if seed is not None:
        random.seed(seed)

    mandala = []
    center = size // 2
    for y in range(size):
        row = []
        for x in range(size):
            dist = abs(x - center) + abs(y - center)
            dist_from_center = ((x - center) ** 2 + (y - center) ** 2) ** 0.5
            if dist_from_center <= 1:
                row.append("◆")
            elif int(dist_from_center * 2) % 3 == 0:
                row.append("❀")
            elif dist % 2 == 0:
                row.append("✿")
            else:
                row.append("❁")
        mandala.append(row)
    return '\n'.join(''.join(row) for row in mandala)

def generate_noise(width=40, height=15, scale=0.3, seed=None):
    if seed is not None:
        random.seed(seed)

    chars = " .:-=+*#%@"
    noise = []
    for y in range(height):
        row = []
        for x in range(width):
            value = random.random()
            idx = min(int(value * len(chars)), len(chars) - 1)
            row.append(chars[idx])
        noise.append(row)
    return '\n'.join(''.join(row) for row in noise)

def generate_banner(text, width=40, seed=None):
    if seed is not None:
        random.seed(seed)

    border_char = random.choice(["═", "─", "╔", "╗", "╚", "╝"])
    chars = "░▒▓█"

    lines = []
    lines.append(border_char * width)
    padded = text.center(width - 2)
    lines.append(border_char + padded + border_char)
    lines.append(border_char * width)

    for i, line in enumerate(lines[1:-1], 1):
        decorative = random.choice(chars)
        lines[i] = decorative + line[1:-1] + decorative

    lines.insert(1, "│" + " ".join(random.choice(chars) for _ in range(width // 2 - 1)) + "│")
    lines.append("│" + " ".join(random.choice(chars) for _ in range(width // 2 - 1)) + "│")

    return '\n'.join(lines)

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
    elif mode == "mandala":
        for i in range(count):
            print(f"\n--- Mandala {i+1} ---")
            print(generate_mandala(seed=i))
    elif mode == "noise":
        for i in range(count):
            print(f"\n--- Noise {i+1} ---")
            print(generate_noise(seed=i))
    elif mode == "banner":
        text = sys.argv[2] if len(sys.argv) > 2 else "Hello World"
        for i in range(count):
            print(f"\n--- Banner {i+1} ---")
            print(generate_banner(text, seed=i))
    else:
        for i in range(count):
            pattern = generate_pattern(seed=i)
            print(f"{i+1:3d}: {pattern}")

    print("-" * 40)
    print("Generation complete!")

if __name__ == "__main__":
    main()