import discord
from transformers import pipeline
from Messages import MessageCounts,RecentMessages
from response import get_response
from config import TOKEN


sentiment_pipeline = pipeline("sentiment-analysis")

client = discord.Client(intents=discord.Intents.all())

# Things to run when the bot connects to Discord
@client.event
async def on_ready():
    print('Connected!')
    # print users on server
    for guild in client.guilds:
        for member in guild.members:
            print(member.name, member)

reply_list = ["RamblingAnthonyBot", "Anthonycsikos"]
guild_names = ["julius's test server"]#, "julius's test server 2"]

messageCounts = MessageCounts()
messageHistory = RecentMessages()

@client.event
async def on_message(message):
    # don't respond to messages from the bot itself
    if message.author == client.user:
        return
    # respond to messages from julius's test servers or anyone in the reply_list
    if message.guild.name not in guild_names and message.author.name not in reply_list:
        return

    response = get_response(message, messageCounts,messageHistory, sentiment_pipeline)

    if response:
        await message.channel.send(response)

client.run(TOKEN)
