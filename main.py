# Напишите бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)


from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

with open('../token.txt') as token:
    TOKEN = token.readline()

bot = Bot(token=TOKEN)
upd = Updater(token=TOKEN)
dispatcher = upd.dispatcher

def start(update,context):
    context.bot.send_message(update.effective_chat.id, 'Привет, пользователь.')

def abv2_del(update,context):
    words = update.message.text.split()
    edited_text = [word for word in words if not 'абв' in word.lower()]
    print(edited_text)
    context.bot.send_message(update.effective_chat.id, ' '.join(edited_text[1:]))

def abv_del(update,context):
    words = update.message.text.split()
    edited_text = [word for word in words if not 'абв' in word.lower()]
    context.bot.send_message(update.effective_chat.id, ' '.join(edited_text))

start_handler = CommandHandler('start', start)
abv2_handler = CommandHandler('abv', abv2_del)
abv_handler = MessageHandler(Filters.text, abv_del)
 
dispatcher.add_handler(start_handler)
dispatcher.add_handler(abv_handler)

upd.start_polling()
upd.idle()