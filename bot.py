import datetime

from telegram.constants import ReactionEmoji
from telegram.ext import Application, filters, CommandHandler, ContextTypes, MessageHandler
from telegram import Update
import os

CHATS = [-1001647519223]

EMOJIS = {
    "zxc_chmo" : ReactionEmoji.CLOWN_FACE,
    "Y14_5r" : ReactionEmoji.UNICORN_FACE,
    "mr4ckkk": ReactionEmoji.ALIEN_MONSTER,
    "I6573859": ReactionEmoji.BANANA,
    "eI_donte": ReactionEmoji.SPOUTING_WHALE,
    "roma_kaurcev": ReactionEmoji.NAIL_POLISH,
    "Myp3ikGay": ReactionEmoji.GHOST,
}

jaba_id = os.getenv("jaba_id")[1 : -1]
tankist = os.getenv("tankist")[1 : -1]
absolute = os.getenv("absolute")[1 : -1]
outtake_lude = os.getenv("outtake_lude")[1 : -1]
zavozik = os.getenv("zavozik")[1 : -1]
sergey = os.getenv("sergey")[1 : -1]
sidzi = os.getenv("sidzi")[1 : -1]
pidarasa = "AgACAgIAAxkBAAPSaW9GKC45SP8oIH5GvSwLbClEjUMAAtcLaxuE3YBLt4Jjoi5gSaYBAAMCAAN5AAM4BA"
operoma = os.getenv("operoma")[1 : -1]
molchun = os.getenv("molchun")[1 : -1]
hay_giler = os.getenv("hay_giler")[1 : -1]
shurupe_benzine = os.getenv("shurupe_benzine")[1 : -1]
sapogi = os.getenv("sapogi")[1 : -1]
pamaty = os.getenv("pamaty")[1 : -1]
AAAA = os.getenv("AAAA")[1 : -1]
pidaras = os.getenv("pidaras")[1 : -1]
advokat = os.getenv("advokat")[1 : -1]
dance = os.getenv("dance")[1 : -1]
pedick =    "AgACAgIAAxkBAAIBDGlvYKvWPNCzUgUf0bD-Os89fA4ZAALqDGsbhN2AS-c4HUb_ISa2AQADAgADeQADOAQ"
xyesos =    "CAACAgIAAx0CYjMl9wABAc3EaW-K1kS2Z-S3m9jqbitrXTTB5TQAAjUdAAJ9UKhIUJJ6M3Ok80c4BA"
xyesosaa =  "AgACAgIAAxkBAAIBg2lvlMLVPDZVDN0SOx55HfqgeaL4AAI5EGsb7uV4SwmE49CFCKWcAQADAgADeQADOAQ"
aboba =     "AgACAgIAAxkBAAIBhWlvlP8TrAesnzLSdKok_iVQGughAAIyEGsb7uV4Syzseq-jKlfeAQADAgADeQADOAQ"
fisher =    "AgACAgIAAxkBAAIBhGlvlOqyFc9zn7CqeKbADL2GsWA3AAI9EGsb7uV4SwqGORgggyqRAQADAgADeQADOAQ"

triggers = {
    "@roma_kaurcev"                 : ('photo' ,tankist),
    "молчун"                        : ('photo', molchun),
    "абсолют"                       : ('photo',absolute),
    "серега"                        : ('photo', sergey),
    "окнутые люди"                  : ('photo', outtake_lude),
    "завозик"                       : ('photo', zavozik),
    "депрессия"                     : ('photo', sidzi),
    "ебланы"                        : ('photo', pidarasa),
    "хай гитлер"                    : ('photo', hay_giler),
    "шуруп бензин"                  : ('photo', shurupe_benzine),
    "сапоги"                        : ('photo', sapogi),
    "светлая память"                : ('photo', pamaty),
    "аааа"                          : ('photo', AAAA),
    "пидарас"                       : ('photo', pidaras),
    "чернобль"                      : ('video', operoma),
    "адвокат"                       : ('video', advokat),
    "педик"                         : ('photo', pedick),
    "хуесосы хуисосатели"           : ('photo', xyesosaa),
    "рома ромчик"                   : ('message', "Пошел нахуй Ромчик(@roma_kaurcev) ψ(▼へ▼メ)～→"),
    "макан"                         : ('message', "Хуесос  ┌∩┐(◣_◢)┌∩┐"),
    "я"                             : ('message', "Головка от хуя  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ "),
    "хуесос"                        : ('sticker', xyesos),

    "абоба"                         : ('photo', aboba),
    "рыбак"                         : ('photo', fisher),
}

send_functions = {
    'photo'      : lambda bot: bot.send_photo,
    'video'      : lambda bot: bot.send_video,
    'animation'  : lambda bot: bot.send_animation,
    'message'    : lambda bot: bot.send_message,
    'sticker'    : lambda  bot: bot.send_sticker,
}

async def react_on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        for trigger, (media_type, reply) in triggers.items():
            words = trigger.split(' ')
            if len(words) == 1 and trigger == text and media_type.lower() == 'message':
                send_method = send_functions[media_type](context.bot)
                await send_method(chat_id, reply)
                break
            elif any(word in text for word in words):
                send_method = send_functions[media_type](context.bot)
                await send_method(chat_id, reply)
                break

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
            print(sticker.file_id)

        if msg.photo:
            print(msg.photo[-1].file_id)

    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def fuck_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    username_part = context.args[0] if len(context.args) == 1 else ""

    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"Пошел нахуй {username_part}"
        )
    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def suck_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    username_part = context.args[0] if len(context.args) == 1 else ""

    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"Соси хуй {username_part}"
        )
    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def dance_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    try:
        await context.bot.send_video(
            chat_id=chat_id,
            video=dance,
        )
    except Exception as e:
        print(f"Не удалось отправить виде: {e}")

async def list_words_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    lines = ["Триггер        | Тип     |", "---------------|---------|"]

    for trigger, (media_type, reply) in sorted(triggers.items()):
        lines.append(f"{trigger:<14} | {media_type:<7}")

    message = "```\n" + "\n".join(lines) + "\n```"

    await context.bot.send_message(
        chat_id=chat_id,
        text=message,
        parse_mode="MarkdownV2"
    )

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
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN environment variable not set!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("set_daily_pidor", set_daily_reminder))
    app.add_handler(CommandHandler("fuck", fuck_func))
    app.add_handler(CommandHandler("suck", suck_func))
    app.add_handler(CommandHandler("dance", dance_func))
    app.add_handler(CommandHandler("list_words", list_words_func))

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