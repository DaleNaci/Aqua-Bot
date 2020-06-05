import asyncio

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Color, Embed

from MinecraftServer import MinecraftServer


Client = discord.Client()
bot = commands.Bot(command_prefix = "!")

bot.remove_command("help")

server = MinecraftServer("x337.ddns.net:25661")


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.command()
async def smp(ctx):
    data = server.server_lookup()

    desc = ""

    for player in data[1]:
        desc += "`{}`\n".format(player)

    embed = Embed(
                title="Players",
                color=Color.blue(),
                description=desc
    )

    await ctx.send(embed=embed)


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()

bot.run(token)
