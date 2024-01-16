#!/usr/bin/python3
"""unction that queries the Reddit API and returns the number of subscribers"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Custom User Agent'}
    params = {"limit": 10, "after": after}

    response = requests.get(url, headers=headers, params=params)

    """Check if request is successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)
            after = data['data']['after']

            if after:
                recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except KeyError:
            return None
    else:
        return None
