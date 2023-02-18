import discord
from discord.ext import commands
from discord.ext.commands import bot
import openai
from transformers import pipeline
from Messages import Messages
from dotenv import load_dotenv
import os
from getpass import getpass

load_dotenv()

if os.getenv('DISCORD_TOKEN') is None:
    TOKEN = getpass("Discord Token: ")
else:
    TOKEN = os.getenv('DISCORD_TOKEN')

if os.getenv('OPEN_AI_KEY') is None:
    openai.api_key = getpass("Open AI Key: ")
else:
    openai.api_key = os.getenv('OPEN_AI_KEY')

model_engine = "text-davinci-003"

client = discord.Client(intents=discord.Intents.all())

sentiment_pipeline = pipeline("sentiment-analysis")

# Things to run when the bot connects to Discord
@client.event
async def on_ready():
    print('Connected!')
    # print users on server
    for guild in client.guilds:
        for member in guild.members:
            print(member.name, member)


reply_list = ["RamblingAnthonyBot", "Anthonycsikos"]

messages = Messages()

@client.event
async def on_message(message):
    # don't respond to messages from the bot itself
    if message.author == client.user:
        return
    # respond to messages from julius's test server or anyone in the reply_list
    if message.guild.name != "julius's test server" and message.author.name not in reply_list:
        return

    print("Message from %s: %s" % (message.author, message.content))
    num_words = len(message.content.split())
    # if there are fewer than 7 words in the message, don't respond
    if  num_words < 6 or num_words > 500:
        return

    # if number of messages sent today > 50, don't respond
    if messages.get_author_message_count(message.author) > 50:
        return
    messages.increment_author_message_count(message.author)

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

    # Send the response to the channel
    await message.channel.send(response)
            

client.run(TOKEN)
