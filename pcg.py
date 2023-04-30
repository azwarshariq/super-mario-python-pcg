import random
import json

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

# Create the level dictionary
level = {
    "objects": {      
            "bush": [[x, random.randint(8, 12)] for x in OBJECTS["bush"]],
            "sky": [[x, random.randint(0, 13)] for x in OBJECTS["sky"]],
            "cloud": [[x, random.randint(3, 7)] for x in OBJECTS["cloud"]],
            "pipe": OBJECTS["pipe"],
            "ground": [[x, 9] for x in OBJECTS["ground"]]
         },
    "layers": {
        layer: {
            "x": [0, WIDTH],
            "y": LAYERS[layer]
        } for layer in LAYERS
    },
    "entities": {
        entity: [
            pos for pos in ENTITIES[entity]
            if pos[1] <= LAYERS["ground"][0] - 1
        ] for entity in ENTITIES
    }
}



# Print the level dictionary

print(level)





#def writeLevel():
data = {
    "id":0,
    "length":60,
    "level": level
}

print("j\n\n", data)
# write the data to a JSON file
with open('levels\Level1-2.json', 'w') as f:
    json.dump(data, f)
