# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "12777841"))
API_HASH = getenv("API_HASH", "d01bbf996325918c7ceec53c0ebf1499")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6459837145").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "mongodb+srv://aston420martin:elNrd24uMqFSQeyW@cluster0.ktluu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
