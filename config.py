import os
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