# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 (C) 2022 𝑩𝒚 @𝗔𝗱𝗿𝗶𝘀𝗵_𝗢𝘄𝗻𝗲𝗿

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝗗𝗲𝗹𝗲𝘁𝗲 𝗮𝗹𝗹 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗳𝗶𝗹𝗲𝘀 ...**")
    else:
        await message.reply_text("❌ **𝗡𝗼 𝗳𝗶𝗹𝗲𝘀 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 ...**")

        
@Client.on_message(command(["rmr", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **𝗗𝗲𝗹𝗲𝘁𝗲 𝗮𝗹𝗹 𝗔𝗱𝗿𝗶𝘀𝗵 𝗳𝗶𝗹𝗲𝘀...**")
    else:
        await message.reply_text("❌ **𝗡𝗼 𝗔𝗱𝗿𝗶𝘀𝗵 𝗙𝗶𝗹𝗲 𝗜𝗻 𝗦𝗲𝗿𝘃𝗲𝗿 ...**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **𝗖𝗹𝗲𝗮𝗻 𝗔𝗹𝗹 𝗝𝘂𝗻𝗸 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹𝘀 ...**")
    else:
        await message.reply_text("✅ **𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗖𝗹𝗲𝗮𝗻 𝗔𝗹𝗹 𝗝𝘂𝗻 ...**")
