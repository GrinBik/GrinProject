from itertools import combinations 

inp = "HACK 2"

string , k = inp.split()

line = list(string)

line.sort()
for i in range(int(k)):
    variants = (list(combinations(line, i + 1)))
    variants.sort()
    for element in variants:
    	print("".join(element))