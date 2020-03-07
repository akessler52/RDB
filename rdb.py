import os
import random
from discord.ext.commands import Bot
from discord.ext import tasks
import datetime
from bs4 import BeautifulSoup
import requests


token = os.getenv('DISCORDAPI')
client = Bot(command_prefix='$')


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.command(name='ping')
async def ping(ctx):
    await ctx.send("pong")


@client.command(name='captains')
async def on_message(message):
    memList = []
    page = requests.get("https://www.mapban.gg/en/ban/csgo/esl/bo1")
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('input')
    cap1Link = links[1]['value']
    cap2Link = links[0]['value']
    viewerLink = links[2]['value']

    for x in client.get_all_members():
        if x.voice:
            if x.voice.channel.name == 'lounge':
                memList.append(x)
    if len(memList):
        cap1 = random.choice(memList)
        user = await cap1.create_dm()
        await user.send(cap1Link)
        memList.remove(cap1)
        cap2 = random.choice(memList)
        user = await cap2.create_dm()
        await user.send(cap2Link)

        await message.channel.send("""
@here - Here are the links for the next 10 man. {3}

:red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:

Scrim Links:
:desktop: - <https://popflash.site/scrim/UGRscrim1>
:earth_americas: - {0}

:military_medal: - {1}
:military_medal: - {2}

:red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:
""".format(viewerLink, cap1.name, cap2.name, client.get_emoji(484465825236123659)))


@tasks.loop(minutes=1)
async def minuteLoop():
    if datetime.datetime.today().weekday() == 1 and datetime.datetime.utcnow().hour == 0 and datetime.datetime.utcnow().minute == 1:
        message_channel = client.get_channel(122167014004359171)
        await message_channel.send("""
@csgo - Weekly 10 man's Sunday night's starting around 8 or 9pm if you are interested. Drop into #lounge to get things started!

:small_red_triangle: Captains decided by me, the bot.
:small_red_triangle: BO1 - Map picks are ban down to the last 2, server decides.
:small_red_triangle: Veto site - https://www.mapban.gg/
:small_red_triangle: Scrim Server - https://popflash.site/
""")


@minuteLoop.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")


minuteLoop.start()

client.run(token)
