import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

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
    await update.message.reply_text("Selamat datang! Gunakan /check_id untuk memeriksa ID Anda.")

# Handler untuk perintah /check_id
async def check_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    username = user.username if user.username else "Tidak ada"

    await update.message.reply_text(f"ID Anda: {user_id}\nUsername Anda: {username}")

# Fungsi utama untuk menjalankan bot
def main() -> None:
    application = Application.builder().token(my_bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("check_id", check_id))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
