# RoastBot

Welcome to RoastBot, a fun and light-hearted AI-powered chatbot that roasts your friends based on their messages. RoastBot uses OpenAI's ChatGPT to generate its witty comebacks. Please remember that RoastBot is intended for good-natured humor and should not be used to bully or harass others. Keep it friendly and enjoy the laughs!

## Quick Start

To get started with RoastBot, follow these simple steps:

Open your terminal and run the following command to execute the quickstart script:

```console
./quickstart.sh
```

Open the config.json file and add the following configurations:

```console
{
  "messageBlacklist": [],
  "responseBlacklist": [],
  "guildNames": [],
  "replyList": []
}
```

- messageBlacklist: A list of phrases or words that if present will cause RoastBot to not reply.
- responseBlacklist: A list of phrases or words that if present will cause RoastBot from using its responses.
- guildNames: A list of guild names (i.e., servers) where you want RoastBot to roast everyone.
- replyList: A list of specific users that RoastBot will reply to.

Open the .env file and add the following secrets:

```console
DISCORD_TOKEN=dummytoken
OPEN_AI_KEY=dummykey
```

## Usage

Once you've set up RoastBot, it's ready to start roasting your friends! It will automatically respond to messages in the specified guilds based on the content of the message. Just keep in mind the following:

1. RoastBot is intended for good fun and should not be used to bully or harass others.
2. Always ensure that everyone participating in the roast session is comfortable with the jokes and understands that it's all in good humor.
3. If someone is uncomfortable with the roasts, please stop using RoastBot with them.
