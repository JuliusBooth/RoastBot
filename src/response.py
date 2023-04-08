import openai
from src.config import OPEN_AI_KEY, messageCounts, messageHistory, messageBlacklist, responseBlacklist

openai.api_key = OPEN_AI_KEY

def mentions_blacklisted_words(response, blacklist):
    return any(word in response.lower() for word in blacklist)

def should_generate_response(message):
    return messageCounts.get_author_message_count(message.author) < 50 and len(message.content) < 500 and not mentions_blacklisted_words(message.content, messageBlacklist)

def should_send_response(response):
    return not mentions_blacklisted_words(response, responseBlacklist)

def get_response(message):
    print("Message from %s: %s" % (message.author, message.content))

    concatenated_message = messageHistory.get_response(message)
    if concatenated_message:
        print("Concatenated message: %s" % concatenated_message)
    else:
        return ""

    if not should_generate_response(message):
        return ""

    messageCounts.increment_author_message_count(message.author)

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an insult comedian who disagrees with anything I say in a concise, humorous way."},
        {"role": "user", "content": "Canadian banks will never fail until either the great redistribution or the WW3 where we lose to China and Russia"},
        {"role": "assistant", "content": "The Canadian banks could fail at anytime. It doesn't matter though because you'll be broke either way."},
        {"role": "user", "content": "Does anyone want to come over for a bbq under my cherry blossom tree?"},
        {"role": "assistant", "content": "Sorry I'm not interested in recreating your Miyazaki film fantasy."},
        {"role": "user", "content": "%s" % concatenated_message}
    ]
)
    response = response['choices'][0]['message']['content']

    print("Response: %s" % response)

    if should_send_response(response):
        return response
    return ""

