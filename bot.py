import discord
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

class MyClient(discord.Client):
    async def on_ready(self):

        print(f'Logged on as {self.user}!')

    async def on_message(self, message):

        if message.author == self.user:
            return

        if message.content.startswith('>bot punch'):
            if message.mentions:
                other_user = message.mentions[0]
                gif = random.choice(punch_gifs)
                caption = f'Ouch! {message.author.display_name} punched {other_user.display_name}. \n{gif}'

                embed = discord.Embed(
                    title=caption,
                    color=discord.Color.brand_red()
                )

                embed.set_image(url = gif)
                await message.channel.send(embed=embed)

            else:
                await message.channel.send(f'Mention the user you want to punch!')



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
