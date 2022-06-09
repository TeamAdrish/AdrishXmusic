
import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_IMAGE, BOT_USERNAME, OWNER_USERNAME, UPDATES_CHANNEL, SUPPORT_GROUP, SOURCE_CODE
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐈 𝐀𝐦 𝐇𝐢𝐠𝐡-𝐥𝐞𝐯𝐞𝐥 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐎𝐟 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.
        𝗠𝗮𝗻𝗴𝗲 𝗯𝘆 :- 𝗧𝗲𝗮𝗺 𝗔𝗱𝗿𝗶𝘀𝗵 
 𝗢𝘄𝗻𝗲𝗿 ➪ »  [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{OWNER_USERNAME})
 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞]({UPDATES_CHANNEL})
 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞]({SUPPORT_GROUP})

𝑨𝒅𝒅 𝑴𝒆 𝒊𝒏 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑  𝑨𝒏𝒅 𝒆𝒏𝒋𝒐𝒚 𝒉𝒊𝒈𝒉 𝑸𝒖𝒂𝒍𝒊𝒕𝒚 𝑺𝒐𝒏𝒈𝒔 

━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝗔𝗱𝗱 𝗠𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#adrish"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bcac4ce2a546c8012ebfa.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐑𝐞𝐩𝐨 💞", url=f"{SOURCE_CODE}")
                ]
            ]
        ),
    )
