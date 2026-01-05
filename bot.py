import datetime

from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import os

async def callback_alarm(context) -> None:
    chat_id = context.job.data
    await context.bot.send_message(
        chat_id=chat_id,
        text="/pidor@SublimeBot"
    )

async def fuck_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id,
        text="Пошел нахуй"
    )

async def set_daily_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    context.job_queue.run_daily(
        callback_alarm,
        time=datetime.time(1, 00, 00, tzinfo=datetime.timezone.utc),
        data=chat_id,
    )

    await update.message.reply_text(
        "Ежедневный пидор поставлен на 9 утра"
    )

def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN environment variable not set!")

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("set_daily_pidor", set_daily_reminder))
    application.add_handler(CommandHandler("fuck", fuck_func))


    application.run_polling()

if __name__ == "__main__":
    main()