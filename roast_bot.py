import discord
from src.discord_history import get_recent_messages
from src.response import get_response
from src.config import TOKEN, replyList, guildNames

client = discord.Client(intents=discord.Intents.all())

# Things to run when the bot connects to Discord
@client.event
async def on_ready():
    print('Connected!')
    # print users on server
    for guild in client.guilds:
        print(guild.name, guild.id)
        for member in guild.members:
            print(member.name, member)

@client.event
async def on_message(message):
    # don't respond to messages from the bot itself
    if message.author == client.user:
        return
    if message.guild.name in guildNames and message.author.name in replyList:
        response = await get_response(message)
        if response:
            await message.channel.send(response)

client.run(TOKEN)
