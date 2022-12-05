from discord.ext import commands
import random

@commands.command(
        
    brief = "Picks from options given at random",
    help = "The bot will pick at random from the option it is given. Make sure the choices are separated by commas"
    )
async def choice(ctx, *options):
    choices = " ".join(options).split(",")
    await ctx.send(random.choice(choices))

async def setup(bot):
    bot.add_command(choice)