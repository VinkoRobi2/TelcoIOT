import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

Token = '7013989876:AAFm44mpmZLJNTh4mx_esxcBslTqZ97pjC8'
bot = telebot.TeleBot(Token)

# Variable global para mantener el estado del bot
bot_activado = True

@bot.message_handler(commands=['help', 'start',])
def enviarsms(message):
    global bot_activado
    markup = ReplyKeyboardMarkup(row_width=2)  # Modificación aquí
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
    global bot_activado
    random2 = random.randint(1,2)
    if random2 == 1:
     bot.send_message(message.chat.id, 'Entiendo. Si necesitas ayuda más tarde, ¡no dudes en contactarme nuevamente!')
    elif random2 == 2:
        bot.send.message(message.chat.id,'Listo. Si me necesitas mas tarde, !no dudes en escribirme')
    bot_activado = False

@bot.message_handler(func=lambda message: not bot_activado)
def reactivar_bot(message):
    global bot_activado
    bot_activado = True
    enviarsms(message)

@bot.message_handler(func=lambda message: message.text == 'Sí, deseo saber la temperatura')
def ubicacion_temperatura(message):
    global bot_activado
    bot.send_message(message.chat.id, '¡Genial! ¿De qué ubicación deseas saber la temperatura?', reply_markup=generar_teclado_ubicaciones())
    bot_activado = True

def generar_teclado_ubicaciones():
    markup = ReplyKeyboardMarkup(row_width=2,one_time_keyboard=True)
    item1 = KeyboardButton("Kennedy")
    item2 = KeyboardButton("Campamento")
    markup.add(item1, item2)
    return markup

def QuedeseassaberK():
    markup = ReplyKeyboardMarkup(row_width=2)
    item1 = KeyboardButton('Temperatura')
    item2 = KeyboardButton('Ph del ambiente')
    markup.add(item1,item2)
    return markup
def QuedeseassaberC():
    markup = ReplyKeyboardMarkup(row_width=2)
    item1 = KeyboardButton('Temperatura')
    item2 = KeyboardButton('Ph del ambiente')
    markup.add(item1,item2)
    return markup
@bot.message_handler(func=lambda message: message.text.lower() == 'kennedy' or message.text.lower() == 'campamento')
def handle_message(message):
    chat_id = message.chat.id
    if message.text.lower() == 'kennedy':
        bot.send_message(chat_id, "Selecciona lo que deseas saber en Kennedy:", reply_markup=QuedeseassaberK())
    elif message.text.lower() == 'campamento':
        bot.send_message(chat_id, "Selecciona lo que deseas saber en Campamento:", reply_markup=QuedeseassaberC())

def clear_messages(message):
    chat_id = message.chat.id
    message_id = message.message_id
    messages = bot.history(chat_id, limit=100)  
    for msg in messages:
        bot.delete_message(chat_id, msg.message_id)

def iniciar_bot():
    bot.polling(none_stop=True)

# Iniciar el bot
if __name__ == "__main__":
    iniciar_bot()