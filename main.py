import telebot

# Replace 'YOUR_API_TOKEN' with your actual Telegram Bot API token
API_TOKEN = 'YOUR_API_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I'm your AI bot. How can I help you today?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling()