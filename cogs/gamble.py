import random
import discord
from discord.ext import commands


class Gamble(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Gamble cog is online')

    @commands.command(aliases=['ролл', 'рандом', 'random'])
    async def roll(self, ctx, *args):
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
        if len(args) < 2:
            await ctx.send(f"{ctx.message.author.mention} слишком мало вариантов для выбора.")
        else:
            choice = ', '.join(args)
            await ctx.send(f"**{choice}**\nЯ выбираю: **{random.choice(args)}**")


def setup(bot):
    bot.add_cog(Gamble(bot))
