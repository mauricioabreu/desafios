"""Test for the crawler application."""


def load_fixture(subreddit):
    with open("fixtures/{subreddit}.html") as f:
        return f.read()


def test_scrap_threads():
    return True
