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


def generate_rainbow(width=40, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    colors = "红橙黄绿青蓝紫"
    rainbow = []
    for y in range(height):
        row = []
        for x in range(width):
            dist = abs(x - width // 2)
            band = int(dist / (width // 2) * 7)
            band = min(band, 6 - band)
            idx = min(int(abs(y - height // 2) / (height // 2) * len(colors)), len(colors) - 1)
            if y >= height // 2 - band and y <= height // 2 + band:
                row.append(colors[min(band, len(colors) - 1)])
            else:
                row.append(' ')
        rainbow.append(''.join(row))
    return '\n'.join(rainbow)


def generate_fireworks(width=40, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    num_explosions = random.randint(2, 4)

    for _ in range(num_explosions):
        cx = random.randint(width // 4, 3 * width // 4)
        cy = random.randint(height // 4, 3 * height // 4)
        radius = random.randint(3, 6)
        color = random.choice(['✿', '❀', '❁', '✸', '✹', '✺'])

        for y in range(height):
            for x in range(width):
                dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
                if dist <= radius:
                    grid[y][x] = color

    return '\n'.join(''.join(row) for row in grid)


def generate_checkerboard(width=20, height=10, seed=None):
    if seed is not None:
        random.seed(seed)

    board = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x + y) % 2 == 0:
                row.append(random.choice(['█', '▓', '▒']))
            else:
                row.append(random.choice(['░', '▒', '▓']))
        board.append(''.join(row))
    return '\n'.join(board)


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


def generate_heart(width=21, height=11, seed=None):
    if seed is not None:
        random.seed(seed)

    heart = []
    for y in range(height):
        row = []
        for x in range(width):
            dx = abs(x - width // 2)
            dy = y - height // 2 + 2
            if dx * dx + dy * dy <= 12:
                row.append(random.choice(['♥', '❤', '❥']))
            else:
                row.append(' ')
        heart.append(''.join(row))
    return '\n'.join(heart)


def generate_hexagon(width=25, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    hexagon = []
    center_x = width // 2
    for y in range(height):
        row = []
        dist_from_center = abs(y - height // 2)
        row_width = height - dist_from_center
        start_x = center_x - row_width // 2
        for x in range(width):
            if start_x <= x < start_x + row_width:
                row.append(random.choice(['⬡', '⬢', '◈', '◉']))
            else:
                row.append(' ')
        hexagon.append(''.join(row))
    return '\n'.join(hexagon)


def generate_tunnel(width=40, height=20, seed=None):
    if seed is not None:
        random.seed(seed)

    tunnel = []
    center_x, center_y = width // 2, height // 2
    chars = " .·:;+*#@█"
    for y in range(height):
        row = []
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            dist = (dx * dx + dy * dy) ** 0.5
            max_dist = ((width // 2) ** 2 + (height // 2) ** 2) ** 0.5
            value = dist / max_dist
            idx = min(int(value * len(chars)), len(chars) - 1)
            angle = math.atan2(dy, dx)
            if abs(dx) < 2 or abs(dy) < 2:
                row.append(random.choice(['║', '╔', '╗', '╚', '╝', '═']))
            else:
                row.append(chars[idx])
        tunnel.append(''.join(row))
    return '\n'.join(tunnel)


def generate_dna_helix(width=40, height=20, seed=None):
    if seed is not None:
        random.seed(seed)

    helix = []
    chars = "ATCG"
    base_pairs = "─═┄┅"
    
    for y in range(height):
        row = []
        phase = y / height * 4 * math.pi
        offset = int(math.sin(phase) * (width // 3))
        
        for x in range(width):
            center_dist = abs(x - width // 2)
            relative_pos = (x + offset - width // 2)
            
            if center_dist < 2:
                if relative_pos < 0:
                    row.append(random.choice(['╭', '╮']))
                else:
                    row.append(random.choice(['╯', '╰']))
            elif center_dist < width // 3:
                if (x + offset) % 4 == 0:
                    row.append(random.choice(list(chars)))
                elif (x + offset + 2) % 4 == 0:
                    row.append(random.choice(list(chars)))
                elif (x + offset) % 2 == 0:
                    idx = min(int(center_dist / (width // 3) * len(base_pairs)), len(base_pairs) - 1)
                    row.append(base_pairs[idx])
                else:
                    row.append(' ')
            else:
                row.append(' ')
        helix.append(''.join(row))
    
    return '\n'.join(helix)


def generate_snowflake(size=15, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(size)] for _ in range(size)]
    center = size // 2

    for y in range(size):
        for x in range(size):
            dx, dy = x - center, y - center
            dist = (dx * dx + dy * dy) ** 0.5
            if dist < 1:
                grid[y][x] = random.choice(['*', '✱', '✲'])
            elif dist < 3:
                grid[y][x] = random.choice(['❄', '❅', '❆', '✦'])
            elif int(dist) % 2 == 0:
                grid[y][x] = random.choice(['·', '•', '◦'])

    for i in range(center):
        grid[center - i][center] = '│'
        grid[center + i][center] = '│'
        grid[center][center - i] = '─'
        grid[center][center + i] = '─'
        if i < center // 2:
            grid[center - i][center - i] = '┌'
            grid[center - i][center + i] = '┐'
            grid[center + i][center - i] = '└'
            grid[center + i][center + i] = '┘'

    return '\n'.join(''.join(row) for row in grid)


def generate_pyramid(width=31, height=9, seed=None):
    if seed is not None:
        random.seed(seed)

    pyramid = []
    for y in range(height):
        row = []
        indent = height - y - 1
        stars = y * 2 + 1
        for x in range(width):
            if x < indent or x >= indent + stars:
                row.append(' ')
            else:
                row.append(random.choice(['▲', '△', '◢', '◣']))
        pyramid.append(''.join(row))
    return '\n'.join(pyramid)


def generate_galaxy(width=41, height=21, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width // 2, height // 2
    stars = "✨✦✧⋆⭒✶✷⸝⸞⸟"

    for y in range(height):
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            dist = (dx * dx + dy * dy) ** 0.5
            if dist < 1:
                grid[y][x] = random.choice(['☉', '☀', '◉'])
            elif dist < 4:
                grid[y][x] = random.choice(['✸', '✹', '❂'])
            elif dist < 8:
                angle = math.atan2(dy, dx)
                spiral = (angle + dist / 3) % (2 * math.pi)
                if int(spiral * 3) % 2 == 0:
                    grid[y][x] = random.choice(list(stars))
            else:
                value = random.random()
                if value < 0.1:
                    grid[y][x] = random.choice(list(stars))

    for arm in range(3):
        angle_offset = arm * (2 * math.pi / 3)
        for r in range(2, min(center_x, center_y) - 1):
            x = int(center_x + r * math.cos(angle_offset + r * 0.15))
            y = int(center_y + r * math.sin(angle_offset + r * 0.15))
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = random.choice(['✧', '✦', '✶'])

    return '\n'.join(''.join(row) for row in grid)


def generate_spider_web(width=41, height=21, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width // 2, height // 2
    max_radius = min(center_x, center_y)

    for y in range(height):
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            dist = (dx * dx + dy * dy) ** 0.5
            angle = math.atan2(dy, dx) if dist > 0 else 0
            if dist < 1:
                grid[y][x] = '●'
            elif int(dist) % 3 == 0:
                grid[y][x] = '○'
            elif abs(math.sin(angle * 6)) < 0.3:
                grid[y][x] = '│' if abs(dx) > abs(dy) else '─'
            elif dist < max_radius * 0.8:
                grid[y][x] = random.choice(['◌', '◎', '○'])

    for i in range(0, center_x, 4):
        for dy in range(-i, i + 1):
            for dx in range(-i, i + 1):
                if dx * dx + dy * dy == i * i:
                    x, y = center_x + dx, center_y + dy
                    if 0 <= x < width and 0 <= y < height:
                        grid[y][x] = '●'

    return '\n'.join(''.join(row) for row in grid)


def generate_vortex(width=40, height=20, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width // 2, height // 2
    arms = random.randint(3, 6)
    chars = "◉●○◌◎◐◑◒◓"

    for y in range(height):
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            dist = (dx * dx + dy * dy) ** 0.5
            if dist < 1:
                grid[y][x] = random.choice(['☉', '☀', '★'])
            else:
                angle = math.atan2(dy, dx)
                spiral = (angle + dist * 0.3) % (2 * math.pi)
                arm_idx = int(spiral / (2 * math.pi) * arms)
                intensity = int(dist * 2) % len(chars)
                if dist < min(center_x, center_y) * 0.9:
                    grid[y][x] = chars[intensity]

    return '\n'.join(''.join(row) for row in grid)


def generate_kaleidoscope(width=40, height=20, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width // 2, height // 2
    segments = random.randint(6, 12)
    colors = "🟢🔵🟣🔴🟠🟡🟤⚫⚪"

    for y in range(height):
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            dist = (dx * dx + dy * dy) ** 0.5
            angle = math.atan2(dy, dx) if dist > 0 else 0
            normalized_angle = (angle + math.pi) / (2 * math.pi)
            segment = int(normalized_angle * segments) % segments
            pattern_val = (dist / 2 + segment * 0.5) % 3
            if dist < 2:
                grid[y][x] = random.choice(['★', '✦', '✧'])
            elif int(pattern_val) == 0:
                grid[y][x] = random.choice(['◈', '◉', '◊'])
            elif int(pattern_val) == 1:
                grid[y][x] = random.choice(['❖', '✿', '❀'])
            else:
                if dist < min(center_x, center_y) * 0.8:
                    grid[y][x] = random.choice(list('▓▒░'))

    return '\n'.join(''.join(row) for row in grid)


def generate_clouds(width=40, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    chars = " .☁️☁️☁️"

    for y in range(height):
        for x in range(width):
            noise = random.random()
            if noise < 0.1:
                grid[y][x] = chars[0]
            elif noise < 0.3:
                grid[y][x] = random.choice(['☁', '☁'])
            elif noise < 0.5:
                grid[y][x] = random.choice(['☁️'])
            else:
                grid[y][x] = ' '

    return '\n'.join(''.join(row) for row in grid)


def generate_constellation(width=40, height=20, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    stars = []
    num_stars = random.randint(8, 15)

    for _ in range(num_stars):
        sx = random.randint(1, width - 2)
        sy = random.randint(1, height - 2)
        stars.append((sx, sy))
        grid[sy][sx] = random.choice(['*', '✦', '✧', '⋆'])

    for i in range(len(stars) - 1):
        x1, y1 = stars[i]
        x2, y2 = stars[i + 1]
        dx, dy = x2 - x1, y2 - y1
        steps = max(abs(dx), abs(dy))
        if steps > 0:
            for step in range(steps):
                t = step / steps
                cx = int(x1 + t * dx)
                cy = int(y1 + t * dy)
                if 0 <= cx < width and 0 <= cy < height:
                    if grid[cy][cx] == ' ':
                        grid[cy][cx] = random.choice(['·', '•', '◦', '⁚'])

    return '\n'.join(''.join(row) for row in grid)


def generate_coral(width=40, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    chars = "✿❀❁❃❋⸶⸷◐◑"

    for y in range(height):
        for x in range(width):
            phase = x / width * 2 * math.pi + y / height * math.pi
            intensity = (math.sin(phase) + 1) / 2
            if intensity > 0.3 and random.random() > 0.4:
                grid[y][x] = random.choice(list(chars))

    for _ in range(3):
        cx, cy = random.randint(0, width), random.randint(0, height)
        for dy in range(-3, 4):
            for dx in range(-3, 4):
                if 0 <= cx + dx < width and 0 <= cy + dy < height:
                    if abs(dx) + abs(dy) < 4:
                        grid[cy + dy][cx + dx] = random.choice(['🪸', '🪷', '🔴', '🟠'])

    return '\n'.join(''.join(row) for row in grid)


def generate_cherry_blossom(width=40, height=15, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    chars = "✿❀❁❃✸✹❋"

    for y in range(height):
        for x in range(width):
            phase = x / width * 3 * math.pi + y / height * 2 * math.pi
            intensity = (math.sin(phase) + 1) / 2
            if intensity > 0.4 and random.random() > 0.5:
                grid[y][x] = random.choice(list(chars))

    for _ in range(4):
        cx, cy = random.randint(2, width - 3), random.randint(2, height - 3)
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if 0 <= cx + dx < width and 0 <= cy + dy < height:
                    if abs(dx) + abs(dy) < 3:
                        grid[cy + dy][cx + dx] = random.choice(['❀', '✿', '❁', '❃'])

    return '\n'.join(''.join(row) for row in grid)


def generate_lotus(width=41, height=17, seed=None):
    if seed is not None:
        random.seed(seed)

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width // 2, height // 2

    for y in range(height):
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            dist = (dx * dx + dy * dy) ** 0.5
            angle = math.atan2(dy, dx) if dist > 0 else 0
            petal_angle = abs(math.sin(angle * 3))
            if dist < 3:
                grid[y][x] = random.choice(['✿', '❀', '❁'])
            elif dist < 7 and petal_angle > 0.3:
                grid[y][x] = random.choice(['❃', '❋', '✾'])
            elif dist < 9 and petal_angle > 0.5:
                grid[y][x] = random.choice(['⸝', '⸞', '⸟'])

    for r in range(2, 6):
        y = center_y + r
        if y < height:
            grid[y][center_x] = '│'

    return '\n'.join(''.join(row) for row in grid)


def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] AI Playground v2.0")
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
    elif mode == "rainbow":
        for i in range(count):
            print(f"\n--- Rainbow {i+1} ---")
            print(generate_rainbow(seed=i))
    elif mode == "checkerboard":
        for i in range(count):
            print(f"\n--- Checkerboard {i+1} ---")
            print(generate_checkerboard(seed=i))
    elif mode == "fireworks":
        for i in range(count):
            print(f"\n--- Fireworks {i+1} ---")
            print(generate_fireworks(seed=i))
    elif mode == "heart":
        for i in range(count):
            print(f"\n--- Heart {i+1} ---")
            print(generate_heart(seed=i))
    elif mode == "hexagon":
        for i in range(count):
            print(f"\n--- Hexagon {i+1} ---")
            print(generate_hexagon(seed=i))
    elif mode == "pyramid":
        for i in range(count):
            print(f"\n--- Pyramid {i+1} ---")
            print(generate_pyramid(seed=i))
    elif mode == "tunnel":
        for i in range(count):
            print(f"\n--- Tunnel {i+1} ---")
            print(generate_tunnel(seed=i))
    elif mode == "snowflake":
        for i in range(count):
            print(f"\n--- Snowflake {i+1} ---")
            print(generate_snowflake(seed=i))
    elif mode == "galaxy":
        for i in range(count):
            print(f"\n--- Galaxy {i+1} ---")
            print(generate_galaxy(seed=i))
    elif mode == "spider":
        for i in range(count):
            print(f"\n--- Spider Web {i+1} ---")
            print(generate_spider_web(seed=i))
    elif mode == "vortex":
        for i in range(count):
            print(f"\n--- Vortex {i+1} ---")
            print(generate_vortex(seed=i))
    elif mode == "kaleidoscope":
        for i in range(count):
            print(f"\n--- Kaleidoscope {i+1} ---")
            print(generate_kaleidoscope(seed=i))
    elif mode == "dna":
        for i in range(count):
            print(f"\n--- DNA Helix {i+1} ---")
            print(generate_dna_helix(seed=i))
    elif mode == "clouds":
        for i in range(count):
            print(f"\n--- Clouds {i+1} ---")
            print(generate_clouds(seed=i))
    elif mode == "coral":
        for i in range(count):
            print(f"\n--- Coral {i+1} ---")
            print(generate_coral(seed=i))
    elif mode == "constellation":
        for i in range(count):
            print(f"\n--- Constellation {i+1} ---")
            print(generate_constellation(seed=i))
    elif mode == "cherry":
        for i in range(count):
            print(f"\n--- Cherry Blossom {i+1} ---")
            print(generate_cherry_blossom(seed=i))
    elif mode == "lotus":
        for i in range(count):
            print(f"\n--- Lotus {i+1} ---")
            print(generate_lotus(seed=i))
    else:
        for i in range(count):
            pattern = generate_pattern(seed=i)
            print(f"{i+1:3d}: {pattern}")

    print("-" * 40)
    print("Generation complete!")

if __name__ == "__main__":
    main()