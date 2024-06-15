import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "14454340"))
    API_HASH = os.environ.get("API_HASH", "293a46f9c7e2b023a66c5128cc91d897")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6599290938:AAF6zoNsXvCWOaK7Pi9zbmXBnxpNrvKKtK8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Astrosamplebot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
