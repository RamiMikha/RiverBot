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

        #imports the commands once the bot is ready
        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name !="__init.py":
                #loads the command file but ignores the ".py"
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")


   #ctx gettings a bunch on context from discord.py 
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

 #runs the bot from the api saved in settings
    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()