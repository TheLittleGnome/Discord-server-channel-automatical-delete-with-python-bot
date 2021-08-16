from discord.ext import commands
import discord

client = commands.Bot(command_prefix = 'for example: !?')

@client.event
async def on_ready():
    guild = client.get_guild(server ID)
    delete_channel_1 = discord.utils.get(guild.channels, name="first_channel_name")
    delete_channel_2 = discord.utils.get(guild.channels, name="another_channel_name")
    #as many times as necessary (Ctrl+C and Ctrl+V)

    print('command line comment, this is alternative function')
    if not  delete_channel_1 is None:
        await delete_channel_1.delete()
    if not  delete_channel_2 is None:
        await delete_channel_2.delete()
    #as many times as necessary (Ctrl+C and Ctrl+V)

client.run("bot token here")
