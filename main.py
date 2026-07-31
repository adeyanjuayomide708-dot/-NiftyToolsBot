from telegram.ext import Updater, CommandHandler
import os
import logging

# ... rest of your code ...

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    
    updater.start_polling()
    updater.idle()
