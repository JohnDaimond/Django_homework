import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot("5930755466:AAGscYvfU00PUF0lDhExIb2H-xxeGEoi-bQ")

#@bot.message_handler(commands=["start"])
#def start(message):
 #   markup = types.ReplyKeyboardMarkup()
  #  btn1 = types.KeyboardButton("Перейти на сайт")
   # btn2 = types.KeyboardButton("Вызвать мастера")
    #markup.row(btn1, btn2)
   # btn3 = types.KeyboardButton("Ремонт")
   # btn4 = types.KeyboardButton("Модернизация")
   # markup.row(btn3, btn4)
   # bot.send_message(message.chat.id, f"<b>Приветствую {message.from_user.first_name}\n что вас интересует?</b>",
   #                  parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=["site", "website"])
def site(message):
    webbrowser.open('https://911-it-master.by/')

@bot.message_handler(commands=["start"])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url='https://911-it-master.by/')
    btn2 = types.InlineKeyboardButton("Вызвать мастера", callback_data='Edit')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton("Ремонт", callback_data='Eda')
    btn4 = types.InlineKeyboardButton("Модернизация", callback_data='Ed')
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, f"<b>Приветствую {message.from_user.first_name}\n что вас интересует?</b>", parse_mode = "html", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, "Website is open")

@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти на сайт", url= 'https://911-it-master.by/' )
    btn2 = types.InlineKeyboardButton("Вызвать мастера", callback_data='Edit')
    markup.row(btn1, btn2)
    bot.reply_to(message, "Понял Вашу проблему перейдите на наш сайт или оставьте заявку для вызова мастера", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "Edit":
        bot.edit_message_text("+375295954567", callback.message.chat.id, callback.message.message_id)
    elif callback.data == "Ed":
        bot.edit_message_text("Модернизация временно не возможна, позвоните по номеру +375295954567 для консультации ", callback.message.chat.id, callback.message.message_id)
    elif callback.data == "Eda":
        bot.edit_message_text("Мы получили вашу заявку, наш консультат свяжется с вами", callback.message.chat.id, callback.message.message_id)

@bot.message_handler()
def info(message):
    if message.text.lower() == "Спасибо":
        bot.send_message(message.chat.id, f"благодарим вас что обратились к нам")


bot.polling(none_stop=True)
##