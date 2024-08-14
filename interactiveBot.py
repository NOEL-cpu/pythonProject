# нужно создать кнопку в боте после которой запускается режим тренировки

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Запоминание слов", callback_data='remember_words')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите действие:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'remember_words':
        query.edit_message_text(text="Вы выбрали 'Запоминание слов'!")

def main():
    # Замените 'YOUR_TOKEN' на ваш реальный токен API Telegram Bot
    updater = Updater("YOUR_TOKEN", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
