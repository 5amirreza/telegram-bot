import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
bot.reply_to(message, "سلام! ربات با موفقیت فعال شد 🤖")

@bot.message_handler(func=lambda message: True)
def reply(message):
bot.reply_to(message, message.text)

bot.infinity_polling()
