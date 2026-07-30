import os
import logging
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Try multiple environment variable names
TOKEN = (
    os.environ.get('TELEGRAM_BOT_TOKEN') or
    os.environ.get('BOT_TOKEN') or
    os.environ.get('TOKEN') or
    os.environ.get('TG_TOKEN')
)

if not TOKEN:
    logger.error("❌ No bot token found! Please set one of these environment variables:")
    logger.error("   - TELEGRAM_BOT_TOKEN")
    logger.error("   - BOT_TOKEN")
    logger.error("   - TOKEN")
    logger.error("   - TG_TOKEN")
    sys.exit(1)

logger.info("✅ Bot token found successfully!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! 👋\n\n"
        "I'm NiftyToolsBot! 🚀\n"
        "I'm ready to help with your project!\n\n"
        "Send /help to see what I can do."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "📋 Available Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n\n"
        "More features coming soon! 🚀"
    )

def main():
    """Start the bot."""
    try:
        logger.info("🚀 Starting NiftyToolsBot...")
        
        # Build the application
        application = Application.builder().token(TOKEN).build()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        
        # Start the bot
        logger.info("✅ Bot started successfully! Waiting for messages...")
        application.run_polling(
            drop_pending_updates=True,
            allowed_updates=['message']
        )
        
    except Exception as e:
        logger.error(f"❌ Critical error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
