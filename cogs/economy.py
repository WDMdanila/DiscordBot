import discord
from discord.ext import commands


class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.members = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print('Economy cog is online')

    @commands.command(name='load_economy')
    @commands.has_role(695621674464182302)
    async def get_members(self, ctx):
        for member in ctx.guild.members:
            self.members[member.id] = 100


def setup(bot):
    bot.add_cog(Economy(bot))
