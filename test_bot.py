from transliterate import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    user = update.message.from_user
    update.message.reply_html("Hello <b>{}!</b>\n\nWelcome to Latin - Cyrillic converter bot \n<b>Enter the text:</b>".format(user.first_name))

    #text = str(update.message.text)
    #update.message.reply_text(text)

def response(update, context):
    words = update.message.text

    if words.isascii():
        update.message.reply_text(to_cyrillic(words))
    else:
        update.message.reply_text(f"{to_latin(words)}")

def main():
    updater = Updater("5407272479:AAG8TOPRwvRF434MdGh_wnf6QbpBIf5XeY8", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, response))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()