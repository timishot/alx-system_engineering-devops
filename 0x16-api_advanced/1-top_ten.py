#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Custom User Agent'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)

    """Check if request is successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        except KeyError:
            return None
    else:
        return None
