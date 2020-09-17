#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """[summary]

    Args:
        subreddit ([type]): [description]
        hot_list (list, optional): [description]. Defaults to [].
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    if after is not None:
        url += '?after={}'.format(after)

    req = requests.get(url, headers=header).json()

    if req.get('error') == 404:
        return

    dat = req.get("data").get("children")

    for tit in dat:
        hot_list.append(tit.get("data").get("title"))

    after = req.get("data").get("after")

    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
