"""
Economy cog
"""

from discord.ext import commands


class Economy(commands.Cog):
    """
    Economy cog, under development
    """

    def __init__(self, bot):
        self.bot = bot
        self.members = {}

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Action to be done when Economy cog is loaded

        :return: None
        """

        print('Economy cog is online')

    @commands.command(name='load_economy')
    @commands.has_role(695621674464182302)
    async def get_members(self, ctx):
        """
        Get server members

        :param ctx: context of command
        :return: None
        """

        for member in ctx.guild.members:
            self.members[member.id] = 100

    # TODO: Develop actual economy cog


def setup(bot):
    """
    Setup a cog

    :param bot: bot for which the cog is set up
    :return: None
    """

    bot.add_cog(Economy(bot))
