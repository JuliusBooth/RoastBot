import discord
from src.response import get_response
from src.config import TOKEN, replyList, guildNames

client = discord.Client(intents=discord.Intents.all())

# Things to run when the bot connects to Discord
@client.event
async def on_ready():
    print('Connected!')
    # print users on server
    for guild in client.guilds:
        for member in guild.members:
            print(member.name, member)

@client.event
async def on_message(message):
    # don't respond to messages from the bot itself
    if message.author == client.user:
        return
    # respond to messages from anyone on server or in replyList
    if message.guild.name not in guildNames and message.author.name not in replyList:
        return
    response = get_response(message)
    if response:
        await message.channel.send(response)

client.run(TOKEN)
