import openai
from config import OPEN_AI_KEY

openai.api_key = OPEN_AI_KEY

def mentions_bot(message):
    # checks if the words openai or language model are in the message
    return "openai" in message.content.lower() or "language model" in message.content.lower() or "julius" in message.content.lower()

def get_response(message, messageCounts,messageHistory, sentiment_pipeline):
    print("Message from %s: %s" % (message.author, message.content))

    concatenated_message = messageHistory.get_response(message)
    if concatenated_message:
        print("Concatenated message: %s" % concatenated_message)
    else:
        return ""

    # if number of messages sent today > 50, don't respond
    if messageCounts.get_author_message_count(message.author) > 50:
        return
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

    data = [response]
    sentiment = sentiment_pipeline(data)
    print(response, sentiment)
    if mentions_bot(message):
        return ""
    # if sentiment[0]["label"] == "POSITIVE" and sentiment[0]["score"] > 0.999:
    #     return ""
    return response

