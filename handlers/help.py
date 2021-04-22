from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

PM_HELP_TEXT = "Sorry You Can't Use Me!" 

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await message.reply_text(
     PM_HELP_TEXT, 
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Support Channel', url='https://t.me/trvpn'),
                    InlineKeyboardButton('Owner', url='https://t.me/trvpn')
                ],
                [
                    InlineKeyboardButton('Song Plays On', url='https://t.me/trvpn'),
                    InlineKeyboardButton('Source', url='')
                ]
            ]
        )
    ) 
