import os
from discord import Embed
import cairo
import settings
from lib.database import get_db


async def send_kanji_details(kanji, channel, text=""):
    kanji_details = get_db()["kanji"].find_one({"kanji": kanji})

    if kanji_details is None:
        await channel.send("**(◎_◎;)** Je n'ai pas trouvé le kanji **{}**")
        return

    kun = "-"
    if len(kanji_details["reading-kun"]) > 0:
        kun = ", ".join(kanji_details["reading-kun"])

    on = "-"
    if len(kanji_details["reading-on"]) > 0:
        on = ", ".join(kanji_details["reading-on"])

    details = Embed()
    details.title = "Kanji {}".format(kanji_details["kanji"])
    details.description = kanji_details["meaning"]
    details.url = kanji_details["source"]["jlpt-go"]
    details.set_thumbnail(url=get_kanji_thumbnail(kanji_details["kanji"]))
    details.add_field(name="Lecture KUN", value=kun, inline=True)
    details.add_field(name="Lecture ON", value=on, inline=True)
    details.add_field(name="Clé", value="{} ({})".format(kanji_details["radical"], kanji_details["radical-number"]), inline=False)
    details.add_field(name="Niveau scolaire", value=kanji_details["level-school"], inline=True)
    details.add_field(name="Niveau JLPT", value=kanji_details["level-jlpt"], inline=True)

    if len(kanji_details["related-kanji"]) > 1:
        details.add_field(name="Voir aussi",value=" ".join(kanji_details["related-kanji"]), inline=False)

    details.set_footer(text="JLPT-Go")

    await channel.send(text, embed=details)

def get_kanji_thumbnail(kanji):

    path = settings.ASSETS_ROOT+"/kanji/kanji-{}.png".format(kanji)

    if not os.path.isfile(path):
        canvas = cairo.ImageSurface(cairo.FORMAT_ARGB32, 512,512)
        ctx = cairo.Context(canvas)
        ctx.scale(512,512)
        ctx.set_source_rgb(0.184, 0.192, 0.211)
        ctx.rectangle(0,0,1,1)
        ctx.fill()
        ctx.set_source_rgb(1, 1, 1)
        ctx.select_font_face("Source Han Sans", cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(0.8)
        ctx.move_to(0.1,0.8)
        ctx.show_text(kanji)

        with open(path,"bw") as f:
            canvas.write_to_png(path)

    return settings.ASSETS_BASE_URL+"/kanji/kanji-{}.png".format(kanji)
