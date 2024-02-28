import os
import discord
import time
from discord.ext import commands
#from discord.ext.commands import Bot
#from discord.voice_client import VoiceClient
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
#client = discord.Client(command_prefix='&', intents=intents)
bot = commands.Bot(command_prefix='&', intents=intents)



#Bot is online check
@bot.event
async def on_ready():
    print('speak bot online')

#Testing responses to specific users and messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('&test'):
        await message.channel.send('bot is online')        
        

    if message.author.id == 191388873673146368:
        outmes = 'remember to drink water'
        await message.channel.send(outmes)


    await bot.process_commands(message)


#Play specified audio
@bot.command(pass_context= True)
async def play(ctx, link):
    voice_channel = ctx.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=link))


#Play audio then leave
@bot.command(pass_context= True)
async def drink(ctx, link):
    if (ctx.author.voice and not ctx.voice_client):
        channel = ctx.message.author.voice.channel
        await channel.connect(reconnect = False)
        voice_channel = ctx.voice_client
        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source=link))
        time.sleep(3)
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()

#Make bot join vc
@bot.command(pass_context= True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect(reconnect = False)

#Make bot leave vc
@bot.command(pass_context= True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()

#Play specified audio file
@bot.command(pass_context= True)
async def testing(ctx, file):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=file))

#Pause audio
@bot.command(pass_context=True)
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()

#Resume audio
@bot.command(pass_context=True)
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()

#Stop audio
@bot.command(pass_context=True)
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()


#Start bot
bot.run(TOKEN)