import requests
import json

file_path = ('C:\\Users\\user\\Desktop\\Downloads\\GrinProject\\Super_Hero_token.txt')

def best_super_hero(names: list) -> str:

    best_hero = {}
    
    for name in names:
        resp = requests.get(url+name)
        best_hero[name] = int(resp.json()['results'][0]['powerstats']['intelligence'])
    
    max_intelligence = max(list(best_hero.values()))
    
    for hero in list(best_hero.keys()):
        if best_hero[hero] == max_intelligence:
            name_max_int = hero
    
    return f'Самый умный супер герой - это {name_max_int} !!!!!'
    
with open(file_path, "r", encoding = "utf-8") as token_file:
    token = token_file.readline().strip()

url = 'https://superheroapi.com/api/'+token+'/search/'

print(best_super_hero(["Hulk", 'Captain America', 'Thanos']))