import noise
import numpy as np
import time
import random

# Set up the Perlin noise generator
np.random.seed(int(time.time()))

def perlinNoise():
    octaves = 5
    persistence = 0.5
    lacunarity = 2.0
    scale = 10.0

    OBJECTS = {
        "bush": [2, 17, 24, 34, 40, 44],
        "sky": [48, 49, 52, 53],
        "cloud": [5, 13, 26, 32, 42, 55],
        "pipe": [(8, 10), (12, 12), (22, 12), (29, 9)],
        "ground": list(range(40, 60))
    }

    def generate_perlin_noise(x, y):
        value = 0
        for i in range(octaves):
            frequency = lacunarity ** i
            amplitude = persistence ** i
            value += noise.snoise2(x * frequency / scale, y * frequency / scale, octaves=i + 1) * amplitude
        return value

    pip_coordinates = []
    for x, y in OBJECTS["pipe"]:
        x_noise = generate_perlin_noise(x, y)
        y_noise = generate_perlin_noise(x + 1000, y + 1000)
        height_noise = generate_perlin_noise(x + 2000, y + 2000)
        
        x_factor = 10  # Increase this value for more variation
        x_coord = max(6, x + round(x_noise * x_factor))
        y_coord = min(max(9, y + round(y_noise * 5)), 12) 
        height = round(height_noise * 2 + 4)
       
            
        pip_coordinates.append([x_coord, y_coord, height])

    PIPES = {"pipe": pip_coordinates}
    return PIPES
