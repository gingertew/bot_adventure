import discord.ext
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()

questcount = 0
questint = 0
quest1 = 1
quest2 = 2
quest3 = 3
quest4 = 4
quest5 = 5
quest6 = 6
quest = ['cut down a tree','kill a bear']

@client.event
async def on_message(message):
    if message.content.startswith('!givequest'):
        embed = discord.Embed(title="Quest", description="Here's your quest", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/456888981234122763/quest-for-g-book.png")
        questint += 1
        if questint == quest1:
            quest1 = random.choice(quest)
            embed.add_field(name = 'quest' + str(questint), value = quest1, inline = False)
        elif questint == quest2:
            quest2 = random.choice(quest)
            embed.add_field(name = 'quest' + str(questint), value = quest2, inline = False)
        elif questint == quest3:
            quest3 = random.choice(quest)
            embed.add_field(name = 'quest' + str(questint), value = quest3, inline = False)
        elif questint == quest4:
            quest4 = random.choice(quest)
            embed.add_field(name = 'quest' + str(questint), value = quest4, inline = False)
        elif questint == quest5:
            quest5 = random.choice(quest)
            embed.add_field(name = 'quest' + str(questint), value = quest5, inline = False)
        elif questint == quest6:
            quest6 = random.choice(quest)
            embed.add_field(name = 'quest' + str(questint), value = quest6, inline = False)
        await client.send_message(message.channel, embed=embed)
    elif message.content.startswith('!quest'):
        embed = discord.Embed(title="Quest", description="Here's a list of your quests", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/443166782086184970/456888981234122763/quest-for-g-book.png")
        while questint != questcount:
            embed.add_field(name = str(questname), value = possibleque, inline = False)
            questcount += 1
            if questcount == questint:
                break 
        await client.send_message(message.channel, embed=embed)
@client.event
async def on_ready():
    print("im up and running")

client.run("NDQzMTY3MTY0NDU5OTA5MTIw.DgHKyQ.suQH5_Qg6FnxDykaxbdAbkEnXO0")
