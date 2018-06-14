import discord.ext
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()
global atlunl 
atlunl = 0
@client.event
async def on_message(message):
    if message.content.startswith('!start'):
        embed = discord.Embed(title="Start Screen", description="decide what you're going to do", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/456205678302986240/apps.png")
        embed.add_field(name="Open World", value="go and explore the world you know", inline=False)
        embed.add_field(name="Arena", value="battle your foes in an arena bloodshed", inline=False)
        await client.send_message(message.channel, embed=embed)
        global gamestart
        gamestart = 1
    elif message.content.startswith('!openworld') and gamestart == 1:
        embed = discord.Embed(title="World Pick", description="which world do you choose?",color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/456208224190857238/pixel_art_earth_by_gpbrck-d8vb4hz.png")
        embed.add_field(name="Plantaria", value="the spawn place of everyone", inline=False)
        if atlunl == 1:
            embed.add_field(name="Atlantis", value="the waters that are wavy", inline=False)
        await client.send_message(message.channel, embed=embed)
    elif message.content.startswith('!arena') and gamestart == 1:
        embed = discord.Embed(title="Arena Opponents", description="lobby where all the cool kids hang out",color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/456210559411552279/startups_from_hell__underground_arena.png")
        emb.add_field(name="fighters", value="not completed yet", inline=False)
        await client.send_message(message.channel, embed=embed)
@client.event
async def on_ready():
    print("im up and running")

client.run("NDQzMTY3MTY0NDU5OTA5MTIw.DgHKyQ.suQH5_Qg6FnxDykaxbdAbkEnXO0")
