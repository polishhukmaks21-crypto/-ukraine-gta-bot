import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.environ["BOT_TOKEN"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Игровая валюта", callback_data="currency")],
        [InlineKeyboardButton("🏢 Игровые бизнесы", callback_data="businesses")],
        [InlineKeyboardButton("📞 Поддержка", callback_data="support")],
    ]

    await update.message.reply_text(
        "🇺🇦 Ukraine GTA — Магазин\n\n"
        "🛒 Выберите категорию:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "currency":
        keyboard = [
            [InlineKeyboardButton("💰 1 000 000 — 30 грн", callback_data="buy_currency")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")],
        ]

        await query.edit_message_text(
            "💰 Игровая валюта\n\nВыберите нужное количество:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "businesses":
        keyboard = [
            [InlineKeyboardButton("🎰 Казино — 15 000$", callback_data="buy_casino")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")],
        ]

        await query.edit_message_text(
            "🏢 Игровые бизнесы\n\nВыберите бизнес:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "buy_currency":
        await query.edit_message_text(
            "💰 1 000 000 игровой валюты — 30 грн\n\n"
            "🛒 Для покупки обратитесь в поддержку."
        )

    elif query.data == "buy_casino":
        await query.edit_message_text(
            "🎰 Казино — 15 000$\n\n"
            "🛒 Для покупки обратитесь в поддержку."
        )

    elif query.data == "support":
        await query.edit_message_text(
            "📞 Поддержка\n\n"
            "По вопросам покупки обратитесь к администратору."
        )

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("💰 Игровая валюта", callback_data="currency")],
            [InlineKeyboardButton("🏢 Игровые бизнесы", callback_data="businesses")],
            [InlineKeyboardButton("📞 Поддержка", callback_data="support")],
        ]

        await query.edit_message_text(
            "🇺🇦 Ukraine GTA — Магазин\n\n"
            "🛒 Выберите категорию:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()


if __name__ == "__main__":
    main()
