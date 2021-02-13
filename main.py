import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.muteloli'):
        await message.channel.send('Cadê aquele fdp')

    if message.content.startswith(''):
        pass


client.run(TOKEN)

# ToDO: fazer o bot desmotivacional
