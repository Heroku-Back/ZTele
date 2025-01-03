import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.errors import AccessTokenExpiredError, AccessTokenInvalidError
from ..Config import Config
from .bothseesion import bothseesion
from .client import ZedUserBotClient
from .logger import logging

LOGS = logging.getLogger("زدثــون")
__version__ = "3.10.3"

loop = None

if Config.STRING_SESSION:
    session = bothseesion(Config.STRING_SESSION, LOGS)
else:
    session = "zelzal"

APP_ID = 27455984
API_HASH = "62d5f68ce2e9189636967120220f5755"

try:
    zedub = ZedUserBotClient(
        session=session,
        api_id=APP_ID,
        api_hash=API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(
        f"STRING_SESSION CODE WRONG MAKE A NEW SESSION - {e}\n كود سيشن تيليثـون غير صالح .. قم باستخـراج كود جديد ؟!"
    )
    sys.exit()


try:
    zedub.tgbot = tgbot = ZedUserBotClient(
        session="ZedTgbot",
        api_id=APP_ID,
        api_hash=API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=Config.TG_BOT_TOKEN)
except FloodWaitError as e:
    LOGS.error(f"FloodWaitError: فلود وايت - يرجى الانتظار لـ {e.seconds} ثانية.")
except (AccessTokenExpiredError, AccessTokenInvalidError):
    LOGS.error("توكن البوت غير صالح قم باستبداله بتوكن جديد من بوت فاذر")
