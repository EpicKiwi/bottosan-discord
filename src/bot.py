import re

from features import INSTALLED_FEATURES
import discord
import settings
import os

print("starting ボットさん")
client = discord.Client()

MENTION_REGEX = re.compile("<@&######>")

@client.event
async def on_ready():
    global MENTION_REGEX
    MENTION_REGEX = re.compile("^\s*<@!{}>".format(client.user.id))

    os.makedirs(settings.ASSETS_ROOT,exist_ok=True)
    os.makedirs(settings.ASSETS_ROOT+"/kanji",exist_ok=True)

    print("\n{} installed features".format(len(INSTALLED_FEATURES)))
    for feature in INSTALLED_FEATURES:
        print("- {}".format(feature.name))
    print("")

    print("ボットさん is running\n")

@client.event
async def on_message(message):

    if MENTION_REGEX.match(message.content) is not None:
        message.content = re.sub(MENTION_REGEX, "", message.content).strip()
    elif not isinstance(message.channel, discord.DMChannel):
        return

    for feature in INSTALLED_FEATURES:
        if feature.is_matching(message):
            await feature.execute(message)
            break


client.run(settings.BOT_TOKEN)