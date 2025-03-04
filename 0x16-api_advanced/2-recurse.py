#!/usr/bin/python3
"""
Returns a list of the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):

    """
    Returns a list of the titles of all hot articles for a given
    subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        return hot_list if hot_list else None

    hot_list.extend(post['data']['title'] for post in posts)

    after = data['data'].get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
