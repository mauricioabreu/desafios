import requests


def read_html_page(site, subreddit):
    response = requests.get(
        "/r/".join([site, subreddit]),
        allow_redirects=True,
        headers={"User-Agent": "most-awesome-threads 0.1"},
    )
    return response.content
