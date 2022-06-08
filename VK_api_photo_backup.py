import os
import requests
import yadisk
import time
import datetime
from pprint import pprint

# Создаем класс, который будет иметь методы для выполнения поставленных задач, а также token доступа к API VK
class VK_user:

	# URL неизменнен для работы с API VK
	url = "https://api.vk.com/method/"
	# Работа будет производится с версией API под номером 5.131.
	version = '5.131'

	def __init__(self, token: str):
		self.params = {
						"access_token" : token,
						"v" : self.version}

	# Метод для получения фотографий профиля
	def get_photos(self, user_id: str):
		photos_url = self.url + "photos.get"
		photos_params = {
							"user_id" : user_id,
							"album_id" : "wall"}
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
		 		if types['type'] == "r":
		 			quality_photos[types['url']] = elem["date"]
		return quality_photos

# Считываем token для работы с API VK
def get_token(file_name: str):
	file_path = os.path.join(os.getcwd(), file_name)
	with open(file_path, "r", encoding = "utf-8") as file:
		access_token = file.readline().strip()
	return access_token

vk_token = get_token("VK_access_token.txt")
yandex_token = get_token("Yandex_access_token.txt")

user = VK_user(vk_token)
user_id = "733087995"

result = user.get_photos(user_id)
# pprint(result)
result = user.get_quality_photos(result)

yandex = yadisk.YaDisk(token=yandex_token)

now = datetime.datetime.now()
directory = "download images "+now.strftime("%d-%m-%Y")

yandex.mkdir(directory)
for elem in list(result.keys()):
	yandex.upload_url(elem, directory+"/"+time.strftime("%M", time.gmtime(result[elem]))+".jpg")
