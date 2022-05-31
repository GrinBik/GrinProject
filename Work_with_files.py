import os
from pprint import pprint

def prepare_cookbook(file_name: str) -> dict:
	
	file_path = os.path.join(os.getcwd(), file_name)
	cookbook = {}

	with open(file_path, "r", encoding = "utf-8") as file:

		for line in file:
			recipe = []
			dish_name = line[:-1]
				
			ingredients_number = int(file.readline())

			for i in range(ingredients_number):
		
				string = file.readline().strip().split(" | ")
				ingridient = {}

				ingridient_name = string[0]
				ingridient["ingredient_name"] = ingridient_name

				quantity = int(string[1])
				ingridient["quantity"] = quantity
				
				unit = string[2]
				ingridient["measure"] = unit
				
				recipe.append(ingridient)

			cookbook[dish_name] = recipe
			file.readline()

		return cookbook

def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:

	cook_book = prepare_cookbook("Сookbook.txt")

	shop_list = {}

	for dish in dishes:
		if dish in list(cook_book.keys()):

			ingridients = cook_book[dish]
			ingridients_number = len(ingridients)

			for i in range(ingridients_number):
				
				ingredient_name = ingridients[i]["ingredient_name"]
				measure = ingridients[i]["measure"]
				quantity = ingridients[i]["quantity"]
				
				if ingredient_name not in shop_list:
					shop_list[ingredient_name] = {"measure" : measure , "quantity" : quantity * person_count}
				else:
					shop_list[ingredient_name]["quantity"] += quantity * person_count
		
		else: 
			print(f'{dish} - нет такого рецепта!')
	
	return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель'], 1))