import os
import json
from getpass import getpass
from dotenv import load_dotenv

load_dotenv()

if os.getenv('OPEN_AI_KEY') is None:
    OPEN_AI_KEY = getpass("Open AI Key: ")
else:
    OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')

if os.getenv('DISCORD_TOKEN') is None:
    TOKEN = getpass("Discord Token: ")
else:
    TOKEN = os.getenv('DISCORD_TOKEN')

data= {}

current_dir = os.path.dirname(os.path.realpath(__file__))
CONFIG_NAME = 'config.json'
CONFIG_PATH =os.path.join(current_dir, CONFIG_NAME)
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH) as f:
        config = json.load(f)

responseBlacklist = config.get('responseBlacklist', [])
messageBlacklist = config.get('messageBlacklist', [])
guildNames = config.get('guildNames', [])
replyList = config.get('replyList', [])
botName = config.get('botName', '')
REPLACEMENT_NAME = "Insult Comedian"

