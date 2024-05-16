# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "20114671"))
    API_HASH = os.environ.get("API_HASH", "db35dedc1f6918b21f65f8435481355d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6861349544:AAHPq4iyw_8y3wXKWZ5jDOkB1hIdivFmjaY")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1445283714))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(5918110486)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://densilraja:ZM1NE14X8Wa@cluster0.xoux857.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
