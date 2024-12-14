import re

robots = open("input.txt").read().splitlines()
width, height = 101, 103
t = 100

width_mid = width/2 - 0.5
height_mid = height/2 - 0.5
q1, q2, q3, q4 = 0, 0, 0, 0

for robot in robots:
    match = re.search(r"p=(.+) v=(.+)", robot)
    x,y = tuple(map(int, match.group(1).split(',')))
    dx,dy = tuple(map(int, match.group(2).split(',')))

    nx = (x + dx*t) % width
    ny = (y + dy*t) % height

    if nx < width_mid and ny < height_mid:
        q1 += 1
    elif nx > width_mid and ny < height_mid:
        q2 += 1
    elif nx < width_mid and ny > height_mid:
        q3 += 1
    elif nx > width_mid and ny > height_mid:
        q4 += 1

print(q1*q2*q3*q4)
