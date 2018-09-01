# Crawler

This is a rediit crawler. It crawls subreddits and its main goal is to gather the most awesome threads - up to 5k votes!

If you want to read more about the challenge, read [the challenge](CHALLENGE.md)

## Usage

To use this crawler, you can invoke it as a `CLI`, talk to it using the `Telegram bot` or import it and use it as an `API`. The API is the highest surface
used to build higher level interfaces from it, for example the `CLI` and the `Telegram bot`.

Head to the interface you want to use and follow the examples.

### API

Import the API and use the `find_awesome_threads` function to find some amazing threads.

```python
from crawler.api import find_awesome_threads
subreddits = ["cats", "askreddit", "brazil"]
awesome_threads = find_awesome_threads(subreddits)
print(awesome_threads)
```

### CLI

```console
$ python cli.py -h
$ python cli.py "cats;askreddit"
```

### Telegram bot

To run the bot you need to run the module that starts a long polling process.
Before running it, you need a Telegram API token.

```console
$ python bot.py -h
$ python bot.py <TOKEN>
```

## Tests

There is a test suite that guarantee our code works and does not break when we change it.

```console
make test
```
