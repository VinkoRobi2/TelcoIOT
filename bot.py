import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

Token = '7013989876:AAFm44mpmZLJNTh4mx_esxcBslTqZ97pjC8'
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['help', 'start'])
def enviarsms(message):
    markup = ReplyKeyboardMarkup(row_width=2)
    item1 = KeyboardButton("Sí, deseo saber la temperatura")
    item2 = KeyboardButton("No, tal vez más tarde")
    markup.add(item1, item2)
    
    random_number = random.randint(1, 2)
    if random_number == 1:
        bot.reply_to(message, '¡Hola! Soy TelcoIot, tu asistente para consultas sobre temperatura. ¿Necesitas saber cómo está el clima hoy?', reply_markup=markup)
    elif random_number == 2:
        bot.reply_to(message, '¡Hola! Soy TelcoIot, aquí estoy para mantenerte al día con la temperatura. Si alguna vez necesitas conocer la temperatura actual o previsiones para tu área, ¡no dudes en preguntar! Estoy aquí para ayudarte.', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'No, tal vez más tarde')
def detener_bot(message):
    bot.send_message(message.chat.id, 'Entiendo. Si necesitas ayuda más tarde, ¡no dudes en contactarme nuevamente!')
    bot.stop_polling()


@bot.message_handler(func=lambda message: message.text == 'Sí, deseo saber la temperatura')
def ubicacion_temperatura(message):
    bot.send_message(message.chat.id, '¡Genial! ¿De qué ubicación deseas saber la temperatura?', reply_markup=generar_teclado_ubicaciones())

def generar_teclado_ubicaciones():
    markup = ReplyKeyboardMarkup(row_width=2)
    item1 = KeyboardButton("Kennedy")
    item2 = KeyboardButton("Campamento")
    markup.add(item1, item2)
    return markup

@bot.message_handler(func=lambda message: message.text == "Kennedy")
def QuedeseassaberK(message):
    bot.send_message(message.chat.id, '!Bien, ¿Qué específicamente deseas saber de Kennedy?', reply_markup=Opcines() )


@bot.message_handler(func=lambda message: message.text =='Campamento')
def QuedeseassaberC(message):
    bot.send_message(message.chat.id,'!Bien que deseas saber de Campamento', reply_markup=Opcines())

def Opcines():
    markup = ReplyKeyboardMarkup(row_width=2)
    item1 = KeyboardButton('Temperatura')
    item2 = KeyboardButton('Ph del ambiente')
    markup.add(item1,item2)
bot.polling()
