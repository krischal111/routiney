import os
import dotenv
dotenv.load_dotenv()
routiney_token = os.getenv('routiney_token')
from utils import *

import discord
intents = discord.Intents.default()
intents.message_content = True
# intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  for guild in client.guilds:
    print(guild.name)
    members = '\n - '.join([member.name for member in guild.members])
    print(" -", members)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  # print(f"User '{message.author}' says:\n '''{message.content[:]}'''")
  if message.content.startswith('!help'):
    help_text = read_help()
    await message.channel.send(help_text)
  
  if message.content.startswith('!rutu'):
    await message.channel.send('Ask the CR')
















if __name__ == "__main__":
  client.run(routiney_token)