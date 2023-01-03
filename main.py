from src.modelling import Modelling
from src.gif import GifSearcher
from src.translator import Translator
from dotenv import load_dotenv
import os
from discord.ext import commands
import discord

load_dotenv()

print(os.getenv("DISCORD_KEY"))
print(os.getenv("GIPHY_KEY"))
print(os.getenv("TENOR_KEY"))
print(os.getenv("MICROSOFT_TRANSLATOR"))
print(os.getenv("MICROSOFT_LOCATION"))

# Create the Modelling object
modelling = Modelling()

# Create the GifSearcher object
gif_searcher = GifSearcher()

# Create the translator object
translator = Translator()

activity = discord.Activity(type=discord.ActivityType.watching, name="Reply with %r to a message",)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents, activity=activity, status=discord.Status.idle)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def r(ctx):
    message = await ctx.channel.fetch_message(ctx.message.reference.message_id)

    message_content = translator.translate(message.content)

    keywords = modelling.get_keywords(message_content)
    gif = gif_searcher.search_gif(keywords)

    print(f'{ctx.author}, sending a gif to {message.author} with keywords {keywords}')

    await ctx.send(gif)


DISCORD_KEY = os.getenv("DISCORD_KEY")
bot.run(DISCORD_KEY)
