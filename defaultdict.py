import os
from collections import defaultdict

file_path = os.path.join(os.getcwd(), "defaultdict_input.txt")

group_A = defaultdict(list)

group_B = list()

index = 0

with open(file_path, "r", encoding = "utf-8") as file:

    n, m = map(int, file.readline().split())

    i = 1
    
    for line in file:

        string =line.strip()

        if i <= n:
            group_A[string].append(i)
        if n < i <= (n+m):
            group_B.append(string)

        i += 1

for elem in group_B:
    if elem in group_A:
        print(" ".join(map(str, group_A[elem])))
    else:
        print("-1")