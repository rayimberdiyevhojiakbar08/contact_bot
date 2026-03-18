import telebot
from telebot import types
from flask import Flask, request

TOKEN = ""
ADMIN_ID =

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn1 = types.InlineKeyboardButton('Asosiy profile', url='https://t.me/rayimberdiyev_08')
    btn2 = types.InlineKeyboardButton('2', url='https://t.me/xdevreal')
    btn3 = types.InlineKeyboardButton('3', url='https://t.me/rhxreal')

    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Salom! Xabar yozing.", reply_markup=markup)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'voice'])
def forward_to_admin(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.reply_to(message, "Qabul qilindi ✅")

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/')
def index():
    return "Bot ishlayapti 🚀"
