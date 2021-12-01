def entryToArr():
    entry = open('entry.txt', 'r')
    lines = entry.readlines()

    depths = []

    for l in lines:
        depths.append(int(l.strip()))

    return depths

def depthIncreases(entry):
    counter = 0
    if len(entry) <= 1: 
        return counter
    else:
        for i in range(0, len(entry) - 1):
            if entry[i] < entry[i + 1]:
                counter += 1
    return counter

assert depthIncreases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

depthIncreases(entryToArr())
