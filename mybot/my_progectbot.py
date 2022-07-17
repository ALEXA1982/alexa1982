import telebot


bot=telebot.TeleBot("5430587993:AAEpmfnI8Gp3rsaelvwjf848Ji1tE3BHmmg")
@bot.message_handler(content_types=["text","document","audio"])
def get_text_message(message):
    if message.text=="hello":
        bot.send_message(message.from_user.id, "Привет,чем могу ?")
    elif message.text=="/help":
        bot.send_message(message.from_user.id, "Пиши привет")
    else:
        bot.send_message(message.from_user.id, "Не понимаю,пиши/Help ")


bot.polling(none_stop=True,interval=0)
