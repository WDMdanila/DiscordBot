import discord
from discord.ext import commands


class Game:
    def __init__(self, player):
        self.started = False
        self.players = [player]


class Gaming(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.members = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print('Gaming cog is online')

    @commands.command(aliases=['game'])
    @commands.has_role(695621674464182302)
    async def start_game(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Gaming(bot))
