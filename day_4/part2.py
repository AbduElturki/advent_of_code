#[1518-10-14 00:05] falls asleep
#[1518-09-13 00:12] falls asleep
#[1518-03-23 00:26] falls asleep
from collections import defaultdict
import operator
import math
import parse

def get_time(line):
    split = line.split()
    time = split[1][:-1]
    return int(time.split(':')[1])

def main():
    with open('input') as f:
        lines = f.read().splitlines()
    lines.sort()
    guard_sleep_freq = defaultdict(int)

    guard = None
    asleep = None
    
    for line in lines:
        time = get_time(line)
        if "begins shift" in line:
            guard = int(line.split()[3][1:]) 
            asleep = None
        elif 'falls asleep' in line:
            asleep = time 
        elif 'wakes up' in line:
            for i in range(asleep, time):
                guard_sleep_freq[(guard,i)] += 1
    gaurd_most_freq, freq = max(guard_sleep_freq.items(), key=operator.itemgetter(1))[0] 

    print("Guard: " + str(gaurd_most_freq))
    print("Frequency: " + str(freq))
    print("Answer: " + str(gaurd_most_freq * freq))
main()
