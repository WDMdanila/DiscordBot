import os
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'{member.name} is ready to suck some dicks!')


@bot.command()
@commands.has_role(695621674464182302)
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
@commands.has_role(695621674464182302)
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")


@bot.command()
@commands.has_role(695621674464182302)
async def reload(ctx, extension):
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
