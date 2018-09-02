"""API to find the most upvoted threads in subreddits."""
from crawler import net, scrapper


def find_awesome_threads(
    subreddits,
    site="https://old.reddit.com",
    minimum_votes=5000,
    max_pages=5,
    max_threads=5,
):
    """Find the trending threads of reddit.

    A `trending` thread is identified by the total of votes,
    the difference of likes and dislikes.
    """
    subreddits_threads = {}
    for subreddit in subreddits:
        subreddits_threads[subreddit] = scrap_subreddit_threads(
            subreddit,
            "/r/".join([site, subreddit]),
            minimum_votes,
            max_pages,
            max_threads,
        )
    return subreddits_threads


def scrap_subreddit_threads(subreddit, site, minimum_votes, max_pages, max_threads):
    threads = []
    page_site = site

    total_read_pages = 0

    while (len(threads) < max_threads) and (total_read_pages < max_pages):
        if not page_site:
            break

        page = scrapper.tree_from_buffer(net.read_html_page(page_site))
        page_threads, page_site = scrapper.find_threads(page, site)
        threads.extend(filter_most_voted(page_threads, minimum_votes))
        total_read_pages += 1

    return threads[:max_threads]


def filter_most_voted(threads, minimum_votes):
    """Filter all posts that have at least `minimum_votes."""
    most_voted = []
    for thread in threads:
        if thread["upvotes"] >= minimum_votes:
            most_voted.append(thread)
    return most_voted
