import asyncio

from lib.feature import feature
import kanji
from lib.database import get_db

@feature("^(\d+)? ?kanjis?$")
async def random_kanji(sourceMessage, matchResult):
    with sourceMessage.channel.typing():

        count = 1 if matchResult.group(1) is None else int(matchResult.group(1))

        random_kanji_list = get_db().kanji.aggregate([{ "$sample": { "size": count } }])

        for kanji_rand in random_kanji_list:
            await kanji.send_kanji_details(kanji_rand["kanji"], sourceMessage.channel)
            await asyncio.sleep(0.5)

@feature("kanji (.)")
async def kanji_details(sourceMessage, matchResult):
    with sourceMessage.channel.typing():
        await kanji.send_kanji_details(matchResult.group(1), sourceMessage.channel, text="Voici ce que j'ai trouvé")


INSTALLED_FEATURES = [
    random_kanji(),
    kanji_details()
]