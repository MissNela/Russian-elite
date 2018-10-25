import discord
from discord.ext import commands
import asyncio

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

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
    pass
		
bot.run('NTAzMzgxMDM5ODcyMjEyOTky.Dq2JtA.b6b4lSkwcV9_-e8p1wFyH8nZwtE')
