#!/usr/bin/env python3
"""
Simple AI playground demo script.
Generates text-based patterns and outputs them.
"""

import math
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

def generate_heatmap(width=30, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    chars = " .:;+*#@"
    heatmap = []
    for y in range(height):
        row = []
        for x in range(width):
            value = abs(x - width // 2) / (width // 2) * abs(y - height // 2) / (height // 2)
            value = min(value + random.random() * 0.3, 1.0)
            idx = min(int(value * len(chars)), len(chars) - 1)
            row.append(chars[idx])
        heatmap.append(row)
    return '\n'.join(''.join(row) for row in heatmap)

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

def generate_waves(width=40, height=10, seed=None):
    if seed is not None:
        random.seed(seed)

    waves = []
    for y in range(height):
        row = []
        for x in range(width):
            phase = (x / width * 4 * 3.14159) + (y / height * 3.14159)
            value = (math.sin(phase) + 1) / 2
            chars = " ▁▂▃▄▅▆▇█"
            idx = min(int(value * len(chars)), len(chars) - 1)
            row.append(chars[idx])
        waves.append(''.join(row))
    return '\n'.join(waves)


def generate_fractal_tree(width=40, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    def draw_branch(x, y, angle, length, depth):
        if depth == 0 or length < 1:
            return
        dx = int(length * math.cos(angle))
        dy = int(length * math.sin(angle))
        end_x, end_y = x + dx, y + dy
        if 0 <= end_x < width and 0 <= end_y < height:
            grid[end_y][end_x] = random.choice(['*', '✱', '✲', '∗'])
        draw_branch(end_x, end_y, angle - 0.5, length * 0.7, depth - 1)
        draw_branch(end_x, end_y, angle + 0.5, length * 0.7, depth - 1)

    start_x, start_y = width // 2, height - 1
    draw_branch(start_x, start_y, -math.pi / 2, height // 2, 5)
    
    return '\n'.join(''.join(row) for row in grid)

def generate_sierpinski(width=32, height=16, seed=None):
    if seed is not None:
        random.seed(seed)

    triangle = [[' ' for _ in range(width)] for _ in range(height)]
    
    def fill_triangle(x1, y1, x2, y2, x3, y3):
        if abs(x2 - x1) < 2:
            return
        mid1_x, mid1_y = (x1 + x2) // 2, (y1 + y2) // 2
        mid2_x, mid2_y = (x1 + x3) // 2, (y1 + y3) // 2
        mid3_x, mid3_y = (x2 + x3) // 2, (y2 + y3) // 2
        
        for dy in range(min(y1, y2, y3), max(y1, y2, y3)):
            for dx in range(min(x1, x2, x3), max(x1, x2, x3)):
                if abs(dx - mid1_x) + abs(dy - mid1_y) < abs(mid2_x - mid1_x):
                    triangle[dy][dx] = ' '
                else:
                    triangle[dy][dx] = '█'
        
        fill_triangle(x1, y1, mid1_x, mid1_y, mid2_x, mid2_y)
        fill_triangle(mid1_x, mid1_y, x2, y2, mid3_x, mid3_y)
        fill_triangle(mid2_x, mid2_y, mid3_x, mid3_y, x3, y3)

    def sierpinski_iterative(size, cy):
        row_len = size
        for y in range(cy, cy + size):
            if y < height:
                start = (size - (y - cy + 1)) // 2
                for x in range(start, start + (y - cy + 1)):
                    if x < width:
                        triangle[y][x] = random.choice(['▓', '▒', '░', '█'])
                for x in range(start + (y - cy + 1), start + 2 * (y - cy + 1)):
                    if x < width:
                        triangle[y][x] = ' '

    tier1_size = height - 2
    sierpinski_iterative(tier1_size, 1)
    
    return '\n'.join(''.join(row) for row in triangle)


def generate_cellular_automaton(width=40, height=20, rule=30, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = []
    row = [' ' for _ in range(width)]
    row[width // 2] = '█'
    grid.append(row)

    for _ in range(height - 1):
        new_row = [' ' for _ in range(width)]
        for x in range(width):
            left = grid[-1][(x - 1) % width]
            center = grid[-1][x]
            right = grid[-1][(x + 1) % width]
            pattern = (left == '█', center == '█', right == '█')
            idx = (pattern[0] << 2) | (pattern[1] << 1) | pattern[2]
            if (rule >> idx) & 1:
                new_row[x] = random.choice(['█', '▓', '▒'])
        grid.append(new_row)

    return '\n'.join(''.join(row) for row in grid)


def generate_stars(width=40, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    chars = " .✦✧⋆∗✶✷✸✹✺✻✼❖"
    stars = []
    for y in range(height):
        row = []
        for x in range(width):
            value = random.random()
            idx = min(int(value * len(chars)), len(chars) - 1)
            row.append(chars[idx])
        stars.append(''.join(row))
    return '\n'.join(stars)


def generate_diamond(width=21, height=11, seed=None):
    if seed is not None:
        random.seed(seed)

    diamond = []
    center_x = width // 2
    for y in range(height):
        row = []
        for x in range(width):
            dist = abs(x - center_x) + abs(y - height // 2)
            max_dist = height // 2
            if dist <= max_dist:
                row.append(random.choice(['◆', '◇', '○', '●']))
            else:
                row.append(' ')
        diamond.append(row)
    return '\n'.join(''.join(row) for row in diamond)


def generate_concentric_circles(width=40, height=20, seed=None):
    if seed is not None:
        random.seed(seed)

    circles = []
    center_x, center_y = width // 2, height // 2
    max_radius = min(center_x, center_y)

    for y in range(height):
        row = []
        for x in range(width):
            dist = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            ring = int(dist / max_radius * 6)
            chars = " .○◌●◉"
            idx = min(ring, len(chars) - 1)
            row.append(chars[idx])
        circles.append(''.join(row))
    return '\n'.join(circles)


def generate_rosette(width=33, height=17, seed=None):
    if seed is not None:
        random.seed(seed)

    rosette = []
    center_x, center_y = width // 2, height // 2
    chars = "✿❀❁✾❃❋✦✧⋆⭒"

    for y in range(height):
        row = []
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            dist = (dx * dx + dy * dy) ** 0.5
            angle = math.atan2(dy, dx)
            pattern_val = (dist / 3 + angle * 2) % (len(chars) * 1.5)
            if int(pattern_val) < len(chars):
                row.append(chars[int(pattern_val)])
            elif dist < min(center_x, center_y) * 0.9:
                row.append(random.choice(['❀', '✿', '❁']))
            else:
                row.append(' ')
        rosette.append(row)
    return '\n'.join(''.join(row) for row in rosette)


def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] AI Playground v1.7")
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
    elif mode == "heatmap":
        for i in range(count):
            print(f"\n--- Heatmap {i+1} ---")
            print(generate_heatmap(seed=i))
    elif mode == "banner":
        text = sys.argv[2] if len(sys.argv) > 2 else "Hello World"
        for i in range(count):
            print(f"\n--- Banner {i+1} ---")
            print(generate_banner(text, seed=i))
    elif mode == "waves":
        for i in range(count):
            print(f"\n--- Waves {i+1} ---")
            print(generate_waves(seed=i))
    elif mode == "tree":
        for i in range(count):
            print(f"\n--- Fractal Tree {i+1} ---")
            print(generate_fractal_tree(seed=i))
    elif mode == "sierpinski":
        for i in range(count):
            print(f"\n--- Sierpinski Triangle {i+1} ---")
            print(generate_sierpinski(seed=i))
    elif mode == "automaton":
        for i in range(count):
            print(f"\n--- Cellular Automaton {i+1} ---")
            print(generate_cellular_automaton(seed=i))
    elif mode == "diamond":
        for i in range(count):
            print(f"\n--- Diamond {i+1} ---")
            print(generate_diamond(seed=i))
    elif mode == "rosette":
        for i in range(count):
            print(f"\n--- Rosette {i+1} ---")
            print(generate_rosette(seed=i))
    elif mode == "circles":
        for i in range(count):
            print(f"\n--- Concentric Circles {i+1} ---")
            print(generate_concentric_circles(seed=i))
    elif mode == "stars":
        for i in range(count):
            print(f"\n--- Stars {i+1} ---")
            print(generate_stars(seed=i))
    else:
        for i in range(count):
            pattern = generate_pattern(seed=i)
            print(f"{i+1:3d}: {pattern}")

    print("-" * 40)
    print("Generation complete!")

if __name__ == "__main__":
    main()