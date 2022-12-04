import os
import discord
import logging
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client = discord.Client(intents=intents, log_handler=handler)
embed = discord.Embed(title='Japan Countdown')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!countdown'):
        JAPAN_DATE = datetime(year=2023, month=3, day=26, hour=6)
        countdown = JAPAN_DATE - datetime.now()
        embed.description = f"Taking off in {countdown.days} days"
        embed.color = 0x42c8f5
        embed.set_thumbnail(url="https://www.kcpinternational.com/wp-content/uploads/2014/01/Japan-Flag-and-cherry-blossoms.jpg")
        await message.channel.send(embed=embed)

    if message.content.startswith('!hello'):
        await message.channel.send('Hi!')

client.run(os.environ.get('DISCORDBOTTOKEN'))
