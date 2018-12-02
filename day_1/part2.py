import itertools

def main():
    with open('input') as f:
        freq = f.read().splitlines()
    freq = [int(x) for x in freq]
    current = 0
    seen = {0}
    for change in itertools.cycle(freq):
        result = current + change
        print(result)
        if result in seen:
            break
        else:
            current = result
            seen.add(result)
    print(result)

main()
