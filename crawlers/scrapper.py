"""Scrap reddit page to find threads."""

from lxml import html
import requests


def find_threads(subreddit, site="https://old.reddit.com"):
    page = read_html_page(site, subreddit)

    awesome_threads = []

    threads = page.xpath(f"//div[@id = 'siteTable']/div[contains(@class, 'thing')]")

    for thread in threads:
        awesome_threads.append(
            {
                "title": find_title(thread),
                "upvotes": format_upvotes(find_upvotes(thread)),
                "thread_link": format_link(find_link(thread), site),
                "comments_link": find_comments_link(thread),
            }
        )

    return awesome_threads


def format_upvotes(upvotes):
    try:
        return int(upvotes)
    except ValueError:
        return 0


def format_link(link, site):
    if not link.startswith("http"):
        return site + link
    return link


def find_link(thread):
    thread_link = thread.xpath(
        "div[@class='entry unvoted']/div[@class='top-matter']/p[@class='title']/a"
    )[0]
    return thread_link.get("href")


def find_upvotes(thread):
    upvotes = thread.xpath(
        "div[@class='midcol unvoted']/div[@class='score unvoted']/@title"
    )
    if upvotes:
        return upvotes[0]
    return 0


def find_title(thread):
    title = thread.xpath(
        "div[@class='entry unvoted']/div[@class='top-matter']/p[@class='title']/a/text()"
    )
    return title[0]


def find_comments_link(thread):
    comments_link = thread.xpath(
        "div[@class='entry unvoted']/div[@class='top-matter']/ul[1]/li[1]/a"
    )[0]
    return comments_link.get("href")


def read_html_page(site, subreddit):
    response = requests.get(
        "/r/".join([site, subreddit]),
        allow_redirects=True,
        headers={"User-Agent": "most-awesome-threads 0.1"},
    )
    return html.fromstring(response.content)
