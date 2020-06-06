import asyncio

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Color, Embed

from MinecraftServer import MinecraftServer


Client = discord.Client()
bot = commands.Bot(command_prefix = "!")

bot.remove_command("help")

with open("ip.txt", "r") as f:
    lines = f.readlines()
    ip = lines[0].strip()

server = MinecraftServer(ip)


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


@bot.command()
async def help(ctx):
    command_descs = {
        "!help": "Provides information about all commands.",
        "!smp": "List users currently on the Aqua SMP server."
    }

    desc = ""
    for k, v in command_descs.items():
        desc += "`{}`: {}\n".format(k, v)

    embed = Embed(
                title="Commands",
                color=Color.blue(),
                description=desc
    )

    await ctx.send(embed=embed)


with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0].strip()

bot.run(token)
