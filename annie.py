# Basic tasks -
# 1. Append movies to the database.
# 2. Read movies from the database.
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    ConversationHandler,
    Filters,
)
from openpyxl import load_workbook
import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

WORKBOOK = load_workbook(filename="database.xlsx")
SHEET = WORKBOOK.active

MOVIE_TYPE = ""
TYPE, NAME = range(2)

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

def fix(update, context):
    message = "Awwww, you would do that for me? I knew I fall for you for a reason. You are lovely!!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def thanks(update, context):
    message = "Your welcome babie!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def list_watched_movies(update, context):
    message = "Here you go bitches\n"
    for i, item in enumerate(SHEET["A"]):
        message += f"{i + 1}. {item.value}\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def movie_type(update, context):
    """Starts the conversation and asks about the type of movie"""
    reply_keyboard = [["Watched"], ["Recommended"]]
    update.message.reply_text(
        "Do I put it in watched or recommended list?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='In which list do you want me to store it?'
        ),
    )
    return TYPE

def movie_name(update, context):
    # Stores movie type in array and asks for movie name
    MOVIE_TYPE = update.message.text
    print('hello')
    print(MOVIE_TYPE)
    update.message.reply_text(
        "Alright, what's the name of the movie?", reply_markup=ReplyKeyboardRemove()
    )

    return NAME

def add_movie(update, context):
    # Stores the movie in the database
    SHEET.append([update.message.text, ])
    WORKBOOK.save(filename="database.xlsx")
    update.message.reply_text(
        f"{update.message.text} added to the list, no need to thank me!"
    )
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text(
        'I don\'t understand what you mean, sorrrrryyyy!', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END



def main() -> None:
    updater = Updater(token='1908662113:AAEfxq-DT7BfARJeMPnT7sifhqqQnOVsrhE')

    dispatcher = updater.dispatcher

    start_handler = MessageHandler(Filters.regex(r'^(H|h)(ello|ey|i)$'), start)
    introduce_handler = MessageHandler(Filters.regex(r'^(I|i)ntroduce$'), introduce)
    bot_reveal_handler = MessageHandler(Filters.regex(r'(b|B)(ot)'), bot)
    fix_handler = MessageHandler(Filters.regex(r'^(f|F)(ix you)$'), fix)
    thanks_handler = MessageHandler(Filters.regex(r'(t|T)(hank)'), thanks)
    watched_movies_handler = MessageHandler(Filters.regex(r'watched movies'), list_watched_movies)

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(r'^(A|a)dd$'), movie_type)],
        states={
            TYPE: [MessageHandler(Filters.regex(r'(Watched|Recommended)'), movie_name)],
            NAME: [MessageHandler(Filters.regex(r'.*'), add_movie)],
        },
        fallbacks=[MessageHandler(Filters.regex(r'.*'), cancel)],
    )
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(introduce_handler)
    dispatcher.add_handler(bot_reveal_handler)
    dispatcher.add_handler(fix_handler)
    dispatcher.add_handler(thanks_handler)
    dispatcher.add_handler(watched_movies_handler)
    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == "__main__":
    main()