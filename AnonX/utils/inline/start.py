from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐇ᴇʟᴘ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐒ᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚  𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="🌟 𝐆ʀᴏᴜᴘ 🌟", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="💌 𝐂ʜᴀɴɴᴇʟ 💌", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="🤔 𝐇ᴇʟᴘ 🤔", callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐎ᴡɴᴇʀ 🥀", url=f"https://t.me/Thalaivars001"
            )
         ],
        [    
            InlineKeyboardButton(
            text="❄️ 𝐔ᴘᴅᴀᴛᴇꜱ ❄️", url=f"https://t.me/FileStore_Bots_Updates"
            )
        ],
     ]
    return buttons
