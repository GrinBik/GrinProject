from itertools import combinations_with_replacement

string = input().split()

line = list(string[0])

line.sort()

combinations = list(combinations_with_replacement(line, int(string[1])))

for elem in combinations:
	print(''.join(elem))