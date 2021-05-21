import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from script import script

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start"))
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Nexon Projects ❤", url="https://t.me/NexonHex")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id,
    )

@Client.on_message(filters.command(["help", "h"]))
async def help_message(client, message):
    await client.send_message(  
        chat_id=message.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕ Join Our Channel ⭕", url="https://t.me/NexonHex")], [InlineKeyboardButton(text="Support", url="https://t.me/NexonHex_grp"),
                     InlineKeyboardButton(text="Share", url="tg://msg?text=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%20%0A__Today%20i%20just%20found%20out%20an%20intresting%20and%20Powerful__%20%2A%2AZee5%20Downloader%20Bot%2A%2A%20__for%20Free%F0%9F%A5%B0.__%20%20%0A%2A%2ABot%20Link%20%3A%20%40Zee5dl_robot%2A%2A%20%F0%9F%94%A5")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id,
    )

@Client.on_message(filters.command("about"))
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Nexon Projects ❤", url="https://t.me/NexonHex")]]),
        parse_mode="html",
        disable_web_page_preview=True,         
        reply_to_message_id=message.message_id,
    )
