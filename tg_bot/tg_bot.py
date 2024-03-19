from pyrogram import Client
from pyrogram import __version__
from pyrogram.raw.all import layer
from tg_bot import logger
from tg_bot import APP_ID, API_HASH, TOKEN


class TG_BOT(Client):
    def __init__(self):
        super().__init__(
            "",
            # session_string=SESSION,
            bot_token=TOKEN,
            plugins=dict(root="tg_bot/plugins"),
            api_id=APP_ID,
            api_hash=API_HASH,
        )

    async def start(self):
        await super().start()

        bot_me = await self.get_me()
        # await self.send_message(chat_id=DUMP_CH, text="test running")
        # self.set_parse_mode("html")
        logger.info(
            f"Bot based on Pyrogram v{__version__} "
            f"(Layer {layer}) started on @{bot_me.username}. "
        )
        # asyncio.create_task(run_srv())

    async def stop(self, *args):
        await super().stop()
        logger.info("Bot stopped.")
