import settings
from lib.database import get_db
from kanji import get_kanji_thumbnail

for carac in get_db().kanji.find({}):
    print("Generated {}".format(get_kanji_thumbnail(carac["kanji"])))