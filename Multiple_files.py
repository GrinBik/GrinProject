import os

def count_lines_in_file(file_name: str) -> int:
	file_path = os.path.join(os.getcwd(), file_name)
	count = 0
	with open(file_path, "r", encoding = "utf-8") as file:
		for line in file:
			count += 1
	return count

def write_file(count: int, read_file: str, write_file: str, what_we_do: str):
	
	result_path = os.path.join(os.getcwd(), write_file)
	read_path = os.path.join(os.getcwd(), read_file)
	
	with open(result_path, what_we_do, encoding = "utf-8") as result_file:
		with open(read_path, "r", encoding = "utf-8") as reading_file:
			
			result_file.write(read_file + "\n")
			result_file.write(str(count) + "\n")
			
			for line in reading_file:
				result_file.write(line)
			
			result_file.write("\n")

def multiple_files(file_names: list, file_name: str):
	
	files_count = {}
	file_number = len(file_names)

	for path in file_names:
		count_path = count_lines_in_file(path)
		files_count[count_path] = path
	
	for i in range(file_number):
		if i != file_number-1:
			
			min_count_file = min(list(files_count.keys()))
			read_file_path = files_count[min_count_file]
			del files_count[min_count_file]
			
			if i == 0:
				write_file(min_count_file, read_file_path , file_name, "w")
			else:
				write_file(min_count_file, read_file_path , file_name, "a")
		else:
			min_count_file = list(files_count.keys())[0]
			read_file_path = files_count[min_count_file]
			write_file(min_count_file, read_file_path , file_name, "a")

multiple_files(['1.txt', '2.txt', '3.txt'] , "4.txt")