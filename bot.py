import random

import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Running as {}".format(client.user))


@client.event
async def on_message(message):
    if "@someone" in str(message.content).lower():
        members_array = []

        async for member in message.guild.fetch_members(limit=None):
            members_array.append(member)

        await message.channel.send(random.choice(members_array).mention)

client.run("your bot token here")
