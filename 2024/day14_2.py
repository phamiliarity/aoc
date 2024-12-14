import re
import itertools

def calculate_avg_pairwise_distance(robot_positions):
    tot_dist = []
    for a,b in itertools.combinations(robot_positions, 2):
        (x1, y1), (x2, y2) = a, b
        dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        tot_dist.append(dist)
    return sum(tot_dist)/len(tot_dist)

robots = open("input.txt").read().splitlines()
width, height = 101, 103
time_range = range(7000, 8000) #kinda cheesed this. determined the range by submitting random values to get a "this number is too low/high!" message. technically i couldve tried range(0, 10000) and brewed a nice cup of tea in the mean time?

min_avg_dist = float("inf")
min_t = 0
for t in time_range:
    robot_positions = []
    for robot in robots:
        match = re.search(r"p=(.+) v=(.+)", robot)
        x,y = tuple(map(int, match.group(1).split(',')))
        dx,dy = tuple(map(int, match.group(2).split(',')))

        nx = (x + dx*t) % width
        ny = (y + dy*t) % height

        robot_positions.append((nx, ny))
    avg_dist = calculate_avg_pairwise_distance(robot_positions)

    """
    assumption: robots are in closest proximity to each other when they form a
    christmas tree than when they are not in tree formation - i.e. random
    positions?
    """

    if avg_dist < min_avg_dist:
        min_avg_dist = avg_dist
        min_t = t

print(min_t)
