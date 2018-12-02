import math 

def remove_diff(indices, string):
    new_string = ""
    for i in range(len(string)):
        if i in indices:
            continue
        new_string += string[i]
    return new_string

def main():
    best = math.inf
    difference = []
    best_strings = [] 
    with open('input') as f:
        lines = f.read().splitlines()
    for line1 in lines:
        for line2 in lines:
            if line1 is line2:
                continue
            temp = [i for i in range(len(line1)) if line1[i] != line2[i]]
            if len(temp) < best:
                best = len(temp)
                difference = temp
                best_strings = [line1, line2]
                if best is 1:
                    break
    answer = remove_diff(difference, best_strings[0])
    print("Number differences: " + str(best))
    print("String 1: " + best_strings[0]) 
    print("String 2: " + best_strings[1]) 
    print("Answer: " + answer)
main()
            

