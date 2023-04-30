import random

def mapGen(num_platforms):
    # Define map dimensions
    MAP_WIDTH = 60
    MAP_HEIGHT = 10

    # Generate a block of 0s
    map = [[0 for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

    # Set random seed
    random.seed()

    # Randomly select an index from (0,5) to (0,9) and set it to 1
    y = random.randint(5, 9)
    x = 0
    map[x][y] = 1
    last_direction = None
    num_gaps = 0

    # Keep adding 1's to left, right and up until you reach the other side (index x == 59)
    while x < MAP_WIDTH - 1:
        # Determine possible directions to add 1
        possible_directions = []
        if x < MAP_WIDTH - 1 and map[x+1][y] == 0:
            possible_directions.append('right')
        if y > 3 and map[x][y-1] == 0 and last_direction != 'up':
            possible_directions.append('up')
        if y < MAP_HEIGHT - 1 and map[x][y+1] == 0 and last_direction != 'down':
            possible_directions.append('down')
        
        # Choose a random direction from possible directions
        if possible_directions:
            direction = random.choice(possible_directions)
            if direction == 'right':
                x += 1
                last_direction = 'right'
            elif direction == 'up':
                y -= 1
                last_direction = 'up'
            elif direction == 'down':
                y += 1
                last_direction = 'down'
            map[x][y] = 1
            
            # Check if there are four 1's directly atop of each other
            if y > 2 and map[x][y-1] == 1 and map[x][y-2] == 1 and map[x][y-3] == 1:
                # Remove the last 1 and break out of the loop
                map[x][y] = 0
                break
        else:
            # Break out of the loop if there are no possible directions
            break

        # Generate gaps between platforms
        if num_gaps < 2:
            gap = random.randint(1, 3)
            if map[x][y] == 1:
                for i in range(gap):
                    if y > 3:
                        y -= 1
                        map[x][y] = 0
                num_gaps += 1

    # Convert the cells with 1 into a list of indexes
    indexes = []
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map[x][y] == 1:
                indexes.append((x, y))

    # Print the map and indexes
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            print(map[x][y], end="")
        print()

    return indexes[:num_platforms]

platforms = mapGen(num_platforms=5)
print(platforms)