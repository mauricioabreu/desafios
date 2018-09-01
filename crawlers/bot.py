"""Bot to send users subreddits threads.

Usage:

    Asking for help:
        $ python bot.py -h

    Running the bot:
        $ python bot.py <TOKEN>
"""

import argparse
import logging

from telegram.ext import CommandHandler, Updater

from crawler import api


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def get_help(bot, update):
    message = """Available commands to interact with this bot:

    /NadaPraFazer <subreddits>
        Usage: /NadaPraFazer cats;askreddit
    """
    update.message.reply_text(message)


def read_subreddits(bot, update, args):
    if len(args) != 1:
        update.message.reply_text("Usage: /NadaPraFazer cats;askreddit")
        return False

    awesome_threads = api.find_awesome_threads(args[0].split(";"))

    message = ""
    for subreddit, threads in awesome_threads.items():
        for thread in threads:
            message += f"Subreddit: {subreddit}\n"
            message += f"Title: {thread['title']}\n"
            message += f"Upvotes: {thread['upvotes']}\n"
            message += f"Thread link: {thread['thread_link']}\n"
            message += f"Comments link: {thread['comments_link']}\n"
            message += "~" * 20
            message += "\n"

    update.message.reply_text(message)


def error(bot, update, error):
    logger.warning("Update '%s' caused error '%s'", update, error)


def main():
    parser = argparse.ArgumentParser(description="Find some amazing reddit threads")
    parser.add_argument("token", metavar="token", type=str, help="Telegram token")
    args = parser.parse_args()

    updater = Updater(args.token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("help", get_help)
    threads_handler = CommandHandler("NadaPraFazer", read_subreddits, pass_args=True)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(threads_handler)
    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
