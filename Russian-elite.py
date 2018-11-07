#Before you hack my bot again I want you to not do this Im a small coder and my bot is not in any other servers than 2.

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



@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str):
        await bot.send_message(userName, "You have been warned for: {}".format(message)) 
        await bot.say("warning {0} Has Been Warned! Warning Reason : {1} ".format(userName,message))
        pass

        

    
@client.event
async def on_member_join(member):
    await client.send_message(member, "Welcome to Communism Age! read #rules and #docs!")
    
    




@client.command(pass_context=True)
async def help():
    embed = discord.Embed(
        title = "Help",
        description = """
        **:wrench: ``>helpoverall`` :wrench:
          :loud_sound: ``>helpvoice`` :loud_sound:
          :joy: ``>helpfun`` :joy:
          :hammer: ``>helpmoderation`` :hammer:
        
        __```DEVELOPER COMMANDS```__
        **``>dhelp``**
        """,
        
        color = discord.Color.orange()
       
)
    await client.say(embed=embed)
    
  
@client.command(pass_context=True)
async def helpoverall():
    embed = discord.Embed(
        title = "Server Commands",
        description = """
        **_Here you can see all srrver commands._
        >questions - __Shows a questions format. Use in bot commands.__
        >botsugformag - __Shows a bot suggestions format. Use in bot commands.__
        >serversuggetions - __Shows a Server Suggestions format. Use in bot commands.__**
        """,
        color = discord.Color.dark_blue()
)
   
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def helpvoice():
    embed = discord.Embed(
        title = "Voice Commands Not done",
        description = """
        ***__THIS COMMANDS ARENT DONE. Here are all Voice/Music Commands!__***
       ** >join - __Joins a Voice channel.__
        >play - __Play a music!__
        >pause - __Pause music!__
        >resume - __Resumes music!__
        >stop - __Stops a music!__
        >leave - __Leaves a Voice channel!__
        **
        """,
        color = discord.Color.blue()
) 
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpfun():
    embed = discord.Embed(
        title = "Fun Commands",
        description = """
      **__Here are All commands for Fun. Some may not work.__
      >say - __Make the bot say something!__
      ping - __bot will say something ;)__
      Bang Bang! - __You will kill the bot!__**
        """,
        color = discord.Color.dark_green()
) 
    await client.say(embed=embed)
        
@client.command(pass_context=True)
async def dhelp():


    embed = discord.Embed(
          title = "Developer Commands",
          description = """**
          __DEVELOPER EARLY ACCES__
          _No commands has been done yet._
          """,
          
          color = discord.Color.dark_blue()
)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def helpmoderation():
    embed = discord.Embed(
        title = "Moderation Help",
        description = """
        **__MODERATION HELP THEY ARENT DONE! ONLY CLEAR WORKS__**
        **>clear - __Clears a selected ammout of messages. Default 10.__
        >warn - __Warns a User. Not done.__
        >ban - __Bans a user. Not done.__
        >kick - __Kicks a user. Not done.__
        >mute - __Mutes a user. Not done.__
        >unmute - __Unmutes a user. Not done.__
        """,
        color = discord.Color.green()
)
    await client.say(embed=embed)
        
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


@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await bot.say('He/she is mod/admin and i am unable to kick him/her')
        return
    
    try:
        await bot.kick(user)
        await bot.say(user.name+' was kicked. Good bye '+user.name+'!')
        await bot.delete_message(ctx.message)

    except discord.Forbidden:
        await bot.say('Permission denied.')
        return
    
@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx, user:discord.Member):

    if user.server_permissions.ban_members:
        await bot.say('He/she is mod/admin and i am unable to ban him/her')
        return
        
    if not user:
        await bot.say("Please specify a user to ban")

    try:
        await bot.ban(user)
        await bot.say(user.name+' was banned. Good bye '+user.name+'!')

    except discord.Forbidden:
        await bot.say('Permission denied. You need ban members permission')
        return

    except discord.HTTPException:
        await bot.say('ban failed.')
        return
    
@client.event
async def on_message(message):
    
    await client.process_commands(message)
    if message.content.startswith('Ping'):
       
        await client.send_message(message.channel, ':ping_pong: **__Pong!__**' % (userID))
        
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

