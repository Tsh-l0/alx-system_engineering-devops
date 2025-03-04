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
    headers = {"User-Agent": "Custom-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post["data"].get("title"))
        else:
            print(None)
