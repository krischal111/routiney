import os
import dotenv
dotenv.load_dotenv()
routiney_token = os.getenv('routiney_token')
from utils import *
from routine import routine

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
    if len(message.content) < 6:
      day = calculate_day('')
    else:
      day = calculate_day(message.content[6:])
    schedule_text = routine.format_routine(day)
    await message.channel.send(f'```{schedule_text}```\n-# (Please refer to CR for any changes to this routine.)')
















if __name__ == "__main__":
  client.run(routiney_token)