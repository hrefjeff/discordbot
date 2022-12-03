import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!hello'):
    await message.channel.send('greetings!')

# In a linux environment, on the terminal enter following command:
# export DISCORDBOTTOKEN="enter token here"
client.run(os.environ.get('DISCORDBOTTOKEN'))
