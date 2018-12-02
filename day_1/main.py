def main():
    with open('input') as f:
        freq = f.read().splitlines()
    freq_with_carrier = [0] + [int(x) for x in freq]
    result = sum(freq_with_carrier)
    print(result)

main()
