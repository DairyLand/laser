import discord
import asyncio
import random
import praw

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

reddit = praw.Reddit(client_id='<client_id>', client_secret='<client_secret>', user_agent='discord-bot')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_update(before, after):
    if after.activity and after.activity.name == 'Overwatch 2':
        time_played = after.activity.duration.total_seconds() / 60
        if time_played > 10:
            channel = discord.utils.get(after.guild.channels, name='General')
            await channel.send(f'{after.mention} imagine playing overwatch lmao')

@client.event
async def on_message(message):
    if message.content == "$ow":
        subreddit = reddit.subreddit('OverwatchPorn')
        posts = subreddit.hot(limit=10)
        posts = random.sample(list(posts), 10)
        for post in posts:
            if post.url:
                await message.channel.send(post.url)
                await asyncio.sleep(1)
    print(f'{message.author} sent the message: "{message.content}" in the channel: {message.channel}')

client.run('<token>')
