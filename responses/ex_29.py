import math
def liquid_volume(height, radii = 10):
    return (4 * math.pi * radii**3/3) - (math.pi * height**2 *(3*radii - height)/3)

print(liquid_volume(height=2))