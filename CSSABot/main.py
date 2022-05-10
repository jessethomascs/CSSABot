import os
import discord 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    # guild = client.get_guild(id) -- Will be used to force guild-only mode later on
    print(f'{client.user} has connected to Discord!')
    print(client.guilds) # Lists all the guilds that the bot is in

@client.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the guild!'
    )




client.run(TOKEN)