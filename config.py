from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "811052"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ed")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","GJ516 MUSIC BOT")
BOT_USERNAME = getenv("BOT_USERNAME", "GJ516_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GJ516_DISCUSS_GROUP")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "myworldGJ516")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
PICS = getenv("PICS" ,"https://te.legra.ph/file/e500e250ebdbf48a75fa4.jpg https://te.legra.ph/file/f37ede5e8df253250cb19.jpg ")).split()
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/53a33aeb7ff9694c41d20.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1864894033").split()))
