from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters,
)
import logging
import time

updater = Updater(token='1908662113:AAEfxq-DT7BfARJeMPnT7sifhqqQnOVsrhE')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    time.sleep(2)
    first_name = update.message.from_user.first_name
    if first_name == 'Palash':
        message = 'Hey dummy-dum.'
    else:
        message = f'Hai sexy lady, how are you today?'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def introduce(update, context):
    time.sleep(2)
    message = "I'm Annie, I'm from California, I'm Palash's really close friend. He is my babe!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def bot(update, context):
    first_name = update.message.from_user.first_name
    message = "My name is Annie and I'm not a bot. Say that again and you are dead meat!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

start_handler = MessageHandler(Filters.regex('(H|h)(ello|ey|i)'), start)
introduce = MessageHandler(Filters.regex('(I|i)ntroduce'), introduce)
bot_reveal = MessageHandler(Filters.regex('(b|B)(ot)'), bot)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(introduce)
dispatcher.add_handler(bot_reveal)
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()