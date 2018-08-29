"""API to find the most upvoted threads in subreddits."""
import scrapper


def find_awesome_threads(subreddits, minimum_votes=5000):
    """Find the trending threads of reddit.

    A `trending` thread is identified by the total of votes, 
    the difference of likes and dislikes.
    """
    subreddits_threads = {}
    for subreddit in subreddits:
        subreddits_threads[subreddit] = filter_most_voted(
            scrapper.find_threads(subreddit), minimum_votes
        )
    return subreddits_threads


def filter_most_voted(threads, minimum_votes):
    """Filter all posts that have at least `minimum_votes."""
    most_voted = []
    for thread in threads:
        if thread["upvotes"] >= minimum_votes:
            most_voted.append(thread)
    return most_voted
