import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
            
        brief = "Picks from options given at random",
        help = "The bot will pick at random from the option it is given. Make sure the choices are separated by commas"
        )
    async def choice(self, ctx, *options):
        choices = " ".join(options).split(",")
        await ctx.send(random.choice(choices))


    @commands.command(
        brief = "Play a rock, paper, scissors game with the bot",
        help = "The bot will pick at random from rock, paper, scissors. Will then compare with your choice and give you the results")
    async def rps(self, ctx, choice: str):
        # get user's choice
        choice = choice.lower()
    
        if choice not in ["rock", "paper", "scissors"]:
            await ctx.send("Invalid choice! Please choose rock, paper, or scissors.")
        

        # generate bot's choice
        bot_choice = random.choice(["rock", "paper", "scissors"])

        # determine the winner
        if choice == bot_choice:
            await ctx.send(f"We both chose {choice}. It's a tie!")
        elif (choice == "rock" and bot_choice == "scissors") or (choice == "paper" and bot_choice == "rock") or (choice == "scissors" and bot_choice == "paper"):
            await ctx.send(f"You chose {choice} and I chose {bot_choice}. You win!")
        else:
            await ctx.send(f"You chose {choice} and I chose {bot_choice}. I win!")

    @commands.command(
    brief = "The bot will repear whatever you type after the command"
    )
    async def say(self, ctx, *what ):
        try:
            await ctx.send(" ".join(what))
        except Exception:
            await ctx.send("Say What?")

async def setup(bot):
    await bot.add_cog(Fun(bot))


    
