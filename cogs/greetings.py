import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief = "Say hello to River"
    )
    async def hello(self, ctx):
        user = ctx.message.author
        await ctx.send(f"Hello {user} my name is River. It is nice to meet you!") 

async def setup(bot):
    await bot.add_cog(Greetings(bot))