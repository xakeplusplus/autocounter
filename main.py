import discord
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix=">", self_bot = False)

token = "" # your dc token
channelToSendInID = "" # >setchannel in the channel to set it or just paste it here
otherGuyUsername = "" # the username of the guy u doing it with
lastNum = 0

@bot.event
async def on_ready():
    print("Auto-Counter is on! Prefix is '>'")


@bot.command()
async def setchannel(ctx):
    await ctx.message.delete()

    global channelToSendInID

    channelToSendInID = ctx.channel.id
    
    channelToSendInID = int(channelToSendInID)

    f.close()

    print(f"Channel Set To: {channelToSendInID}")

async def count():
    channelToSendIn = bot.get_channel(channelToSendInID)
    await channelToSendIn.send(f"{lastNum + 1}")

@bot.event
async def on_message(message: discord.Message):
    if (message.author == bot.user and message.content == ">setchannel"):
        # await ctx.message.delete()

        global channelToSendInID
        channelToSendInID = message.channel.id
        channelToSendInID = int(channelToSendInID)
        print(f"Channel Set To: {channelToSendInID}")

    if (message.channel == bot.get_channel(channelToSendInID)):
        if (str(message.author) == otherGuyUsername):
            global lastNum
            lastNum = int(message.content)
            await count()
            
        
    await bot.process_commands(message)


bot.run(token, bot=False)