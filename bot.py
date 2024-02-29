import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import requests

Token = '7013989876:AAFm44mpmZLJNTh4mx_esxcBslTqZ97pjC8'
device_idCampamentoT = '6462b70d98d170000e17e2eb'
nivelruidoCampamento = '645d52397031cc4f0d13a7fe'
UbidotsApi = 'BBFF-c7ca19a5ea8b53148a75a818823f5fe9ec9'
bot = telebot.TeleBot(Token)
bot_activado = True




def get_temperatureCampamento():
 url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{device_idCampamentoT}/?token={UbidotsApi}'
 response = requests.get(url)
 print(response)
 if response.status_code == 200:
        data = response.json()
        temperature = data['results'][0]['value']
        return temperature
 else:
    return None


#def get_temperatureKennedy():
  #   url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{device_idKennedy}/temperatura/values/?token={UbidotsApi}&page_size=1'

#def get_HumedadCampamento():
   #   url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{device_idCampamento}/temperatura/values/?token={UbidotsApi}&page_size=1'

#def get_HumedadKennedy():
  #url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{device_idKennedy}/temperatura/values/?token={UbidotsApi}&page_size=1'

#def get_RuidoCampamento():
    #url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{nivelruidoCampamento}/temperatura/values/?token={UbidotsApi}&page_size=1'

#def get_RuidoKennedy():
       # url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{device_idCampamento}/temperatura/values/?token={UbidotsApi}&page_size=1'


@bot.message_handler(func=lambda message: True)
def on_any_message(message):
    global bot_activado
    if bot_activado:
        markup = InlineKeyboardMarkup(row_width=2)
        item1 = InlineKeyboardButton("Sí, deseo saber.", callback_data='temperature')
        item2 = InlineKeyboardButton("No, tal vez más tarde", callback_data='later')
        markup.add(item1, item2)
        random_number = random.randint(1, 2)
        if random_number == 1:
            bot.reply_to(message, '¡Hola! Soy TelcoIot, tu asistente para consultas sobre temperatura. ¿Necesitas saber cómo está el clima hoy?', reply_markup=markup)
        elif random_number == 2:
            bot.reply_to(message, '¡Hola! Soy TelcoIot, aquí estoy para mantenerte al día con la temperatura. Si alguna vez necesitas conocer la temperatura actual o previsiones para tu área, ¡no dudes en preguntar! Estoy aquí para ayudarte.', reply_markup=markup)
        bot_activado = False

@bot.callback_query_handler(func=lambda call: call.data == 'later')
def detener_bot(call):
    global bot_activado
    random2 = random.randint(1, 2)
    if random2 == 1:
        bot.send_message(call.message.chat.id, 'Entiendo. Si necesitas ayuda más tarde, ¡no dudes en contactarme nuevamente!')
    elif random2 == 2:
        bot.send_message(call.message.chat.id, 'Listo. Si me necesitas mas tarde, ¡no dudes en escribirme!')
    bot_activado = False

@bot.callback_query_handler(func=lambda call: call.data == 'temperature')
def ubicacion_temperatura(call):
    global bot_activado
    bot.send_message(call.message.chat.id, '¡Genial! ¿De qué ubicación deseas saber la temperatura?', reply_markup=generar_teclado_ubicaciones())
    bot_activado = True

@bot.message_handler(func=lambda message: not bot_activado)
def reactivar_bot(message):
    global bot_activado
    bot_activado = True
    on_any_message(message)

def generar_teclado_ubicaciones():
    markup = InlineKeyboardMarkup(row_width=2)
    item1 = InlineKeyboardButton("Kennedy", callback_data='kennedy')
    item2 = InlineKeyboardButton("Campamento", callback_data='campamento')
    markup.add(item1, item2)
    return markup

def QuedeseassaberK():
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton('Temperatura', callback_data='temp_kennedy')
    item2 = InlineKeyboardButton('Ph del ambiente', callback_data='ph_kennedy')
    item3 = InlineKeyboardButton('Humedad',callback_data='humedad_kennedy')
    item4 = InlineKeyboardButton('Nivel de Ruido',callback_data='NivelRuido_kennedy')
    markup.add(item1, item2,item3,item4)
    return markup

@bot.callback_query_handler(func=lambda call: call.data == 'temp_campamento')
def handle_temperature_callback(call):
    temperature = get_temperatureCampamento()
    if temperature is not None:
        bot.send_message(call.message.chat.id, f"La temperatura de Campamento es: {temperature}°C")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener la temperatura de Campamento en este momento. Inténtalo de nuevo más tarde.")
        # Si no se puede obtener la temperatura, también envía el teclado de opciones
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
def generar_teclado_opciones():
    markup = InlineKeyboardMarkup(row_width=2)
    item1 = InlineKeyboardButton("Salir", callback_data='exit')
    item2 = InlineKeyboardButton("Volver al menú", callback_data='menu')
    markup.add(item1, item2)
    return markup

@bot.callback_query_handler(func=lambda call: call.data == 'exit')
def handle_exit(call):
    bot.send_message(call.message.chat.id, "¡Hasta luego! Si me necesitas mas tarde, envía cualquier mensaje nuevamente.")
    # Detener el bot
    bot.stop_polling()

@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def handle_menu(call):
    bot.send_message(call.message.chat.id, "Volviendo al menú de opciones...") 
    bot.send_message(call.message.chat.id, "Selecciona lo que deseas saber en Campamento:", reply_markup=QuedeseassaberC())
def QuedeseassaberC():
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton('Temperatura', callback_data='temp_campamento')
    item2 = InlineKeyboardButton('Ph del ambiente', callback_data='ph_campamento')
    item3 = InlineKeyboardButton('Humedad',callback_data='humedad_campamento')
    item4 = InlineKeyboardButton('Nivel de Ruido',callback_data='NivelRuido_campamejnto')
    markup.add(item1, item2,item4,item3)
    return markup

@bot.callback_query_handler(func=lambda call: call.data.lower() in ['kennedy', 'campamento'])
def handle_location(call):
    chat_id = call.message.chat.id
    location = call.data.lower()
    if location == 'kennedy':
        bot.send_message(chat_id, "Selecciona lo que deseas saber en Kennedy:", reply_markup=QuedeseassaberK())
    elif location == 'campamento':
        bot.send_message(chat_id, "Selecciona lo que deseas saber en Campamento:", reply_markup=QuedeseassaberC())
def iniciar_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    iniciar_bot()
