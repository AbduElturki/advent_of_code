import collections

def main():
    with open('input') as f:
        lines = f.read().splitlines()
    twos = 0
    threes = 0
    for line in lines:
        collec = collections.defaultdict(int)
        for c in line:
            collec[c] += 1
        if 2 in list(collec.values()):
            twos += 1
        if 3 in list(collec.values()):
            threes += 1
    print("Twos: " + str(twos))
    print("Threes: " + str(threes))
    checksum = twos * threes
    print("Checksum: " + str(checksum))

main()
            

