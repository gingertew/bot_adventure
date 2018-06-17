import discord.ext
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

#center, north, south, east, west, southwest, southeast, northwest, northeast, doublesouth, doublesouthwest, doublesoutheast
x_axis = 0 
y_axis = 0

@client.event
async def on_message(message):
    if message.content.startswith('!gosouth'):
        global y_axis
        y_axis -= 1      
    elif message.content.startswith('!gonorth'):
        y_axis += 1
    elif message.content.startswith('!goeast'):
        global x_axis
        x_axis += 1
    elif message.content.startswith('!gowest'):
        x_axis -= 1
    elif x_axis < -1 and y_axis > 1:
        await client.send_message(message.channel,"you can't into the water now") 
    if message.content.startswith('!map'):
        emb = (discord.Embed(description="This is your current position on the map"))
        emb.set_author(name="Map")
        emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/451065589046181890/h9VHq2Y2_400x400.png")
        emb.add_field(name="position",value="you are in the center of forest",inline=False)
        await client.send_message(message.channel, embed=emb)
    if message.content.startswith('!hello'):
        await client.send_file(message.channel,"-1-1.jpg")
@client.event
async def on_ready():
    print("I'm up and running")

    
client.run("NDQzMTY3MTY0NDU5OTA5MTIw.Dgdtug.7Y5J0kfgaI1bS3NeLs7ZkpQjZm0")
