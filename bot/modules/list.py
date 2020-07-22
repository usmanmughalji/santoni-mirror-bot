from telegram.ext import CommandHandler, run_async
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
<<<<<<< HEAD
=======
import threading
import re
>>>>>>> e0f74e6... search fix for special characters
from bot.helper.telegram_helper.bot_commands import BotCommands

@run_async
def list_drive(update,context):
<<<<<<< HEAD
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
    except IndexError:
        sendMessage('send a search key along with command', context.bot, update)
        return
        
    reply = sendMessage('Searching...', context.bot, update)

=======
    message = update.message.text
    search = message.split(' ',maxsplit=1)[1]
    search = re.escape(search)
>>>>>>> e0f74e6... search fix for special characters
    LOGGER.info(f"Searching: {search}")
        
    gdrive = GoogleDriveHelper(None)
    msg, button = gdrive.drive_list(search)

    editMessage(msg,reply,button)


list_handler = CommandHandler(BotCommands.ListCommand, list_drive,filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
dispatcher.add_handler(list_handler)
