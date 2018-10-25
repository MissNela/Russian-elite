import discord
from discord.ext import commands
import asyncio
import os
import time

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('This message shall view only bots Owner Mrs.Nela')
	print('----------------------------')

@bot.command()
async def ping():
	await bot.say(':ping_pong: Why are you trying to ping me??')
	await bot.say('Dont try it.. You dont have any chance. Heheh')
  
bot.run('TOKEN')

