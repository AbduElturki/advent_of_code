import numpy as np
import parse

def main():
    with open('input') as f:
        lines = f.read().splitlines()
    claim_matcher = '''#{id:d} @ {x:d},{y:d}: {width:d}x{height:d}'''
    fabric = np.zeros((1000, 1000), dtype=np.int)

    for line in lines:
        r = parse.parse(claim_matcher, line)
        claim = fabric[r['y']: r['y'] + r['height'], r['x']: r['x'] + r['width']]
        claim[:] = claim + 1
    print(np.sum(np.where(fabric > 1, 1, 0)))
main()
