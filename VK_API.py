import requests
from pprint import pprint

class Vk_user:

    url = "https://api.vk.com/method/"

    def __init__(self, token: str, version: str):
        self.params = {
                        'access_token' : token,
                        'v' : version
                        }

    def search_groups(self, q : str, sorting = 0):
        '''
        Параметры sort
        0 - сортировать по умолчанию
        1 - сортировать по скорости роста
        2 - сортировать по отношению дневной посещаемости
        3 - сортировать по отношению количетсва лайков
        4 - сортировать по отношению количества комментариев
        5 - сортировать по отношению количества публикаций
        '''
        group_search_params = {
                                'q' : q,
                                'sort' : sorting,
                                'count' : 300
                                }
        group_search_url = self.url + 'group.search'
        resp = requests.get(group_search_url, params = {**self.params, **group_search_params}).json()
        resp = resp['response']['items']
        return resp

    def search_group_ext(self, q : str, sorting = 0):
        group_search_ext_url = self.url + 'groups.getById'
        target_groups = self.search_groups(q, sorting)
        target_groups_ids = ','.join([str(group['id']) for group in target_groups])
        groups_info_params = {
                                "group_ids" : target_groups_ids,
                                'fields' : "members_count, activity, description"
                                }
        resp = requests.get(group_search_ext_url, params = {**self.params, **groups_info_params}).json()
        return resp['response']

    def get_followers(self, user_id = None):
        followers_url = self.url + 'users.getFollowers'
        followers_params = {
                            "count" : 10,
                            'user_id' : user_id
                        }
        resp = requests.get(followers_url, params = {**self.params, **followers_params}).json()
        return resp['response']

    def user_info(self, user_id = '1'):
        user_url = self.url + 'users.get'
        user_params = {
                        'user_id' : user_id,
                        'fields' : 'education, sex'
                    }
        resp = requests.get(user_url, params = {**self.params, **user_params}).json()
        return resp

    def get_groups(self, user_id = None):
        groups_url = self.url + 'groups.get'
        groups_params = {
                            'count' : 10,
                            "user_id" : user_id,
                            'extended' : 1,
                            'fields' : 'members_count'
                        }
        resp = requests.get(groups_url, params = {**self.params, **groups_params})
        return resp.json()

token = 'c51be480fc5bea43237ee7262a0fb43d160f117f06e1a74e29a2cd730e0adae44ad43c64484c712ca5070'

vk_client = Vk_user(token, '5.131')
result = vk_client.user_info()
pprint(result)