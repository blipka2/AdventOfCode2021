# Part One

import itertools
import collections

def entryToArr(test=False):
    if test:
        entry = open('test.txt', 'r')
    else:
        entry = open('entry.txt', 'r')
    lines = entry.readlines()

    coords = []

    for l in lines:
        x1 = int(l[:l.find(',')])
        y1 = int(l[l.find(',')+1:l.find('-')])
        sub_l = l[l.find('>')+1:]
        x2 = int(sub_l[:sub_l.find(',')])
        y2 = int(sub_l[sub_l.find(',')+1:])
        coords.append([x1,y1,x2,y2])
    
    return coords 

def reverseElements(tupleList):
    return [[t[0][::-1] for t in tupleList]]

def allUniquePairs(xRange, yRange):
    uniquePairs = []
    if len(yRange) == 1:
        perms = itertools.permutations(xRange, len(yRange))
        
        for pair in perms:
            zipped = zip(pair, yRange)
            uniquePairs.append(list(zipped))
        return uniquePairs
    elif len(xRange) == 1:
        perms = itertools.permutations(yRange, len(xRange))
        
        for pair in perms:
            zipped = zip(pair, xRange)
            uniquePairs.append(list(zipped))
        return reverseElements(uniquePairs)
    # Part Two modification
    elif xRange == yRange:
        return [[(i, i)] for i in xRange]

def diagonalCoords(x1, y1, x2, y2):
    coords = []
    if x1 < x2 and y1 < y2:
        while x1 <= x2 and y1 <= y2:
            coords.append([(x1, y1)])
            x1 += 1
            y1 += 1
    elif x1 > x2 and y1 < y2:
        while x1 >= x2 and y1 <= y2:
            coords.append([(x1, y1)])
            x1 -= 1
            y1 += 1
    elif x1 < x2 and y1 > y2:
        while x1 <= x2 and y1 >= y2:
            coords.append([(x1, y1)])
            x1 += 1
            y1 -= 1
    elif x1 > x2 and y1 > y2:
        while x1 >= x2 and y1 >= y2:
            coords.append([(x1, y1)])
            x1 -= 1
            y1 -= 1
    return coords

def getAllCoords(entry):
    allCoords = []
    for coords in entry:
        # only account horizontal and vertical lines
        if coords[0] != coords[2] and coords[1] != coords[3]:
            allCoords.extend(diagonalCoords(coords[0], coords[1], coords[2], coords[3]))
        if coords[0] == coords[2] or coords[1] == coords[3]:
            # print(coords)
            allCoordsAdd = []
            xMin = min(coords[0], coords[2])
            xMax = max(coords[0], coords[2])
            yMin = min(coords[1], coords[3])
            yMax = max(coords[1], coords[3])

            xRange = list(range(xMin, xMax+1))
            yRange = list(range(yMin, yMax+1))

            for line in allUniquePairs(xRange, yRange):
                # print(line)
                for pair in line:
                    if pair not in allCoordsAdd:
                        # allCoordsAdd.append(pair)
                        allCoords.append([pair])

            # allCoords.extend(allCoordsAdd) 
            # allCoords.extend(allUniquePairs(xRange, yRange))
    
    return allCoords

def countDupes(allCoords):
    count = collections.Counter(elem[0] for elem in allCoords)
    #return count
    return sum(1 for k, v in count.items() if v > 1)

# Part One
# assert countDupes(getAllCoords(entryToArr(test=True))) == 5
# Part Two
assert countDupes(getAllCoords(entryToArr(test=True))) == 12
countDupes(getAllCoords(entryToArr()))

