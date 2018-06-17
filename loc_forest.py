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
        global x_axis
        y_axis -= 1 
        if y_axis == -3:
            emb = (discord.Embed(title="Area Change", description="You've entered the Plains of Plantaria", color=0x00ff00))
            emb.set_author(name="Position")
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/457958097185406990/Old-Time-Wallpaperold-time-wallpaper-1920x1080-windows-xp-PIC-WPHR7139.png")
            await client.send_message(message.channel, embed=emb)
            await client.send_file(message.channel,str(x_axis)+str(y_axis)+".jpg")
        else: 
            await client.send_file(message.channel,str(x_axis)+str(y_axis)+".jpg")
    elif message.content.startswith('!gonorth'):
        y_axis += 1
        if y_axis == 2:
            emb = (discord.Embed(title="error", description="you can't walk into the water now!", color=0x00ff00))
            emb.set_author(name="Map")
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/451065589046181890/h9VHq2Y2_400x400.png")
            await client.send_message(message.channel, embed=emb)
            y_axis -= 1 
        else: 
            await client.send_file(message.channel,str(x_axis)+str(y_axis)+".jpg")
    elif message.content.startswith('!goeast'):
        x_axis += 1 
        if x_axis == 2:
            emb = (discord.Embed(title="Area Change", description="You've entered the Plains of Plantaria", color=0x00ff00))
            emb.set_author(name="Position")
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/457958097185406990/Old-Time-Wallpaperold-time-wallpaper-1920x1080-windows-xp-PIC-WPHR7139.png")
            await client.send_message(message.channel, embed=emb)
            await client.send_file(message.channel,str(x_axis)+str(y_axis)+".jpg")
        else: 
            await client.send_file(message.channel,str(x_axis)+str(y_axis)+".jpg")
    elif message.content.startswith('!gowest'):
        x_axis -= 1 
        if x_axis == -2:
            emb = (discord.Embed(title="error", description="you can't walk into the water now!", color=0x00ff00))
            emb.set_author(name="Map")
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/451065589046181890/h9VHq2Y2_400x400.png")
            await client.send_message(message.channel, embed=emb)
            x_axis += 1 
        else: 
            await client.send_file(message.channel,str(x_axis)+str(y_axis)+".jpg")
    if message.content.startswith('!map'):
            await client.send_file(message.channel,str(x_axis)+str(y_axis)+".jpg")
    if message.content.startswith('!hello'):
        emb = (discord.Embed(description="This is your current position on the map"))
        emb.set_author(name="Map")
        emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/451065589046181890/h9VHq2Y2_400x400.png")
        emb.add_field(name="position",value="you are in the center of forest",inline=False)
        await client.send_message(message.channel, embed=emb)
@client.event
async def on_ready():
    print("I'm up and running")

    
client.run("NDQzMTY3MTY0NDU5OTA5MTIw.Dgdtug.7Y5J0kfgaI1bS3NeLs7ZkpQjZm0")
