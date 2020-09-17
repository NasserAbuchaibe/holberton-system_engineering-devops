#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """[summary]

    Args:
        subreddit ([type]): [description]
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    req = requests.get(url, headers=header)

    if req.status_code != 200:
        print("None")
        return

    try:
        childs = req.json().get("data").get("children")
        for child in childs:
            print(child.get("data").get("title"))
    except Exception:
        pass
