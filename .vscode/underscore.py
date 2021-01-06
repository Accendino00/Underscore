# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
pp = commands.Bot(command_prefix='!')
TOKEN = os.getenv('DISCORD_TOKEN')


@pp.event
async def on_ready():
    await pp.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to !help"))
    print("I am online")

@pp.event
async def on_message(message):
    await pp.process_commands(message)
    if message.author == pp.user:
        return
    elif 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

@pp.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong with {str(round(pp.latency, 2))}")

@pp.command(name="whoami")
async def whoami(ctx):
    await ctx.send(f"You are {ctx.message.author.name}")

@pp.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


pp.run(TOKEN)
