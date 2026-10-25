import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Configuration (Environment variables se values li jayengi)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GROUP_LINK = os.environ.get("GROUP_LINK", "https://t.me/your_group_username")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    first_name = user.first_name if user else "Dost"

    # Unique aur Premium Welcome Message
    message_text = (
        f"✨ **Namaste {first_name}!** ✨\n\n"
        "🚀 **Aapka hamare exclusive community bot me swagat hai!**\n\n"
        "📢 Hamare official group me judne ke liye aur sabhi latest updates, "
        "content aur discussions ka hissa banne ke liye neeche diye gaye button par click karein.\n\n"
        "👇 **Neeche 'Join Group' button par click karein:**"
    )

    # Inline Keyboard Buttons
    keyboard = [
        [
            InlineKeyboardButton("📢 Join Our Group", url=GROUP_LINK)
        ],
        [
            InlineKeyboardButton("✨ Updates Channel", url=GROUP_LINK) # Agar channel link alag ho to badal sakte ho
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Message send karein
    await update.message.reply_text(
        text=message_text,
        parse_mode="Markdown",
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN Environment Variable nahi mila!")
        return

    # App build karein
    application = Application.builder().token(BOT_TOKEN).build()

    # /start command handler
    application.add_handler(CommandHandler("start", start))

    # Bot run karein (Polling Mode)
    print("Bot chalu ho gaya hai...")
    application.run_polling()

if __name__ == "__main__":
    main()
