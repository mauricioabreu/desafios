def format_upvotes(upvotes):
    try:
        return int(upvotes)
    except ValueError:
        return 0


def format_link(link, site):
    if not link.startswith("http"):
        return site + link
    return link


def format_threads(threads, site):
    for thread in threads:
        thread["upvotes"] = format_upvotes(thread["upvotes"])
        thread["thread_link"] = format_link(thread["thread_link"], site)

    return threads
