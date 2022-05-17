# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')
bot.remove_command('help') # Removes default help command

@bot.command(name='help')
async def nine_nine(ctx):
    await ctx.send('test')

@bot.command(name='clear') # usage: clear's last n messages
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@bot.command(name='purge') # Purges everything a user has said from the server by userId
async def purge(ctx, userId):
    counter = 0
    async for message in ctx.history(limit=200):
        if message.author == bot.user:
            await message.delete() # Deletes message for given user

@bot.command(name='jail')
async def jail(ctx, userId):
    print('jail call')

@bot.command(name='watch')
async def watch(ctx, userId):
    print('watch dog activated on $user', userId)

@bot.command(name='publish')
    print('Publishing JSON information')





@bot.command(name='overload') # Will be removed, here only to test overloading in python
async def overload(ctx, *args):
    # In theory now we can load in whatever arguments we want?
    # test theory -> overload(int): await 'integer' || overload(str): await 'str'
    await ctx.send('value '+ "\n".join(args))

bot.run(TOKEN)
