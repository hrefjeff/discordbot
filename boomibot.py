import os

from discord.ext import tasks

import discord
import logging
from datetime import datetime

# Japan embedded channel post
JAPAN_DATE = datetime(year=2023, month=3, day=27, hour=0)
embedded_msg = discord.Embed(title='Japan Countdown')
embedded_msg.color = 0x42c8f5
embedded_msg.set_thumbnail(url="https://www.kcpinternational.com/wp-content/uploads/2014/01/Japan-Flag-and-cherry-blossoms.jpg")

class BoomiClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from the task
        self.counter = 0

    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.japan_reminder.start()

    @tasks.loop(seconds=86400)
    async def japan_reminder(self):
        channel = discord.utils.get(self.get_all_channels(), name='code')
        countdown = JAPAN_DATE - datetime.now()
        embedded_msg.description = f"Taking off in {countdown.days} days and {int(countdown.seconds/3600)} hours"
        await channel.send(embed=embedded_msg)

    @japan_reminder.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in

intents = discord.Intents.default()
intents.message_content = True
client = BoomiClient(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hi!')

client.run(os.environ.get('DISCORDBOTTOKEN'))
