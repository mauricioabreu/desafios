from crawler import api


def test_find_awesome_threads():
    print(api.find_awesome_threads(["cats", "askreddit"]))
