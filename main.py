from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN= getenv("TOKEN")

bot = commands.Bot("bot ")

@bot.event
async def on_ready():
    print('Bot initialized')

@bot.command()
async def test(ctx):
    await ctx.send("This is just test command \n ~ MidNightBot 2020")

@bot.command(help='This command says your message. \nFormat: "bot say <message>"')
async def say(ctx,arg1 = None):
    if not arg1: await ctx.send("No message adeded ! See bot help say")
    else: await ctx.send(f"{ctx.author} wants me to say ```{arg1}```")


bot.run(TOKEN)