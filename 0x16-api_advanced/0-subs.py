#!/usr/bin/python3
"""unction that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    """Check if request is successful"""
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        except KeyError:
            return 0
    else:
        return 0
