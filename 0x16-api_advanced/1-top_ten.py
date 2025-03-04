#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10
hot posts in a subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts in a subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {
        'User-agent': 'Python/requests:top_ten_checker:v1.0 (by /u/Tsholoo)'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        try:
            results = response.json()
            posts = results.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title', 'None'))
        except (ValueError, KeyError, TypeError):
            print("None")
        else:
            print("None")
