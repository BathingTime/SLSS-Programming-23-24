# Day 1: Trebuchet

def trebuchet(data):
    sum=0
    for line in data.splitlines():
        for posLine in range(len(line)):
            if line[posLine].isnumeric():
                current=int(line[posLine])*10
                break
        for posLine in range(len(line)-1,-1,-1):
            if line[posLine].isnumeric():
                current+=int(line[posLine])
                break
        sum+=current
    return sum

# Day 2: Cube Conundrum

def cubeConundrum(data):
    ...