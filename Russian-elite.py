import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
from itertools import cycle
import time


my_token = 'NTAzMzgxMDM5ODcyMjEyOTky.Dq2JtA.b6b4lSkwcV9_-e8p1wFyH8nZwtE'

client = commands.Bot(command_prefix = '>')

client.remove_command('help')
status = ['>help for commands', 'With code', "Stabbing Mrs.Nela","With developer Mrs.Nela"]

players = {}


async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name =current_status))
        await asyncio.sleep(60)
    
@client.event
async def on_ready():
    print('The bot is online and connected with Discord.')

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
   
    embed = discord.Embed(color = discord.Color.orange()

    
    embed.add_field(name = '>questions', value = 'Use in commands only. Also it shows what is format in #questions', inline = False)
    embed.add_field(name = '>clear', value = 'Moderators only! (Defaultly on 10)', inline = False)
    embed.add_field(name = '>say', value = 'Let bot to say something', inline = False)
    embed.add_field(name = 'Ping', value = 'Pong!', inline = False)
    await client.send_message(author,embed=embed)
    await client.say('📨 Check DMs For Information')
        

    
@client.event
async def on_member_join(member):
    await client.send_message(member, "Welcome to Communism Age! read #rules and #docs!")
    
    


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='USA immigrent')
    await client.add_roles(member, role)





    
@client.command()
async def questions():
    embed = discord.Embed(
        title = 'Questions Format:',
        description = """Username:  
        Question:    
        Question Meant For:'
        """,

        color = discord.Color.purple()

       
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


@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


@client.command(pass_context = True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context = True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context = True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context = True)
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


@client.command(pass_context=True)
async def serverinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
@client.event
async def on_message(message):
    
    await client.process_commands(message)
    if message.content.startswith('Ping'):
        userID = message.author.id
        await client.send_message(message.channel, '<@%s> :ping_pong: **__Pong!__**' % (userID))
        




   

    

    

    

        
@client.command()
async def gamer():
    await bot.send_message('@GamerHDlol1#2251')
    await bot.send_message('@GamerHDlol1#2251')
    await bot.send_message('@GamerHDlol1#2251')
    await bot.s
    



client.loop.create_task(change_status())

client.run(my_token)

