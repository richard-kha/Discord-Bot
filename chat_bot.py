import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('bot online')


#Use openai api for bot to respond if mentioned
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=f"{message.content}",
    )

    await message.channel.send(response.choices[0].message)



#Start bot
client.run(TOKEN)