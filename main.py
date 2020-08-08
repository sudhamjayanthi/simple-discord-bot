import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN= getenv("TOKEN")

connect = discord.Client()

@connect.event
async def on_ready():
    print('Bot initialized')

@connect.event
async def on_message(message):
    if message.author == connect.user:
        return 
    if True: 
        await message.channel.send(f"{message.author} just messaged!")

connect.run(TOKEN)