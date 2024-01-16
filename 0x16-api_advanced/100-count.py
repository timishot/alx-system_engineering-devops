#!/usr/bin/python#!/usr/bin/python3
"""unction that queries the Reddit API and returns the number of subscribers"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
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
                title = post['data']['title'].lower()
                for word in word_list:
                    word = word.lower()
                    if word in title:
                        counts[word] = counts.get(word, 0) + title.count(word)
            after = data['data']['after']

            if after:
                count_words(subreddit, word_list, after, counts)
            else:
                return print_results(counts)
        except KeyError:
            print("Error: Key not found in JSON response")
    else:
        print("Error: HTTP request failed with\
               status code", response.status_code)


def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (x[0], -x[1]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
