import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import requests

Token = '7013989876:AAFm44mpmZLJNTh4mx_esxcBslTqZ97pjC8'
device_idKennedy = 'wfdtgg'
device_keyK = '645d5238a8f2dd53ed4655b0'

nivelruidoCampamento = '645d52397031cc4f0d13a7fe'
bot = telebot.TeleBot(Token)
bot_activado = True

device_keyC = '6453e976fc27ea000d816cb1'

token = 'BBUS-1GKmVj02Wr3TCfqEy6LgyyVRgLJVZG'

 

def get_temperatureCampamento(device_keyC, token,call):
    url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyC}/_/values/last'
    headers = {'X-Auth-Token': token}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        temperature_data = data.get('temperature')
        PolucionC = data.get('pm2.5')
        H_data = data.get('relhumidity')
        NlevelC = data.get('noiselevel')
        temperature_value = temperature_data.get('value')
        Polucion_value = PolucionC.get('value')
        H_value = H_data.get('value')
        Nlevel_value =  NlevelC.get('value')
        rounded_temperature = round(temperature_value)
        rounded_Polucion = round(Polucion_value)
        rounded_humedad = round(H_value )
        rounded_Ruido = round(Nlevel_value)
        bot.send_message(call.message.chat.id, f"¡Gracias por compartir tu ubicación! Aquí tienes los datos climáticos para tu área")
        bot.send_message(call.message.chat.id, f"La temperatura en Telco City es: {rounded_temperature}°C")
        bot.send_message(call.message.chat.id, f"La Humedad en Telco City es: {rounded_humedad} %")
        bot.send_message(call.message.chat.id, f"El nivel de polucion en Telco City es: {rounded_Polucion} ppm")
        bot.send_message(call.message.chat.id, f"El nivel de ruido en Telco City es: {rounded_Ruido} db")
        markup = InlineKeyboardMarkup(row_width=2)
        item1 = InlineKeyboardButton("Sí, me gustaria saber", callback_data='temperature')
        item2 = InlineKeyboardButton("No, gracias", callback_data='later')
        markup.add(item1, item2)
        bot.send_message(call.message.chat.id, '¿Te gustaría conocer el pronóstico de otro lugar?', reply_markup=markup)



    except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"


def get_temperatureKennedy(device_keyK,token,call):
       url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyK}/_/values/last'
       headers = {'X-Auth-Token': token}
       try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
            data = response.json()
            print(data)
            temperature_data = data.get('temperature')
            PolucionC = data.get('pm2.5')
            H_data = data.get('relhumidity')
            NlevelC = data.get('noiselevel')
            temperature_value = temperature_data.get('value')
            Polucion_value = PolucionC.get('value')
            H_value = H_data.get('value')
            Nlevel_value =  NlevelC.get('value')
            rounded_temperature = round(temperature_value)
            rounded_Polucion = round(Polucion_value)
            rounded_humedad = round(H_value )
            rounded_Ruido = round(Nlevel_value)
            bot.send_message(call.message.chat.id, f"¡Gracias por compartir tu ubicación! Aquí tienes los datos climáticos para tu área")
            bot.send_message(call.message.chat.id, f"La temperatura en Kennedy es: {rounded_temperature}°C")
            bot.send_message(call.message.chat.id, f"La Humedad en Kennedy es: {rounded_humedad} %")
            bot.send_message(call.message.chat.id, f"El nivel de polucion en Kennedy es: {rounded_Polucion} ppm")
            bot.send_message(call.message.chat.id, f"El nivel de ruido en Kennedy es {rounded_Ruido} db")
            markup = InlineKeyboardMarkup(row_width=2)
            item1 = InlineKeyboardButton("Sí, me gustaria saber", callback_data='temperature')
            item2 = InlineKeyboardButton("No, gracias", callback_data='later')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, '¿Te gustaría conocer el pronóstico de otro lugar?', reply_markup=markup)

       except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"

@bot.message_handler(func=lambda message: True)
def on_any_message(message):
    global bot_activado
    if bot_activado:
        markup = InlineKeyboardMarkup(row_width=2)
        item1 = InlineKeyboardButton("Sí, por favor", callback_data='temperature')
        item2 = InlineKeyboardButton("No en este momento", callback_data='later')
        markup.add(item1, item2)
        bot.reply_to(message, '¡Hola! Soy AirScan, tu bot meteorológico personal. Estoy aquí para ofrecerte pronósticos precisos y consejos meteorológicos.¿Quieres continuar?', reply_markup=markup)
        
    else:
        markup = InlineKeyboardMarkup(row_width=2)  
        item1 = InlineKeyboardButton("Sí, por favor", callback_data='temperature')  
        item2 = InlineKeyboardButton("No en este momento,", callback_data='later')  
        markup.add(item1, item2)
        bot_activado = True
        bot.reply_to(message, '¡Hola! Soy AirScan, tu bot meteorológico personal. Estoy aquí para ofrecerte pronósticos precisos y consejos meteorológicos. ¿Quieres continuar?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'temperature')
def ubicacion_temperatura(call):
    global bot_activado
    bot.send_message(call.message.chat.id, '¡Genial! ¿De qué ubicación deseas obtener el pronóstico', reply_markup=generar_teclado_ubicaciones())
    bot_activado = True



@bot.callback_query_handler(func=lambda call: call.data == 'later')
def detener_bot(call):
    global bot_activado
    random2 = random.randint(1, 2)
    if random2 == 1:
        bot.send_message(call.message.chat.id, 'Entiendo. Si necesitas ayuda más tarde, ¡no dudes en contactarme nuevamente!')
    elif random2 == 2:
        bot.send_message(call.message.chat.id, 'Listo. Si me necesitas mas tarde, ¡no dudes en escribirme!')
    bot_activado = False




@bot.message_handler(func=lambda message: not bot_activado)
def reactivar_bot(message):
    global bot_activado
    bot_activado = True
    on_any_message(message)



def generar_teclado_ubicaciones():
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton("Kennedy", callback_data='kennedy')
    item2 = InlineKeyboardButton("Telco City", callback_data='campamento')
    markup.add(item1, item2)
    return markup



@bot.callback_query_handler(func=lambda message:message.data == 'VolverO')
def Volver(call):
    bot.send_message(call.message.chat.id, "Volviendo al menú de opciones...") 
    bot.send_message(call.message.chat.id, "¿De qué ubicación deseas saber la temperatura?", reply_markup=generar_teclado_ubicaciones())







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
    #bot.stop_polling()



@bot.callback_query_handler(func=lambda call: call.data.lower() in ['kennedy', 'campamento'])
def handle_location(call):
    chat_id = call.message.chat.id
    location = call.data.lower()
    if location == 'kennedy':
        get_temperatureKennedy(device_keyK,token,call)
    elif location == 'campamento':
        get_temperatureCampamento(device_keyC, token,call)
def iniciar_bot():
    bot.polling(none_stop=True)




if __name__ == "__main__":
    iniciar_bot()



print('Rob $tone two damm phones babilons can`t track the code ')
print('Dos mil 16')
