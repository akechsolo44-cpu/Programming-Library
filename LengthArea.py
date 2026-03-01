length = 4
width = 3
height = 3

wall_area = 2 * (length + width) * height
paint_coverage_per_can = 10

import math
cans_needed = math.ceil(wall_area / paint_coverage_per_can)

print(f"Total wall area: {wall_area} m²")
print(f"Paint cans needed: {cans_needed}")