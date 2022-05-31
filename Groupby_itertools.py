from itertools import groupby

string = list(map(int, input()))

result = []

for i,j in groupby(string):
    temp_tuple = (len(list(j)) , i)
    result.append(temp_tuple)

for elem in result:
    print(elem, end = ' ')