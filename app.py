import os
import discord
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID = os.getenv('USER_ID')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is connected.')

    user = await client.fetch_user(USER_ID)

    if user:
        dm_channel = await user.create_dm()
        await dm_channel.send(f'{user.display_name}, seu sistema de automação foi inicializado com sucesso.')



client.run(DISCORD_TOKEN)
