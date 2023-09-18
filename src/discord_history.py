from src.config import botName, REPLACEMENT_NAME
import datetime

async def get_recent_messages(channel, limit=10):
    # get last 10 minutes of messages
    ten_mins_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
    messages = list(reversed([message async for message in channel.history(limit=limit, after=ten_mins_ago, oldest_first=False)]))
    concatenated_messages= ""
    for message in messages:
        concatenated_messages += clean_up_author_name(message.author) + ": " + message.content + "\n"

    concatenated_messages = concatenated_messages.replace(botName, REPLACEMENT_NAME)
    concatenated_messages += REPLACEMENT_NAME + ": "

    return concatenated_messages

def clean_up_author_name(author_str):
    return str(author_str).split('#')[0]

