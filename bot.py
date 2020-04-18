"""Main body of the bot, all the functionality is imported using cogs"""
import os
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    """Action to be done when bot is loaded"""
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    """Bot's reaction when someone joins server

    :param member: newly joined member
    :return: None
    """
    await member.create_dm()
    await member.dm_channel.send(f'{member.name} is ready to suck some dicks!')


@bot.command()
@commands.has_role(695621674464182302)
async def load(ctx, extension):
    """Load an extension

    :param ctx: context of command (unused)
    :param extension: extension name
    :return: None
    """
    bot.load_extension(f"cogs.{extension}")


@bot.command()
@commands.has_role(695621674464182302)
async def unload(ctx, extension):
    """Unload an extension

    :param ctx: context of command (unused)
    :param extension: extension name
    :return: None
    """
    bot.unload_extension(f"cogs.{extension}")


@bot.command()
@commands.has_role(695621674464182302)
async def reload(ctx, extension):
    """Reload an extension

    :param ctx: context of command (unused)
    :param extension: extension name
    :return: None
    """
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")


if __name__ == '__main__':
    with open('config.json') as cfg:
        config = json.load(cfg)

    TOKEN = config['token']

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
    bot.run(TOKEN)
