#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10
hot posts in a subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts in a subreddit
    """
    url = f"https://reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent":
               'Python/requests:top_ten_checker:v1.0.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title', 'None'))
        except ValueError:
            print(None)
        else:
            print(None)
