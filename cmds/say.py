from discord.ext import commands

#the second premis takes in what the user says after the command word
#the astricts allows you to take in a infinite amount of word the user says after the command
@commands.command()
async def say(ctx, *what ):
    try:
        await ctx.send(" ".join(what))
    except Exception:
        await ctx.send("Say What?")


async def setup(bot):
    bot.add_command(say)