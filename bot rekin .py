import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix ='PREFIX')

@client.event
async def on_ready():
    print('BOT JEST ONLINE')
    print(discord.__version__)
    
@client.command()
async def ping(ctx):
	await ctx.send("Pong!")
	
client.run('NjEzMDY5OTIwODMzNjM0MzA2.XWacrA.l1BxjOX98Z4Zu3RT7CaLyiNp9Tk')import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix ='+')

@client.event
async def on_ready():
    print('BOT JEST ONLINE')
    print(discord.__version__)
    
@client.command()
async def ping(ctx):
	await ctx.send("Pong!")
	
client.run('NjEzMDY5OTIwODMzNjM0MzA2.XWafWQ.jLAVHEp5B2k72ZK4wWV94WVdups')
