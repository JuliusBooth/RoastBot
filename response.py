import random
import openai
from config import OPEN_AI_KEY

openai.api_key = OPEN_AI_KEY

model_engine = "text-davinci-003"

# A bunch of one or two word negative responses
negative_responses = [
    "no",
    "nah",
    "I'll take no for 200$ Alex",
    "nope",
    "nah trick",
    "you playin",
    "you playin bro",
    "you playin bro?",
    "that ain't it king",
    "that ain't it chief",
    "negatory",
    "negative",
    "nay",
    "u trippin",
    "u trippin bro",
    "u wot m8?",
    "wut",
    "dat's cray cray",
    "respectfully disagree sir",
    "I agree... jk can you imagine tho, like what if I did?! You'd be like the robot has lost his damn mind",
    "wrong"]

def get_response(message, past_messages, sentiment_pipeline):

    print("Message from %s: %s" % (message.author, message.content))
    num_words = len(message.content.split())
    # if there are fewer than 6 words in the message, don't respond
    if  num_words < 6 or num_words > 500:
        # random negative response
        return random.choice(negative_responses)

    # if number of messages sent today > 50, don't respond
    if past_messages.get_author_message_count(message.author) > 50:
        return
    past_messages.increment_author_message_count(message.author)

    max_tokens = 50

    prompt = "You are a very disagreeable, mean spirited person. Your friend Anthony just said '%s'. Tell him why you disagree in under 30 words." % message.content
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response = completion.choices[0].text
    data = [response]
    sentiment = sentiment_pipeline(data)
    print(response, sentiment)
    if sentiment[0]["label"] == "POSITIVE" and sentiment[0]["score"] > 0.98:
        return

