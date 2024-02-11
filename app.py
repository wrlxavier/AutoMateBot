import os
import discord
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is connected.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')


client.run(DISCORD_TOKEN)
