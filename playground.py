#!/usr/bin/env python3
"""
Simple AI playground demo script.
Generates text-based patterns and outputs them.
"""

import random
import sys
from datetime import datetime

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
    print(f"[{timestamp}] AI Playground v1.0")
    print("-" * 40)

    count = 10
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            pass

    for i in range(count):
        pattern = generate_pattern(seed=i)
        print(f"{i+1:3d}: {pattern}")

    print("-" * 40)
    print("Generation complete!")

if __name__ == "__main__":
    main()