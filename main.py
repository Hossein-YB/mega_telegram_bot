from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from text import Messages, Buttons
from utils import create_tables, Admins, Users, Files
from mega_api import MegaUser
import os

create_tables()
Admins.add_admin(1112519901)
app = Client(
    "upload_file",
    api_id=18283899,
    api_hash="f97be58eb771961044e0a347342adda0",
    bot_token='5189309634:AAHOMbcx-2maCpo5_8xsyzU7YCXv1MijYv8'
)


@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    Users.add_user(user_id, username)
    buttons = [[InlineKeyboardButton(text=Buttons.start_history, callback_data=Buttons.start_history_call),
                InlineKeyboardButton(text=Buttons.start_my_profile , callback_data=Buttons.start_my_profile_call )]]
    msg = Messages.START_MSG.format(message.from_user.first_name)
    await message.reply(text=msg, reply_markup=InlineKeyboardMarkup(buttons))


@app.on_message(filters.command("admin"))
async def admin_panel(client, message):
    pass


@app.on_message(filters.photo | filters.video | filters.document | filters.video_note | filters.audio | filters.voice)
async def download_media(client, message):
    user_id = message.from_user.id
    mega = MegaUser(user_id)
    file_path = await message.download()
    mega.upload_file(file_path)
    os.remove(file_path)


app.run()



