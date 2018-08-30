"""Test for the crawler application."""
import os

from .. import scrapper


def load_fixture(subreddit):
    current_path = os.path.dirname(__file__)

    with open(os.path.join(current_path, f"fixtures/{subreddit}.html")) as f:
        return f.read()


def test_scrap_threads():
    content = load_fixture("cats")
    tree = scrapper.tree_from_buffer(content)
    threads = scrapper.find_threads(tree, "https://old.reddit.com")

    # Ensure we have the same number of threads in the response
    assert len(threads) == 25

    # Ensure that a thread is well formed, having the right data
    sample_thread = threads[0]
    expected_thread_data = {
        "title": "After 24 years, I finally became a pet owner. Reddit, meet Kiwi :)",
        "upvotes": 13233,
        "thread_link": "https://old.reddit.com/r/cats/comments/9b44wn/after_24_years_i_finally_became_a_pet_owner/",
        "comments_link": "https://old.reddit.com/r/cats/comments/9b44wn/after_24_years_i_finally_became_a_pet_owner/",
    }
    assert sample_thread == expected_thread_data
