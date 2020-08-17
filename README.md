# ボットさん

> Bot discord for Japanese learning (from french :fr:)

## Install

Clone this repository and install dependencies

```sh-session
pip install -r requirements.txt
```

You must have [cairo](https://www.cairographics.org/) installed on your machine.
On Debian you can run the following :

```sh-session
apt install libcairo2-dev pkg-config
```

Copy `src/settings.template.py` to `src/settings.py` and fill it with your configuration

Start the bot

```sh-session
python src/bot.py
```

## Generate static files

You can generate static files to save time during first requests, some scripts are included allowing you to generate statuic images.

Generate kanji tumbnails

```sh-session
python src/script-generate-kanji-thumbnails.py
```