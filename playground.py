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

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] AI Playground v1.1")
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
    else:
        for i in range(count):
            pattern = generate_pattern(seed=i)
            print(f"{i+1:3d}: {pattern}")

    print("-" * 40)
    print("Generation complete!")

if __name__ == "__main__":
    main()