from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyromod import listen
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
    buttons = [[InlineKeyboardButton(text=Buttons.start_my_profile, callback_data=Buttons.start_my_profile_call)]]
    msg = Messages.START_MSG.format(message.from_user.first_name)
    await app.send_message(chat_id=user_id, text=msg, reply_markup=InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex(Buttons.start_my_profile_call))
async def profile(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.id
    user = Users.get_mega_info(chat_id)
    if user.mega_username:
        msg = Messages.PROFILE_MSG.format(user.mega_username, user.maga_password)
        buttons = [
            [InlineKeyboardButton(text=Buttons.profile_email, callback_data=Buttons.profile_email_call),
             InlineKeyboardButton(text=Buttons.profile_password, callback_data=Buttons.profile_password_call)],
            [InlineKeyboardButton(text=Buttons.profile_history, callback_data=Buttons.profile_history_call)],
        ]
    else:
        msg = Messages.DONT_HAVE_ACCOUNT_MSG
        buttons = [[InlineKeyboardButton(text=Buttons.start_add_account, callback_data=Buttons.start_add_account_call)]]
    await app.edit_message_text(chat_id=chat_id, message_id=message_id, text=msg,
                                reply_markup=InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex(Buttons.start_add_account_call))
async def add_account(client, callback_query, email=None):
    chat_id = callback_query.from_user.id
    email = await client.ask(chat_id, Messages.GET_ACCOUNT_EMAIL_MSG)
    messages = []
    try:
        if "EMAIL" in str(email.entities[0].type):
            password = await client.ask(chat_id, Messages.GET_ACCOUNT_PASSWORD_MSG)
        else:
            password = await email.reply(Messages.IS_NOT_EMAIL_MSG)
            return await add_account(client, callback_query)
    except TypeError:
        password = await email.reply(Messages.IS_NOT_EMAIL_MSG)
        return await add_account(client, callback_query)
    res = MegaUser.check_user(email.text, password.text)
    if res:
        Users.add_mega_info(mega_username=email.text, maga_password=password.text, user_id=chat_id)
        await app.send_message(chat_id, Messages.SUCCESS_ADD)
        await start(client, callback_query)
    else:
        await app.send_message(chat_id, Messages.NOT_ADD)
        await start(client, callback_query)


async def get_file_info(message):
    type_message = str(message.media).split(".")[-1]
    type_message = type_message.lower()
    file_id = "message." + type_message + ".file_id"
    return eval(file_id), type_message


@app.on_message(filters.photo | filters.video | filters.document | filters.video_note | filters.audio | filters.voice)
async def download_media(client, message):
    user_id = message.from_user.id
    file_info = await get_file_info(message)
    print(file_info)
    Files.add_file(file_id=file_info[0], user_id=user_id, file_type=file_info[1])
    try:
        mega = MegaUser(user_id)
        file_path = await message.download()
        mega.upload_file(file_path)
        Files.add_upload_status(1, user_id)
    except Exception as e:
        with open("meg-error.txt", 'a') as f:
            f.write(e.message)
            pass
    os.remove(file_path)


@app.on_message(filters.command("admin"))
async def admin_panel(client, message):
    pass



app.run()



