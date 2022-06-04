import requests
import time
from pprint import pprint
    
today = round(time.time())
two_days_ago = today - 2*24*3600

url = 'https://api.stackexchange.com/2.3/questions'

params = {"fromdate" :two_days_ago ,
          "todate":today,
          "site" : "stackoverflow",
          "sort" : "activity",
          "order" : "desc",
          "tagged" : "Python"}

resp = requests.get(url, params=params)

questions = resp.json()['items']

print('Вопросы за последние два дня:\n')

for question in questions:
    print(f"Кто задал вопрос: {question['owner']['display_name']}")
    print(f"Заданный вопрос: {question.get('title')}")
    print(f'Ссылка на вопрос: {question.get("link")}\n\n')