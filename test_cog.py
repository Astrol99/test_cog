import discord
from discord.ext import commands

class Test:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hey {ctx.author.mention}!")

def setup(bot):
    bot.add_cog(Test(bot))