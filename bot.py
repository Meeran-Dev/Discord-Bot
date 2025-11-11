import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

punch_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWtwb204YXo1MHdtanhsemV4b291dDZvYTEwOXY0b2JoejN5ZW9pbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/NuiEoMDbstN0J2KAiH/giphy.gif",
              "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTlsd3FjbnV6eTN3dndmNHg1d2FsZXNzZmhnMXYxYWdyODlvOTg5dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xUO4t2gkWBxDi/giphy.gif",
              "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTlsd3FjbnV6eTN3dndmNHg1d2FsZXNzZmhnMXYxYWdyODlvOTg5dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/okECPQ0lVQeD6/giphy.gif"]

slap_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczN4OW84cTZsc2R4OXFudWZnMTZyZ3F4bWxiY3dtb29ob3NuamJuOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Gf3AUz3eBNbTW/giphy.gif",
             "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczN4OW84cTZsc2R4OXFudWZnMTZyZ3F4bWxiY3dtb29ob3NuamJuOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Zau0yrl17uzdK/giphy.gif",
             "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczN4OW84cTZsc2R4OXFudWZnMTZyZ3F4bWxiY3dtb29ob3NuamJuOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xUNd9HZq1itMkiK652/giphy.gif"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>bot ', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command()
async def punch(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f'Mention the user you want to punch!')
        return

    gif = random.choice(punch_gifs)
    caption = f'Ouch! {ctx.author.display_name} punched {member.display_name}.'

    embed = discord.Embed(
        title=caption,
        color=discord.Color.brand_red()
    )

    embed.set_image(url=gif)
    await ctx.send(embed=embed)

@bot.command()
async def slap(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f'Mention the user you want to slap!')
        return

    gif = random.choice(slap_gifs)
    caption = f'BAM! {ctx.author.display_name} slapped {member.display_name}.'

    embed = discord.Embed(
        title=caption,
        color=discord.Color.blue()
    )

    embed.set_image(url=gif)
    await ctx.send(embed=embed)

bot.run(token)
