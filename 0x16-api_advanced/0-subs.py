#!/usr/bin/python3
"""Function that queries the Reddit API and
 returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
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
