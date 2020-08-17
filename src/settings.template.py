import os

# Discord Bot token used to possess your bot
BOT_TOKEN="YourDiscordBotToken"

# Folder containing all assets generated by the bot that must be served on the web
ASSETS_ROOT="{}/../assets".format(os.path.dirname(__file__))

# Base URL of the ASSETS_ROOT folder avalable on the web (served via https)
ASSETS_BASE_URL="http://localhost:8080"

# Mongodb host where are stored kanji and vocabulary data
MONGODB_HOST="localhost"

# Mongodb port
MONGODB_PORT=27017

# Mongodb Database
MONGODB_DATABASE="bottosan"