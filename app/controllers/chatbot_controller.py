import discord

from models.credentials_model import CredentialsModel


class ChatbotController:

    def __init__(self):

        self.credentials_model = CredentialsModel()


    def run(self):

        discord_credentials = self.credentials_model.get_discord_credentials()

        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print(f'{client.user} is connected.')
            user = await client.fetch_user(discord_credentials['USER_ID'])
            if user:
                dm_channel = await user.create_dm()
                await dm_channel.send(f'{user.display_name}, seu sistema de automação foi inicializado com sucesso.')


        client.run(discord_credentials['TOKEN'])
