import discord

from discord.ext import commands
from discord.ext.commands import bot

import asyncio
from itertools import cycle
import time


my_token = 'NTAzMzgxMDM5ODcyMjEyOTky.DrtSQQ.j8TNVzKT8KAKEVEjlHJQuzVAz_o'



client = commands.Bot(command_prefix = '>')
client.remove_command('help')

players = {}

status = ['>help for commands', 'With code', "Stabbing Mrs.Nela","With developer Mrs.Nela"]

players = {}



@client.event
async def on_ready():
    print('The bot is online and connected with Discord.')



    

        

    
@client.event
async def on_member_join(member):
    await client.send_message(member, "Welcome to Communism Age! read #rules and #docs!")
    
    




@client.command(pass_context=True)
async def help():
    embed = discord.Embed(
        title = "Help",
        description = """
        **>questions - shows Questions format
        >botsugformat - Shows bot suggestions format
        >serversuggestions - Shows Server suggestions format
        >clear - Cleares A amount of messages (Default = 10)
        __VOICE (Not done)__
        >join - Joins a Voice Channel
        >play - Play something!
        >pause - Pauses a music
        >resume - Resumes a Music!
        >leave - Leaves a Voice Channel!
        >stop - Stops playing music!
        __FUN (some are not done)__
        >say - Make bot something to say!
        >command_idea_here
        Ping - Bt will say somethig!
        Bang Bang! - Bot will say something!
        >serverinfo - get Info about our server!
        __MODERATION (NOT DONE)__
        >kick - Kicks a user!
        >ban - Bans a User!
        >mute - Mutes a user!
        >unmute - Unmutes a user!
        __DEVELOPER COMMANDS__
        >dhelp**
        """,
        
        color = discord.Color.dark_red()
)
    await client.say(embed=embed)
        
@client.command(pass_context=True)
async def dhelp():
    if message.author.id: "342364288310312970"
      embed = discord.Embed(
          title = "Developer Commands",
          description = """**
          __DEVELOPER EARLY ACCES__
          _No commands has been done yet._
          """,
          
          color = discord.Color.light_blue()
      )
        await client.say(embed=embed)
        else:
            await client.say(message.channel, "You are not a Developer!"



    
@client.command(pass_context=True)
async def questions():
    embed = discord.Embed(
        title = 'Questions Format:',
        description = """
     Username:  
     Question:    
     Question Meant For:
        """,

        color = discord.Color.green()

       
)
    
    await client.say(embed=embed)


@client.command(pass_context=True)
async def botsugformat():
    embed = discord.Embed(
        title = 'Bot suggestions Format:',
        description = """
     Username: (Your username)
     Rank: (Higest rank)
     Suggestion: (Your suggestion)

        """,

        color = discord.Color.orange()

       
)
    
    await client.say(embed=embed)
    

@client.command(pass_context=True)
async def serversuggestions():
    embed = discord.Embed(
        title = 'Server Suggestions Format:',
        description = """
        Username:(Discord username)
     Rank: (Your higest rank)
     Suggestion: (Your server suggestion)
     How could it help: (How could this help)
        """,

        color = discord.Color.blue()

       
)
    
    await client.say(embed=embed)

@client.command(pass_context = True)
async def clear(ctx, amount = 10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')


@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    embed = discord.Embed(
        title = 'Voice channel',
        description = 'commands for the voice channel.',
        colour = discord.Colour.blue()
    )

    embed.add_field(name = '>play', value = 'play youtube audio with url', inline = False)
    embed.add_field(name = '>pause', value = 'pauses audio', inline = False)
    embed.add_field(name = '>resume', value = 'resumes audio', inline = False)
    embed.add_field(name = '>leave', value = 'leave voice channel', inline = False)
    
    await client.say(embed=embed)
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()



@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()



@client.command()
async def say(*args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await client.say(output)



    
@client.event
async def on_message(message):
    
    await client.process_commands(message)
    if message.content.startswith('Ping'):
        userID = message.author.id
        await client.send_message(message.channel, '<@%s> :ping_pong: **__Pong!__**' % (userID))
        
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.startswith('Bang Bang!'):
        await client.send_message(message.channel, 'x_x _Dying_. why did you shot me? x_x')




@client.command()
async def serverinfo():
    embed = discord.Embed(
        title = "Server Info",
        description = """
        This is server info. here you can read about server.
        Minister (Owner): Mrs.Nela
        Deputy Minister: Kazuto Kirigaya
        Deputy Minister: GamerHDlol1
        ================================
        SERVER INFO
        This server is Role Play server. 3 warnings = Mute (@in Gulag)
        6 warnings is Mute on 24h (@in Gulag)
        9 warnings is Kick
        12 warnings = Ban
        13 warnings = Perma ban
        currect Bots: 2
        users: 6
        I hope you will enjoy your stay!
        """,
        colour = discord.Colour.green()
)
    await client.say(embed=embed)
        
        
                        

    

        
@client.command()
async def gamer():
    await bot.send_message('@GamerHDlol1#2251')
    await bot.send_message('@GamerHDlol1#2251')
    await bot.send_message('@GamerHDlol1#2251')
    await bot.s
    





client.run(my_token)

