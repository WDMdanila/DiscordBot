"""Gaming cog"""
from discord.ext import commands

SYMBOLS = ['@', '#', '$', '&', '?', '%']


class Gaming(commands.Cog):
    """Gaming cog, under development"""
    def __init__(self, bot):
        self.started = False
        self.players = {}
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Action to be done when Gaming cog is loaded"""
        print('Gaming cog is online')

    @commands.command(aliases=['game'])
    @commands.has_role(695621674464182302)
    async def start_game(self, ctx, symbol=None):
        """Start a game

        :param ctx: context of command
        :param symbol: player symbol
        :return: None
        """
        pass

    # TODO: Develop actual gaming cog


def setup(bot):
    """Setup a cog

    :param bot: bot for which the cog is set up
    :return: None
    """
    bot.add_cog(Gaming(bot))
