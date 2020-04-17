import random
from discord.ext import commands


class Gambling(commands.Cog):
    """
    Gambling cog, has some related commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Action to be done when Gambling cog is loaded

        :return: None
        """

        print('Gambling cog is online')

    @commands.command(aliases=['ролл', 'рандом', 'random'])
    async def roll(self, ctx, *args):
        """
        Rolls a random number in specified range (if not specified range is 0 to 99)
        Allows member to make a prediction of a number

        :param ctx: context of command
        :param args: arguments, range may be in style "1-200", prediction - number.
        :return: None
        """

        end = {
            True: ['повезло...', 'счастливчик!'],
            False: ['лалка.', 'ебать ты лох!']
        }
        try:
            if len(args) == 2:
                ran = args[0].split('-')
                n = random.randint(int(ran[0]), int(ran[1]))
                x = int(args[1])
            else:
                n = random.randint(0, 100)
                x = int(args[0])
            await ctx.send(f"Выпало: **{n}**\n{ctx.message.author.mention} {random.choice(end[n == x])}")
        except:
            try:
                ran = args[0].split('-')
                n = random.randint(int(ran[0]), int(ran[1]))
                await ctx.send(f"Выпало: **{n}**")
            except:
                await ctx.send(f"{ctx.message.author.mention} сломал казино, мудак")

    @commands.command(aliases=['выбор', 'выбери'])
    async def choose(self, ctx, *args):
        """
        Choose from a list of words sent by a member. May accept sentences if escaped with double quotes

        :param ctx: context of command
        :param args: words or sentences to choose from
        :return: None
        """

        if len(args) < 2:
            await ctx.send(f"{ctx.message.author.mention} слишком мало вариантов для выбора.")
        else:
            choice = ', '.join(args)
            await ctx.send(f"**{choice}**\nЯ выбираю: **{random.choice(args)}**")


def setup(bot):
    """
    Setup a cog

    :param bot: bot for which the cog is set up
    :return: None
    """

    bot.add_cog(Gambling(bot))
