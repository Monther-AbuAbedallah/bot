import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define your bot token
TOKEN = '6246239316:AAEbQmb9DOv5727xFPEUkH1IqvY5-9dMCCw'

# Create an updater and pass in your bot token
updater = Updater(token=TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Define the command for adding the bot to a group
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm ready to delete messages containing specific words in this group.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Define the function to delete messages containing specific words
def delete_message(update, context):
    words_to_delete = ['امك' , 'أمك' , 'ابوك' , 'أبوك' , 'شرموط' , 'عرص' , 'الوراني', 'حرام' , 'حرامي' , 'حرامية' , 'حراميه' , 'حراميه' , 'حرام' , 'سنة' , 'سني' , 'شيعة' , 'شيعي']

    message_text = update.message.text.lower()
    for word in words_to_delete:
        if word in message_text:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
            break

delete_handler = MessageHandler(Filters.text, delete_message)
dispatcher.add_handler(delete_handler)

# Start the bot
updater.start_polling()
