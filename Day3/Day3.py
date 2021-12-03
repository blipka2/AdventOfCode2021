# Part One

def entryToArr():
    entry = open('entry.txt', 'r')
    lines = entry.readlines()

    diagnostics = []

    for l in lines:
        diagnostics.append(l.strip())

    return diagnostics

def majorityBit(sum, length, part): 
    if sum / length > 0.5:
        return 1
    elif sum / length < 0.5:
        return 0
    else:
        if part == 1:
            return 1
        elif part == 2:
            return 0.5

def getGamma(entry, part):
    sums = [ sum(int(row[i]) for row in entry) for i in range(len(entry[0])) ]
    return [majorityBit(i, len(entry), 1) for i in sums]

def getEpsilon(gamma):
    return [1 - i for i in gamma]

def binaryToDec(bin):
    return int("".join(str(x) for x in bin), 2)

def getPower(entry):
    gamma = binaryToDec(getGamma(entry, 1))
    epsilon = binaryToDec(getEpsilon(getGamma(entry, 1)))
    return  gamma * epsilon

assert getPower(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']) == 198

getPower(entryToArr())

# Part Two

def bitCriteria(entry, key, o2):
    for i in range(len(key)):
        if key[i] == 0.5:
            if o2:
                key[i] = 1
            else:
                key[i] = 0
        entry = [e for e in entry if int(e[i]) == key[i]]
        # regen key w/ new values
        if o2:
            key = getGamma(entry, 2)
        else:
            key = getEpsilon(getGamma(entry, 2))
        if len(entry) == 1:
            break
    return binaryToDec(entry)

def getOxygen(entry):
    return bitCriteria(entry, getGamma(entry, 2), True)

def getCO2(entry):
    return bitCriteria(entry, getEpsilon(getGamma(entry, 2)), False)

def getLifeSupport(entry):
    return getOxygen(entry) * getCO2(entry)


assert getLifeSupport(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']) == 230

getLifeSupport(entryToArr())
