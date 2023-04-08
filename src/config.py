import os
import json
from getpass import getpass
from dotenv import load_dotenv
from src.Messages import MessageCounts, RecentMessages

load_dotenv()

if os.getenv('OPEN_AI_KEY') is None:
    OPEN_AI_KEY = getpass("Open AI Key: ")
else:
    OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')

if os.getenv('DISCORD_TOKEN') is None:
    TOKEN = getpass("Discord Token: ")
else:
    TOKEN = os.getenv('DISCORD_TOKEN')

messageCounts = MessageCounts()
messageHistory = RecentMessages()

data= {}
if os.path.exists('config.json'):
    with open('config.json') as f:
        data = json.load(f)
elif os.path.exists('src/config.json'):
    with open('src/config.json') as f:
        data = json.load(f)
        
responseBlacklist = data.get('responseBlacklist', [])
messageBlacklist = data.get('messageBlacklist', [])
guildNames = data.get('guildNames', [])
replyList = data.get('replyList', [])

