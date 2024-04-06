import discord
from discord.ext import commands
from main import get_response

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ask(ctx, *question ):
    str = ''
    for item in question:
        str = str + ' ' + item
    
    response = get_response(str)
    await ctx.send(response)


bot.run("token here")