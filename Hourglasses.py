max_number = - float('inf')
curr_number = 0

arr = []

for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))

for index in range(1, 5):
    for ind in range(1, 5):
        curr_number = 0
        curr_number += arr[index-1][ind-1] + arr[index-1][ind] + arr[index-1][ind+1] + arr[index][ind] + arr[index+1][ind-1] + arr[index+1][ind] + arr[index+1][ind+1]
        if curr_number > max_number:
            max_number = curr_number
        
print(max_number)