"""Admin cog"""

import random
import discord
from discord.ext import commands


class Admin(commands.Cog):
    """Admin cog which has admin and some utility commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Action to be done when Admin cog is loaded"""
        print('Admin cog is online')

    @commands.command(aliases=['очистить'])
    @commands.has_role(695621674464182302)
    async def clear(self, ctx, num: int):
        """Purge num messages in the channel

        :param ctx: context of command
        :param num: number of messages to be purged
        :return: None
        """
        await ctx.channel.purge(limit=num)

    @commands.command(aliases=['пидорнуть'])
    @commands.has_role(695621674464182302)
    async def fuck_off(self, ctx, member: discord.Member):
        """Move a memeber to a Faggots cast, remove all rights

        :param ctx: context of command
        :param member: member to be moved
        :return: None
        """
        await member.remove_roles(ctx.guild.get_role(695636250140344442),
                                  ctx.guild.get_role(695614165087420416),
                                  ctx.guild.get_role(695933575828209704))
        tmp = await ctx.guild.create_voice_channel('TMP')
        try:
            await member.move_to(tmp, reason='Сори, ты отброс')
        finally:
            await tmp.delete()
        await member.add_roles(ctx.guild.get_role(696412698744717363))
        await ctx.send(f"{member.mention}, теперь ты отброс и чмошник!")

    @commands.command(aliases=['нахуй'])
    @commands.has_role(695621674464182302)
    async def kick_from_voice(self, ctx, member: discord.Member):
        """Kick a member from a voice chat

        :param ctx: context of command
        :param member: member to be kicked out
        :return: None
        """
        tmp = await ctx.guild.create_voice_channel('TMP')
        try:
            await member.move_to(tmp, reason='Сори, ты отброс')
        finally:
            await tmp.delete()
        await ctx.send(f"{member.mention}, пошел нахуй!")

    @commands.command(aliases=['поднять'])
    @commands.has_role(695621674464182302)
    async def fuck_on(self, ctx, member: discord.Member):
        """Elevate user rights back to the normal

        :param ctx: context of command
        :param member: member to be elevated
        :return: None
        """
        await member.remove_roles(ctx.guild.get_role(696412698744717363))
        await member.add_roles(random.choice([ctx.guild.get_role(695636250140344442),
                                              ctx.guild.get_role(695614165087420416),
                                              ctx.guild.get_role(695933575828209704)]))
        await ctx.send(f"{member.mention}, поздравляю, теперь ты не отброс!")

    @commands.command(aliases=['испугать'])
    @commands.has_role(695621674464182302)
    async def scare(self, ctx):
        """Drop a random message using /tts

        :param ctx: context of command
        :return: None
        """
        scares = ['Raaaaawr',
                  'WOOOOOHOOOO',
                  'Batya pidor',
                  'Suck a dick',
                  'BOOOOOO',
                  'Whyyyyyyyyy?',
                  'Do you love me?',
                  'Time to suck',
                  'Sunia pidor!\nGegegegegege']
        await ctx.send(f"{random.choice(scares)}!", tts=True)


def setup(bot):
    """Setup a cog

    :param bot: bot for which the cog is set up
    :return: None
    """
    bot.add_cog(Admin(bot))
