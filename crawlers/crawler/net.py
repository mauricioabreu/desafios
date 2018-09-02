import requests


def read_html_page(url):
    response = requests.get(
        url, allow_redirects=True, headers={"User-Agent": "most-awesome-threads 0.1"}
    )
    return response.content
