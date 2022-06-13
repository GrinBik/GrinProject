import os
import requests
import yadisk
import time
import datetime
from pprint import pprint
import json
import time
from progress.bar import IncrementalBar

# Создаем класс, который будет иметь методы для выполнения поставленных задач, а также token доступа к API VK
class VK_user:

	# URL неизменнен для работы с API VK
	url = "https://api.vk.com/method/"
	# Работа будет производится с версией API под номером 5.131.
	version = '5.131'

	def __init__(self, token: str):
		self.params = {"access_token" : token,
					   "v" : self.version}

	# Метод для получения фотографий профиля
	def get_photos(self, user_id: str):
		photos_url = self.url + "photos.get"
		photos_params = {"user_id" : user_id,
						 "album_id" : "profile"}
		photos = requests.get(photos_url, params = {**self.params, **photos_params})
		return photos.json()['response']['items']

	# Метод для получения информации профиля
	def user_info(self, user_id = '1'):
		user_info_url = self.url + "users.get"
		user_info_params = {
							'owner_id' : user_id,
							'fields' : 'education, sex'}
		user_info = requests.get(user_info_url, params = {**self.params, **user_info_params}).json()
		return user_info

	# Метод для получения фотографий максимального качества
	def get_quality_photos(self, photos: list):
		length = len(photos)
		quality_photos = {}
		for elem in photos:
		 	for types in elem["sizes"]:
		 		if types['type'] == "w":
		 			quality_photos[types['url']] = elem["date"]
		return quality_photos

# Считываем token для работы с API VK
def get_token(file_name: str):
	file_path = os.path.join(os.getcwd(), file_name)
	with open(file_path, "r", encoding = "utf-8") as file:
		access_token = file.readline().strip()
	return access_token

# Записываем данные сохраненных фотографий (name, type) в JSON файле
def write_result(file_name: str, result):
	file_path = os.path.join(os.getcwd(), file_name)
	with open(file_path, "w", encoding = "utf-8") as file:
		json.dump(result, file)

# Считываем token для VK, id для VK и token для Yandex
vk_token = get_token("VK_access_token.txt")
vk_id = get_token("VK_id.txt")
yandex_token = get_token("Yandex_access_token.txt")

user = VK_user(vk_token)

# Запрашиваем информацию о всех фотографиях на стене
result = user.get_photos(vk_id)

# Запоминаем фотографии только с хорошим качеством
result = user.get_quality_photos(result)

# Подключаемся к Яндекс диску
yandex = yadisk.YaDisk(token=yandex_token)

# Создаем папку на Яндекс диске с текущей датой для загрузки в нее фото из VK
now = datetime.datetime.now()
directory = "download images "+vk_id+now.strftime(" %d-%m-%Y %H-%M-%S")

try:
	yandex.mkdir(directory)
except yadisk.exceptions.ParentNotFoundError:
	print('Проблема с созданием директории на Яндекс Диске!')
except yadisk.exceptions.DirectoryExistsError:
	yandex.remove(directory)
	time.sleep(2)
	yandex.mkdir(directory)

output_data = {}
output_data["Photos"] = []

length = len(list(result.keys()))
bar = IncrementalBar('Copy', max = length)

# Загружаем фото из VK на Яндекс диск
# index задан для того, чтобы не делать полный бэкап, а для проверки
# работоспособности программы ограничиться копированием 5-ти фотографий
index = 1
for elem in list(result.keys()):
	bar.next()
	filename = time.strftime("%M", time.gmtime(result[elem]))
	yandex.upload_url(elem, directory+"/"+filename+'.jpg')
	output_data["Photos"].append({'filename': filename,'size': 'r',})
	if index == 5:
		break
	index += 1
bar.finish()

# Записываем в файл выходные данные
write_result("VK_api_output.txt", output_data)