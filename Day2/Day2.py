# Part One

def entryToArr():
    entry = open('entry.txt', 'r')
    lines = entry.readlines()

    directions = []

    for l in lines:
        directions.append(l.strip())

    return directions

def getPosition(directions):
    horizontal = 0
    depth = 0
    for i in range(len(directions)):
        if 'forward' in directions[i]:
            horizontal += int(directions[i].split("forward",1)[1].strip())
        elif 'down' in directions[i]:
            depth += int(directions[i].split("down",1)[1].strip())
        elif 'up' in directions[i]:
            depth -= int(directions[i].split("up",1)[1].strip())
    return horizontal * depth

assert getPosition(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150

getPosition(entryToArr())

# Part Two

def getComplexPosition(directions):
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(directions)):
        if 'forward' in directions[i]:
            x = int(directions[i].split("forward",1)[1].strip())
            horizontal += x
            depth += aim * x
        elif 'down' in directions[i]:
            aim += int(directions[i].split("down",1)[1].strip())
        elif 'up' in directions[i]:
            aim -= int(directions[i].split("up",1)[1].strip())
    return horizontal * depth

assert getComplexPosition(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 900


getComplexPosition(entryToArr())
