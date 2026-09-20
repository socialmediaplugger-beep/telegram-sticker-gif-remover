import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def delete_sticker_or_gif(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    message = update.effective_message

    if not message:
        return

    if message.sticker or message.animation:
        try:
            await message.delete()
        except Exception as e:
            print(f"Delete error: {e}")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.Sticker.ALL | filters.ANIMATION,
            delete_sticker_or_gif
        )
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
