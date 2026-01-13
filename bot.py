import datetime

from telegram.constants import ReactionEmoji
from telegram.ext import Application, filters, CommandHandler, ContextTypes, MessageHandler
from telegram import Update
import os

CHATS = []

EMOJIS = {
    "zxc_chmo" : ReactionEmoji.CLOWN_FACE,
    "Y14_5r" : ReactionEmoji.UNICORN_FACE,
    "mr4ckkk": ReactionEmoji.ALIEN_MONSTER,
    "I6573859": ReactionEmoji.BANANA,
    "eI_donte": ReactionEmoji.SPOUTING_WHALE,
    "roma_kaurcev": ReactionEmoji.HOT_DOG,
    "Myp3ikGay": ReactionEmoji.GHOST,
}

jaba_id = "CgACAgQAAx0CYjMl9wABAbxqaV0_tuGGHH3-73ECfAGQ9ggM4hoAAjMEAAIvULVTUGEmWUs7wUk4BA"
romchik_id = "AgACAgIAAxkBAAO-aWZ5E9HnkEu_15d1sFkvlr4skFkAAnwSaxttODFLEjpPniWwqSUBAAMCAAN4AAM4BA"

async def react_on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.is_bot:
        return

    msg = update.message
    text = update.message.text.lower() if update.message.text else ""
    chat_id = update.effective_chat.id

    try:
        username = msg.from_user.username if msg.from_user.username else ""
        if EMOJIS.keys().__contains__(username):
            await context.bot.set_message_reaction(
                chat_id=msg.chat_id,
                message_id=msg.message_id,
                reaction=[EMOJIS[username]],
                is_big=False
            )
    except Exception as e:
        print(f"Не удалось поставить реакцию: {e}")

    try:
        if "я" == text:
            await update.message.reply_text("Головка от хуя  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ")
        if "макан" == text:
            await context.bot.send_message(chat_id,"Хуесос  ┌∩┐(◣_◢)┌∩┐")
        if "рома" in text or "ромчик" in text:
            await context.bot.send_message(chat_id,"Пошел нахуй Ромчик(@roma_kaurcev) ψ(▼へ▼メ)～→")
        if "@roma_kaurcev" in text:
            await msg.reply_photo(
                photo="AgACAgIAAxkBAAO-aWZ5E9HnkEu_15d1sFkvlr4skFkAAnwSaxttODFLEjpPniWwqSUBAAMCAAN4AAM4BA"
            )

    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def echo_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    try:
        if msg.animation:
            if msg.animation.file_id == jaba_id:
                await msg.reply_animation(
                    animation=jaba_id,
                    reply_to_message_id=msg.message_id
                )

        if msg.sticker:
            sticker = msg.sticker

            await msg.reply_sticker(
                sticker=sticker.file_id,
                reply_to_message_id=msg.message_id
            )
    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def fuck_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Пошел нахуй"
        )
    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def suck_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Соси хуй"
        )
    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def callback_alarm(context) -> None:
    chat_id = context.job.data

    try:
        if not CHATS.__contains__(chat_id):
            return

        await context.bot.send_message(
            chat_id=chat_id,
            text="/pidor@SublimeBot"
        )
    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def set_daily_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    try:
        if CHATS.__contains__(chat_id):
            await update.message.reply_text(
                "Ежедневный пидор уже поставлен"
            )
            return
        else:
            CHATS.append(chat_id)

        context.job_queue.run_daily(
            callback_alarm,
            time=datetime.time(1, 00, 00, tzinfo=datetime.timezone.utc),
            data=chat_id,
        )

        await update.message.reply_text(
            "Ежедневный пидор поставлен на 9 утра"
        )
    except Exception as e:
        print(f"Не удалось поставить напоминалку: {e}")

def main() -> None:
    token = "8389376627:AAH-ZXn-jOSH6tE0n30ajQsKElLDD5Ci8C8"

    if not token:
        raise ValueError("BOT_TOKEN environment variable not set!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("set_daily_pidor", set_daily_reminder))
    app.add_handler(CommandHandler("fuck", fuck_func))
    app.add_handler(CommandHandler("suck", suck_func))

    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        react_on_message
    ))

    app.add_handler(MessageHandler(
        filters.ANIMATION | filters.ATTACHMENT,
        echo_media
    ))

    app.run_polling()

if __name__ == "__main__":
    main()