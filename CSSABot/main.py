# bot.py
import os
import random
import discord
import json

from discord.ext import commands
from dotenv import load_dotenv
from paramiko import Channel

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')
bot.remove_command('help') # Removes default help command
guild = discord.Guild


# Syntax    ".clear {amnt}". Exists to clear n-amount of messages from the channel the command is called from
@bot.command(name='clear') # usage: clear's last n messages
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

# Syntax    ".purge @{user} {amnt} {optional: -rf}". Exists to remove n-amount of messages from a user. If left without
#           the optional argument, it will remove n-amount of messages from the channel the command is called from. If
#           the optional argument is included, it will remove n-amount of messages from *all* channels (except board
#           channels) that the user is in. TO CLARIFY: If you specify 100 for amount, it will remove 100 messages from
#           EACH channel that the user is in!
@bot.command(name='purge') # Purges everything a user has said from the server by userId
async def purge(ctx):
    counter = 0
    async for message in ctx.history(limit=200):
        if message.author == bot.user:
            await message.delete() # Deletes message for given user

# Syntax    ".jail @{user}". Tags a user with a "time out" role. The "time out" role exists to suppress a users
#           messages but not the content they see.
@bot.command(name='jail')
async def jail(ctx):
    message = ctx.message
    if message.mentions:
        member = message.mentions[0]
        await member.add_roles(discord.utils.get(member.guild.roles, name='Test'))
        #await member.add_roles('Test')
    else:
        return

# Syntax    ".watch @{user}". Exists for high-risk users who are little to "out of pocket" in the Discord and thus
#           earn a higher priority for both the chat filter bot & for board members to spectate. 
@bot.command(name='watch')
async def watch(ctx):
    # Log user in database watch list
    pyToJson = {}
    message = ctx.message 
    if message.mentions:
        member = message.mentions[0]
        pyToJson = {
            "Discord ID": member.id,
            "Discord Name": member.name
        }
    jsonStr = json.dumps(pyToJson)
    # ---
    # Confirm addition in admin chat
    print(jsonStr) #debug
    await ctx.send("Added user to watchlist")
    # ---

# Syntax ".watchlist". Exists to print out watch list in board chat. 
@bot.command(name='watchlist')
async def watchlist(ctx):
    print('Current watch list:')

#Syntax     ".publish". Exists to post announcement from configured file
@bot.command(name='publish')
async def publish(ctx):
    print('Publishing JSON information')

@bot.command(name='help')
async def help(ctx):
    await ctx.send("Help me! Help! ... Is it me? Am I the drama?")

@bot.command(name='uptime')
async def uptime(ctx):
    await ctx.send('Uptime')

@bot.command(name='info')
async def info(ctx):
    await ctx.send('info')

@bot.command(name='club')
async def club(ctx):
    await info(ctx)

@bot.command(name='request-info')
async def requestInfo(ctx):
    await ctx.send('We have no info on you...... yet :moyai:')

@bot.event
async def on_raw_reaction_add(payload):
    #print(payload) #Debug
    channelId = 694520377300484137
    if payload.emoji.name == '🥊':
        await payload.member.add_roles(discord.utils.get(payload.member.guild.roles, name='Test'))

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    member = await guild.fetch_member(payload.user_id) # payload.member not available for REACTION_REMOVE event type
    
    if payload.emoji.name == '🥊':
        role = discord.utils.get(guild.roles, name="Test")
        await member.remove_roles(role)
    else:
        return

    return
    




bot.run(TOKEN)
