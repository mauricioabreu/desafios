"""CLI for finding subreddits threads.

Usage:

    Asking for help:
        $ python cli.py -h

    Finding awesome subreddit threads:
        $ python cli.py cats;python
"""

import argparse

from crawler import api

parser = argparse.ArgumentParser(description="Find some amazing reddit threads")
parser.add_argument(
    "subreddits",
    metavar="subreddits",
    type=str,
    help="subreddits separate by semicolon. Ex: askreddit;worldnews;cats",
)

args = parser.parse_args()

awesome_threads = api.find_awesome_threads(args.subreddits.split(";"))

for subreddit, threads in awesome_threads.items():
    for thread in threads:
        print(f"Subreddit: {subreddit}")
        print(f"Title: {thread['title']}")
        print(f"Upvotes: {thread['upvotes']}")
        print(f"Thread link: {thread['thread_link']}")
        print(f"Comments link: {thread['comments_link']}")
        print("\n")
        print("~" * 20)
        print("\n")
