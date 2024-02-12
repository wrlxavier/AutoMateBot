import os
from dotenv import load_dotenv


class CredentialsModel:

    def __init__(self):
        self.credentials = {}
        self._load_credentials()
  

    def _load_credentials(self):
        
        load_dotenv()
        self.credentials['DISCORD_TOKEN'] = os.getenv('DISCORD_TOKEN')
        self.credentials['DISCORD_USER_ID'] = os.getenv('DISCORD_USER_ID')
            

    def get_discord_credentials(self):

        discord_credentials = {
            'TOKEN': self.credentials['DISCORD_TOKEN'],
            'USER_ID': self.credentials['DISCORD_USER_ID']
        }

        return discord_credentials



