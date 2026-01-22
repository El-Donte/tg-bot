import datetime

from telegram.constants import ReactionEmoji
from telegram.ext import Application, filters, CommandHandler, ContextTypes, MessageHandler
from telegram import Update
import os

from nick_parser import get_nicks_for_name

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

jaba_id         = "CgACAgQAAx0CYjMl9wABAc4HaW-bS2BtVGcLVBp81QABeDqZCXhkAAIzBAACL1C1U1BhJllLO8FJOAQ"
tankist         = "AgACAgIAAxkBAAO-aWZ5E9HnkEu_15d1sFkvlr4skFkAAnwSaxttODFLEjpPniWwqSUBAAMCAAN4AAM4BA"
absolute        = "AgACAgIAAxkBAAPLaW9FR8M_DlQbCxhQ_oRawyJPocgAAscLaxuE3YBLKWgmS1UyIn8BAAMCAAN5AAM4BA"
outtake_lude    = "AgACAgIAAxkBAAPMaW9FdREh4Mb5y0NENUnwulLSiOYAAskLaxuE3YBLLa5e0PJq2QQBAAMCAAN5AAM4BA"
zavozik         = "AgACAgIAAxkBAAP0aW9Wydrq5LzjAo-m74XWaj0O6kkAAnwMaxuE3YBLCY2z2LHFCxIBAAMCAAN4AAM4BA"
sergey          = "AgACAgIAAxkBAAPOaW9FyD3plsgBspRSETdOuPBMBeoAAtALaxuE3YBLXjyNjTlVg5YBAAMCAAN5AAM4BA"
sidzi           = "AgACAgIAAxkBAAPRaW9GC_25qRIQRRu3txv3aSgm_EIAAtQLaxuE3YBLKD3mtJCP2Y4BAAMCAAN4AAM4BA"
pidarasa        = "AgACAgIAAxkBAAPSaW9GKC45SP8oIH5GvSwLbClEjUMAAtcLaxuE3YBLt4Jjoi5gSaYBAAMCAAN5AAM4BA"
operoma         = "BAACAgIAAxkBAAPTaW9HQQg2C-ejVWdOJJS1GSC7CssAAnWJAAKE3YBL7down5xYU9Q4BA"
molchun         = "AgACAgIAAxkBAAPUaW9I2__Oc-4Hb4Yoe2vluTQCFFkAAusLaxuE3YBLDA5YS1d0aQwBAAMCAAN5AAM4BA"
hay_giler       = "AgACAgIAAxkBAAPVaW9I8bQ-I577DDrkS8vSFhGm-8oAAuwLaxuE3YBL7WYMb6DhBWwBAAMCAAN5AAM4BA"
shurupe_benzine = "AgACAgIAAxkBAAPWaW9JDK0AAZTQDkdapA9ZajBjuf9OAALtC2sbhN2ASxnTWzwmPUeWAQADAgADeQADOAQ"
sapogi          = "AgACAgIAAxkBAAPXaW9JLA4my1mJQ_RddLNPYkFfIhUAAvELaxuE3YBLwGr7R1kjUJoBAAMCAAN5AAM4BA"
pamaty          = "AgACAgIAAxkBAAPYaW9JR8sWkzexFvkO6gsoK0Dfy-8AAvILaxuE3YBLF3cPvBEsTo4BAAMCAAN5AAM4BA"
AAAA            = "AgACAgIAAxkBAAPZaW9JX-mKLJWJWSFyKtH_72aT1h4AAvQLaxuE3YBLAAGQTBTaYO4HAQADAgADeQADOAQ"
pidaras         = "AgACAgIAAxkBAAPaaW9Jgr5xqIgLkelHAAGVs__kWsyIAAL4C2sbhN2ASwABuYK-QpPnzQEAAwIAA3gAAzgE"
advokat         = "BAACAgIAAxkBAAPbaW9JtucYCmrkAAEYA8bTbMS5S35BAAKgiQAChN2ASyztqGa6l4QsOAQ"
dance           = "BAACAgIAAxkBAAPlaW9NwNOUUPiQGDNaikuZJFCn0AgAAgSIAAJDmlBKHnP9yFRreSI4BA"
pedick          = "AgACAgIAAxkBAAIBDGlvYKvWPNCzUgUf0bD-Os89fA4ZAALqDGsbhN2AS-c4HUb_ISa2AQADAgADeQADOAQ"
xyesos          = "CAACAgIAAx0CYjMl9wABAc3EaW-K1kS2Z-S3m9jqbitrXTTB5TQAAjUdAAJ9UKhIUJJ6M3Ok80c4BA"
xyesosaa        = "AgACAgIAAxkBAAIBg2lvlMLVPDZVDN0SOx55HfqgeaL4AAI5EGsb7uV4SwmE49CFCKWcAQADAgADeQADOAQ"
aboba           = "AgACAgIAAxkBAAIBhWlvlP8TrAesnzLSdKok_iVQGughAAIyEGsb7uV4Syzseq-jKlfeAQADAgADeQADOAQ"
fisher          = "AgACAgIAAxkBAAIBhGlvlOqyFc9zn7CqeKbADL2GsWA3AAI9EGsb7uV4SwqGORgggyqRAQADAgADeQADOAQ"
papa            = "AgACAgIAAxkBAAICq2lyS-CQXI0v7ki3JQstnkmk63iNAALnEmsbcDWRS8Gl1U1Ghw9_AQADAgADeQADOAQ"
deadinside            = "CAACAgIAAx0CYjMl9wABAdGCaXIt25F549kFHFS0ghD0r-LXuzoAApU2AAKySBFI2a7AYscanJY4BA"

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
    "хуисосатели"                   : ('photo', xyesosaa),
    "макан"                         : ('message', "Хуесос  ┌∩┐(◣_◢)┌∩┐"),
    "хуесос"                        : ('sticker', xyesos),
    "абоба"                         : ('photo', aboba),
    "рыбак"                         : ('photo', fisher),
    "папочка зол"                   : ('photo', papa),
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
        if "1000-7" in text:
            await deadinside_func(update, context)
            return

        if "рома" in text or "ромчик" in text:
            send_method = send_functions["message"](context.bot)
            await send_method(chat_id, "Пошел нахуй Ромчик(@roma_kaurcev) ψ(▼へ▼メ)～→")

        if "я" == text:
            send_method = send_functions["message"](context.bot)
            await send_method(chat_id, "Головка от хуя  (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ")

        for trigger, (media_type, reply) in triggers.items():
            if trigger in text:
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
        print(f"Не удалось отправить видеo: {e}")

async def deadinside_func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text="dead inside 1000-7"
        )
        n = 1000
        while n > 0:
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"{n}-7"
            )
            n -= 7
        await context.bot.send_sticker(
            chat_id=chat_id,
            sticker=deadinside,
        )
    except Exception as e:
        print(f"Не 1000-7 {e}")

async def list_nicks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    name = context.args[0] if len(context.args) == 1 else ""

    nicks = '\n'.join(get_nicks_for_name(name))
    reply_string = f'Вот ники для имени: {name}\n\n' + nicks

    try:
        await context.bot.send_message(
            chat_id=chat_id,
            text=reply_string
        )
    except Exception as e:
        print(f"Не удалось отправить ники: {e}")

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
    try:
        await context.bot.send_message(
            chat_id=CHATS[0],
            text="/pidor@SublimeBot"
        )
    except Exception as e:
        print(f"Не удалось ответить: {e}")

async def set_daily_reminder(app: Application) -> None:
    bot = app.bot
    try:
        app.job_queue.run_daily(
            callback_alarm,
            time=datetime.time(1, 00, 00, tzinfo=datetime.timezone.utc)
        )
    except Exception as e:
        print(f"Не удалось поставить напоминалку: {e}")

def main() -> None:
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN environment variable not set!")

    app = (
        Application
            .builder()
            .post_init(set_daily_reminder)
            .token(token)
            .build()
    )

    app.add_handler(CommandHandler("fuck", fuck_func))
    app.add_handler(CommandHandler("suck", suck_func))
    app.add_handler(CommandHandler("dance", dance_func))
    app.add_handler(CommandHandler("list_words", list_words_func))
    app.add_handler(CommandHandler("nick", list_nicks))

    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        react_on_message
    ))

    app.add_handler(MessageHandler(
        filters.ANIMATION | filters.ATTACHMENT,
        echo_media
    ))

    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )

if __name__ == "__main__":
    main()