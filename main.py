import telebot

TOKEN = "8423725996:AAGi92MUk53ZHk8aOAHRj2ywcuTzXWFIHu0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🎉 خوش آمدی به Woso Collection Bot!")

bot.polling()
