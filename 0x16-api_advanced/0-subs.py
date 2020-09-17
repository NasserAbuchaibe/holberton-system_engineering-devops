#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """[summary]

    Args:
        subreddit ([str]): [subreddit]
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    req = requests.get(url, headers=header)

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    return 0
