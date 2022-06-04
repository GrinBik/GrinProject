import os
from itertools import product

file_path = os.path.join(os.getcwd(), "test.txt")
with open(file_path) as f:
    
    k, m = list(map(int, f.readline().split()))
    
    arr = []
  
    for i in range(k):
        arr.append(list(map(int, f.readline().split()))[1:])
  
result = map(lambda x: sum(i**2 for i in x) % m, product(*arr))

print(max(result))