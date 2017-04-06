# import vk
import json

import requests

from webim_test_task.settings import VK_API_KEY, VK_SECRET_KEY


def vk_auth():
    url = 'https://oauth.vk.com/authorize'
    params = {'client_id': VK_API_KEY, 'display': 'page', 'redirect_uri': 'http://127.0.0.1:8000/get_token',
              'scope': 'friends', 'response_type': 'code', 'v': '5.63'}
    auth = requests.get(url=url, params=params)
    return auth.url


def get_access_token(code):
    url = 'https://oauth.vk.com/access_token'
    params = {'client_id': VK_API_KEY, 'client_secret': VK_SECRET_KEY,
              'redirect_uri': 'http://127.0.0.1:8000/get_token',
              'code': code}
    auth = requests.get(url=url, params=params)
    return json.loads(auth.text)


def get_friends(access_token):
    'https://api.vk.com/method/friends.getOnline?v=5.52&access_token='
    url = 'https://api.vk.com/method/friends.getOnline'
    params = {'v': '5.52', 'access_token': access_token}
    friends_info = requests.get(url, params)
    friends = json.loads(friends_info.text).get('response')[5:]
    reworked_friends = []
    for friend in friends:
        url = 'https://api.vk.com/method/users.get?user_id=210700286&v=5.52'
        params = {'user_id': friend, 'v': '5.52'}
        response = requests.get(url, params)
        reworked_friends.append('%s %s' % (json.loads(response.text).get('response')[0].get('first_name'),
                                json.loads(response.text).get('response')[0].get('last_name')))
    return reworked_friends

def get_info(access_token, user_id):
    url = 'https://api.vk.com/method/users.get?user_id=210700286&v=5.52'
    params = {'user_id': user_id, 'v': '5.52'}
    response = requests.get(url, params)
    user = '%s %s' % (json.loads(response.text).get('response')[0].get('first_name'),
                      json.loads(response.text).get('response')[0].get('last_name'))
    friends = get_friends(access_token)
    return user, friends
