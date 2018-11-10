#Before you hack my bot again I want you to not do this Im a small coder and my bot is not in any other servers than 2.

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = '>')
client.remove_command('help')

players = {}

status = ['>help for commands', 'With code', "Stabbing Mrs.Nela","With developer Mrs.Nela"]

players = {}



@client.event
async def on_ready():
    print("The bot is online and connected with Discord!")

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.startswith('>help'):
        await client.send_message(message.channel, "Here is you're ``Help`` type >helpcategory`` for more help.")
    
   
@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str):
        await client.send_message(userName, "You have been warned for: {}".format(message)) 
        await client.say("warning {0} Has Been Warned! Warning Reason : {1} ".format(userName,message))
        pass

        

    
@client.event
async def on_member_join(member):
    await client.send_message(member, "Welcome to Communism Age! read #rules and #docs!")
    
@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("You haven't specified a role! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("{} role has been added to {}.".format(role, user))

        if role in user.roles:
            await client.remove_roles(user, role)
            return await client.say("{} role has been removed from {}.".format(role, user))
 
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def norole(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Do not ask for promotions check Rules again.')
    return


@client.command(pass_context=True)
async def help():
    embed = discord.Embed(
        title = "Help",
        description = """
        **``Here is all what I could find.``
        :wrench: ``>helpoverall`` :wrench:
          :loud_sound: ``>helpvoice`` :loud_sound:
          :joy: ``>helpfun`` :joy:
          :hammer: ``>helpmoderation`` :hammer:
        
        __```DEVELOPER COMMANDS```__
        ``>dhelp``**
        """,
        
        color = discord.Color.orange()
       
)
   
    await client.say(embed=embed)
    
@client.command(pass_context = True)
async def play(ctx, *, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    try:
        vc = await client.join_voice_channel(voice_channel)
        msg = await client.say("Loading...")
        player = await vc.create_ytdl_player("ytsearch:" + url)
        player.start()
        await client.say("Succesfully Loaded ur song!")
        await client.delete_message(msg)
    except Exception as e:
        print(e)
        await client.say("Reconnecting")
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                await x.disconnect()
                nvc = await client.join_voice_channel(voice_channel)
                msg = await client.say("Loading...")
                player2 = await nvc.create_ytdl_player("ytsearch:" + url)
                player2.start()


@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not playing anyting???!")

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def joinvoice(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await client.join_voice_channel(channel)

    
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='**Hope you will be active here. Check Our server rules and never try to break any rules. ',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='Navy of SCLD', name='join-leave')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check <#474572305192845312> and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)
  
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






@client.command()
async def say(*args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await client.say(output)


@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await client.say('**He is mod/admin and i am unable to kick him/her**')
        return
    
    try:
        await client.kick(user)
        await client.say(user.name+' was kicked. Good bye '+user.name+'!')
        await client.delete_message(ctx.message)

    except discord.Forbidden:
        await client.say('Permission denied.')
        return

    
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):

    if user.server_permissions.ban_members:
        await client.say('**He is mod/admin and i am unable to ban him/her**')
        return

    try:
        await client.ban(user)
        await client.say(user.name+' was banned. Good bye '+user.name+'!')

    except discord.Forbidden:

        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('ban failed.')
        return		 



@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     


async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)

    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await client.say('Ban list is empty.')
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await client.say('Permission denied.')
        return
    except discord.HTTPException:
        await client.say('unban failed.')
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
    





client.run(os.getenv("BOT_TOKEN"))

