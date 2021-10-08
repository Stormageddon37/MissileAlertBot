import os
import string
from API import RedColorAlarmAPI
from datetime import datetime
import discord
import random
import time
import asyncio
import threading

with open("TOKEN.txt", "r") as f:
    BOT_TOKEN = f.read()
    print("TOKEN: " + BOT_TOKEN)

bot = discord.Client()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!A'):
        alert = str(API.get_last_alert())
        when = alert[15:34]
        where = alert[77:len(alert) - 2]
        await message.channel.send(where + "\n" + when)


@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('I will send this message when I join a server')
        break


@bot.event
async def on_ready():
    print('Logged in as: {0.user.name}\nID: {0.user.id}'.format(bot))


def check_new():
    threading.Timer(5.0, check_new).start()
    # print("Hello, World!")
    # print(API.get_last_alert())


API = RedColorAlarmAPI()
check_new()
bot.run(BOT_TOKEN)
