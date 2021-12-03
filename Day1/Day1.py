# Part One

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
        for i in range(len(entry) - 1):
            if entry[i] < entry[i + 1]:
                counter += 1
    return counter

assert depthIncreases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

depthIncreases(entryToArr())

# Part Two

def getWindow(entry, pos):
    return entry[pos] + entry[pos - 1] + entry[pos - 2]

def windowIncreases(entry):
    counter = 0
    previousWindow = getWindow(entry, 2)
    for i in range(3, len(entry)):
        curWindow = getWindow(entry, i)
        if curWindow > previousWindow:
            counter += 1
        previousWindow = curWindow
    return counter

assert windowIncreases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5

windowIncreases(entryToArr())
