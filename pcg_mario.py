import json
import numpy as np
from pipe import *
from ground import *

import time

def proceduralGeneration(levelName):
    # Set up the Perlin noise generator
    np.random.seed(int(time.time()))
    # Define the width and height of the level
    WIDTH = 60
    HEIGHT = 16

    # Define the list of possible objects
    OBJECTS = {
        "bush": [2, 17, 24, 34, 40, 44],
        "sky": [48, 49, 52, 53],
        "cloud": [5, 13, 26, 32, 42, 55],
        "pipe": [(8, 10, 4), (12, 12, 4), (22, 12, 4), (29, 9, 6)],
        "ground": list(range(40, 60))
    }

    # Define the list of layers and their y positions
    LAYERS = {
        "sky": [0, 13],
        "ground": [14, 16]
    }

    # Define the list of entities and their positions
    ENTITIES = {
        "CoinBox": [(4, 8), (42, 5), (56, 2)],
        "coinBrick": [(37, 9)],
        "coin": [(random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2)) for _ in range(30)],
        "Goomba": [(random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2)) for _ in range(3)],
        "Koopa": [(random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2)) for _ in range(4)],
        "RandomBox": [(random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2), random.choice(["RedMushroom", "GreenMushroom"])) for _ in range(2)]
    }

    # Define the initial state of the Game of Life cells randomly
    GAME_OF_LIFE_INITIAL_STATE = np.random.choice([0, 1], size=(HEIGHT, WIDTH), p=[0.2, 0.8])

    # Define the rules for the Game of Life
    def apply_rules(state):
        neighbors_count = np.zeros_like(state)
        for i in range(HEIGHT):
            for j in range(WIDTH):
                neighbors_count[i, j] = state[max(0, i-1):min(i+2, HEIGHT), max(0, j-1):min(j+2, WIDTH)].sum() - state[i, j]
        birth_mask = (neighbors_count == 3) & (state == 0)
        survive_mask = ((neighbors_count == 2) | (neighbors_count == 3)) & (state == 1)
        state = (birth_mask | survive_mask).astype(np.int8)
        return state

    # Run the Game of Life for a certain number of steps
    def run_game_of_life(initial_state, num_steps):
        state = initial_state
        for i in range(num_steps):
            state = apply_rules(state)
        return state


    #print("\n\nlololol\n\n\n",PIPES["pipe"])
    # Create the level dictionary
    PIPES = perlinNoise()
    print("hu",PIPES["pipe"])

    platform = mapGen(60)
    print(platform)

    MAX_COIN_Y_DIST = 3

    MAX_COIN_Y_DIST = 3  # maximum distance a coin box can be from the ground/pipe

    level = {
        "objects": {      
            "bush": [[x, random.randint(8, 12)] for x in OBJECTS["bush"]],
            "sky": [[x, random.randint(0, 13)] for x in OBJECTS["sky"]],
            "cloud": [[x, random.randint(3, 7)] for x in OBJECTS["cloud"]],
            "pipe": PIPES["pipe"],
            "ground": platform
        },
        "layers": {
            layer: {
                "x": [0, WIDTH],
                "y": LAYERS[layer]
            } for layer in LAYERS
        },
        "entities": {
            entity: [
                (pos[0] + 4, pos[1]) if entity in {"goomba", "koopa"} and pos[0] < 15 else pos
                for pos in ENTITIES[entity]
                if pos[1] <= LAYERS["ground"][0] - 1 and (
                    entity != "coin" or (
                        pos[1] <= max(pipe[1] for pipe in PIPES["pipe"]) + MAX_COIN_Y_DIST and
                        not any(abs(pos[0] - pipe[0]) < 1 and abs(pos[1] - pipe[1]) < 1 for pipe in PIPES["pipe"]) and
                        not any(abs(pos[0] - entity_pos[0]) < 1 and abs(pos[1] - entity_pos[1]) < 1 for entity_pos in ENTITIES[entity] if entity_pos != pos) and
                        not any(pipe[0] - 3 <= pos[0] <= pipe[0] + 3 for pipe in PIPES["pipe"])
                    )
                ) and (
                    entity != "coinbox" or (
                        pos[1] == LAYERS["ground"][0] - 3 or
                        any(abs(pos[0] - pipe[0]) < 1 and abs(pos[1] - pipe[1] - 2) < 1 for pipe in PIPES["pipe"])
                    )
                )
            ] for entity in ENTITIES
        }
    }



    # Print the level dictionary
    print(level)
    data = {
        "id":0,
        "length":60,
        "level": level
    }

    print("j\n\n", data)
    # write the data to a JSON file
    with open(levelName, 'w') as f:
        json.dump(data, f)



def main():
    proceduralGeneration('levels\Level 2.json')
    proceduralGeneration('levels\Level 3.json')
    proceduralGeneration('levels\Level 4.json')
    proceduralGeneration('levels\Level 5.json')
    proceduralGeneration('levels\Level 6.json')

if __name__ == "__main__":
    main()