import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
import httpx

# Ganti dengan token bot Anda
my_bot_token = "7369819911:AAHATdOCKY0KGjkuaXgJyEj8eI3p9dfM8Go"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Handler untuk perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Periksa ID Anda", callback_data='check_id')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selamat datang! Gunakan tombol di bawah ini:", reply_markup=reply_markup)

# Handler untuk callback button
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    if query.data == 'check_id':
        user = query.from_user
        user_id = user.id
        username = user.username if user.username else "Tidak ada"
        await query.edit_message_text(text=f"ID Anda: {user_id}\nUsername Anda: {username}")

# Fungsi utama untuk menjalankan bot
def main() -> None:
    application = Application.builder().token(my_bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()