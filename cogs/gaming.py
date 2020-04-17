import random
import discord
from discord.ext import commands

SYMBOLS = ['@', '#', '$', '&', '?', '%']


class Gaming(commands.Cog):

    def __init__(self, bot):
        self.started = False
        self.players = {}
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Gaming cog is online')

    @commands.command(aliases=['game'])
    @commands.has_role(695621674464182302)
    async def start_game(self, ctx, symbol=None):
        pass


def setup(bot):
    bot.add_cog(Gaming(bot))
