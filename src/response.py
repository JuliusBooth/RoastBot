import openai
from src.config import OPEN_AI_KEY, messageBlacklist, responseBlacklist,REPLACEMENT_NAME
from src.discord_history import get_recent_messages, clean_up_author_name

openai.api_key = OPEN_AI_KEY

def mentions_blacklisted_words(response, blacklist):
    return any(word in response.lower() for word in blacklist)

def should_generate_response(last_message, concatenated_recent_messages):
    MESSAGE_MIN_LENGTH = 20
    MESSAGE_MAX_LENGTH = 2000
    MAX_RESPONSES = 2
    return concatenated_recent_messages.count(REPLACEMENT_NAME) <= MAX_RESPONSES  and len(last_message) > MESSAGE_MIN_LENGTH and len(concatenated_recent_messages) < MESSAGE_MAX_LENGTH and not mentions_blacklisted_words(last_message, messageBlacklist)

def should_send_response(response):
    return not mentions_blacklisted_words(response, responseBlacklist)

def prompt_for_response(concatenated_message, victim):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are an insult comedian in a discord chat, who disagrees with anything {victim} says in a concise, humorous way. Don't use metaphors or similes in the insult. Only insult {victim}."},
            {"role": "user", "content": "%s" % concatenated_message}

        ]
    )
    print(response)
    return response['choices'][0]['message']['content']


async def get_response(last_message):
    originating_channel = last_message.channel
    print("Message from %s in channel %s: %s" % (last_message.author, originating_channel, last_message.content))
    
    concatenated_recent_messages = await get_recent_messages(originating_channel, 10)

    if concatenated_recent_messages:
        print("Concatenated message: %s" % concatenated_recent_messages)
    else:
        return ""

    if should_generate_response(last_message.content, concatenated_recent_messages):
        response = prompt_for_response(concatenated_recent_messages, clean_up_author_name(last_message.author))

        print("Response: %s" % response)

        if should_send_response(response):
            return response
    return ""

