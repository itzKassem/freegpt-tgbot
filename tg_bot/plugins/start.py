from pyrogram import filters
from tg_bot.tg_bot import TG_BOT as tbot


from freeGPT import AsyncClient

@tbot.on_message(filters.text)
async def gpt_reply(_, message):
    prompt = message.text
    try:
        resp = await AsyncClient.create_completion("gpt3", prompt)
        await message.reply_text(f"🤖: {resp}")
    except Exception as e:
             await message.reply_text(f"🤖: {e}")