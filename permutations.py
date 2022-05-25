from itertools import permutations

string , k = input().split(" ")

line = list(permutations(string, int(k)))

line.sort()

for i in line:
    print(''.join(i))