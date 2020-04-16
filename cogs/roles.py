import discord
import random
from discord.ext import commands


class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Roles cog is online')

    @commands.command(aliases=['отпетушить'])
    async def rape(self, ctx, *targets: discord.Member):
        end = [
            ', хотя он вроде и так петух...',
            ', готовь мыло.',
            ', тобі пізда.',
            ', хуя себе, вот это ведро...',
            ', закинул вялого за щеку.',
            ', лови мягкого под губу.',
            ', мой попу.',
            ''
        ]

        roles = {ctx.guild.get_role(695621674464182302), ctx.guild.get_role(695933575828209704)}

        if set(ctx.message.author.roles) & roles:
            text = ', '.join([target.mention for target in targets])
            await ctx.send(f"{ctx.message.author.mention} начинает петушить {text} {random.choice(end)}")
        else:
            await ctx.send(
                f"{ctx.message.author.mention} сейчас будет сосать. Только залупочесы могут петушить кого-то!")

    @commands.command(aliases=['хромосома'])
    async def chromosome(self, ctx, *targets: discord.Member):
        end = [
            ', тебе она нужнее',
            ', хотя вроде ничего не изменилось.',
            ', тобі пізда.',
            ', тут явно перебор.',
            ', теперь ты аутист. (не то что бы это было новостью для тебя)',
            ', лови ядро.',
            ', добро пожаловать в клуб.',
            ''
        ]

        roles = {ctx.guild.get_role(695621674464182302), ctx.guild.get_role(695636250140344442)}

        if set(ctx.message.author.roles) & roles:
            text = ', '.join([target.mention for target in targets])
            await ctx.send(f"{ctx.message.author.mention} подарил хромосому {text} {random.choice(end)}")
        else:
            await ctx.send(f"{ctx.message.author.mention} сейчас будет сосать. Только овощи могут подарить хромосому!")

    @commands.command(aliases=['пакет'])
    async def trash(self, ctx, *targets: discord.Member):
        end = [
            ', а так даже красивее',
            ', хотя вроде ничего не изменилось.',
            ', тобі пізда.',
            ', пахнуть стало лучше.',
            ', и голову мыть не нужно. (хотя ты и не собирался)',
            ', лови ядро.',
            ', добро пожаловать в клуб.',
            ''
        ]

        roles = {ctx.guild.get_role(695621674464182302), ctx.guild.get_role(695614165087420416)}

        if set(ctx.message.author.roles) & roles:
            text = ', '.join([target.mention for target in targets])
            await ctx.send(f"{ctx.message.author.mention} надел на голову {text} пакет {random.choice(end)}")
        else:
            await ctx.send(
                f"{ctx.message.author.mention} сейчас будет сосать. Только мусор может надеть пакет на голову!")

    @commands.command(aliases=['я'])
    async def change_my_role(self, ctx, role):
        roles = {
            'овощ': ctx.guild.get_role(695636250140344442),
            'мусор': ctx.guild.get_role(695614165087420416),
            'залупочес': ctx.guild.get_role(695933575828209704)
        }

        if role in roles:
            await ctx.author.remove_roles(ctx.guild.get_role(695636250140344442),
                                          ctx.guild.get_role(695614165087420416),
                                          ctx.guild.get_role(695933575828209704))
            await ctx.author.add_roles(roles[role])
            await ctx.send(f"{ctx.message.author.mention}, поздравляю, теперь ты {role}!")
        else:
            await ctx.send(f"{ctx.message.author.mention}, соси письку!")

    @commands.command(aliases=['ты'])
    async def change_role(self, ctx, member: discord.Member, role):
        roles = {
            'овощ': ctx.guild.get_role(695636250140344442),
            'мусор': ctx.guild.get_role(695614165087420416),
            'залупочес': ctx.guild.get_role(695933575828209704)
        }

        if ctx.guild.get_role(695621674464182302) not in member.roles:
            if role in roles:
                await member.remove_roles(ctx.guild.get_role(695636250140344442),
                                          ctx.guild.get_role(695614165087420416),
                                          ctx.guild.get_role(695933575828209704))
                await member.add_roles(roles[role])
                await ctx.send(f"{member.mention}, поздравляю, теперь ты {role}!")
            else:
                await ctx.send(f"{ctx.message.author.mention}, соси письку!")
        else:
            await ctx.send(f"{ctx.message.author.mention}, соси пипиську.")


def setup(bot):
    bot.add_cog(Roles(bot))
