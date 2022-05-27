double_num = list(bin(int(input())))

double_num.remove('0')
double_num.remove('b')

max_one = 0
max_two = 0
for elem in double_num:
	if elem == '1':
		max_two += 1
	else:
		if max_one < max_two:
			max_one = max_two
			max_two = 0
		else:
			max_two = 0

print(max(max_one,max_two))