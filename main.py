import settings
import discord
from discord.ext import commands
import random

def run():
    """
    Set up for the bot, getting the intents and commands from discord.py
    Setting the prefix
    Runs the bot
    Has some commands
    """
    print(settings.DISCORD_API_SECRET)
    intents = discord.Intents.default()
    #allows bot to take information from messages
    intents.message_content = True
    bot = commands.Bot(command_prefix=".", intents=intents)

    #uses events
    #Once the bot is ready it runs the on_ready function
    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("Bot is Ready!")
        print("--------------------")


   #ctx gettings a bunch of context from discord.py 
    @bot.command(
        #this allows you to access the command with different alisases
        aliases=["p"],
        help="This gives help about the command in a specific message for each command",
        description="This gives a longer description about the command in a specific message for each command",
        brief="This gives a short description in the list of commands"
        #enabled=False would disable the command
        #hidden=True would not show the command in the help list
    )
    async def ping(ctx):
        await ctx.send("pong")
    
    #the second premis takes in what the user says after the command word
    #the astricts allows you to take in a infinite amount of word the user says after the command
    @bot.command()
    async def say(ctx, *what ):
        try:
            await ctx.send(" ".join(what))
        except Exception:
            await ctx.send("Say What?")


    @bot.command(
        brief = "Picks from options given at random",
        help = "The bot will pick at random from the option it is given. Make sure the choices are separated by commas"
    )
    async def choice(ctx, *options):
        choices = " ".join(options).split(",")
        await ctx.send(random.choice(choices))

 
    #runs the bot from the api saved in settings
    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()
