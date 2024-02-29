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

 

def get_temperatureCampamento(device_keyC, token):
    url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyC}/_/values/last'
    headers = {'X-Auth-Token': token}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        temperature_data = data.get('temperature')
        if temperature_data:
          temperature_value = temperature_data.get('value')
        if temperature_value is not None:
           rounded_temperature = round(temperature_value)
           return rounded_temperature

    except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"

def PolucionCampamento(device_keyC,token):
   url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyC}/_/values/last'
   headers = {'X-Auth-Token': token}
   try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        PolucionC = data.get('pm2.5')
        if PolucionC:
          Polucion_value = PolucionC.get('value')
        if Polucion_value is not None:
           rounded_temperature = round(Polucion_value)
           return rounded_temperature

   except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"
   
def PolucionKennedy(device_keyK,token):
    url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyK}/_/values/last'
    headers = {'X-Auth-Token': token}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        PolucionK = data.get('pm2.5')
        if PolucionK:
          PolucionK_value = PolucionK.get('value')
        if PolucionK_value is not None:
           rounded_temperature = round(PolucionK_value)
           return rounded_temperature

    except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"
 

def get_temperatureKennedy(device_keyK,token):
       url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyK}/_/values/last'
       headers = {'X-Auth-Token': token}
       try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        temperature_data = data.get('temperature')
        if temperature_data:
          temperature_value = temperature_data.get('value')
        if temperature_value is not None:
           rounded_temperature = round(temperature_value)
           return rounded_temperature
       except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"

def get_HumedadCampamento(device_keyC, token):
    url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyC}/_/values/last'
    headers = {'X-Auth-Token': token}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        H_data = data.get('relhumidity')
        if H_data:
            H_value = H_data.get('value')
            if H_value is not None:
                rounded_humidity = round(float(H_value))
                return rounded_humidity
        return "No se encontró el valor de humedad en la respuesta."
    except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"



def get_HumedadKennedy(device_keyK,token):
  url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyK}/_/values/last'
  headers = {'X-Auth-Token': token}
  try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        HK_data = data.get('relhumidity')
        if HK_data:
          HK_value = HK_data.get('value')
        if HK_value is not None:
           rounded_temperature = round(HK_value)
           return rounded_temperature
  except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"

def get_RuidoCampamento(device_keyC,token):
    url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyC}/_/values/last'
    headers = {'X-Auth-Token': token}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        NlevelC = data.get('noiselevel')
        if  NlevelC :
             Nlevel_value =  NlevelC.get('value')
        if Nlevel_value is not None:
                rounded_humidity = round(float(Nlevel_value))
                return rounded_humidity
        return "No se encontró el valor de humedad en la respuesta."
    except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"



def get_RuidoKennedy():
       url = f'https://industrial.api.ubidots.com/api/v2.0/devices/{device_keyK}/_/values/last'
       headers = {'X-Auth-Token': token}
       try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanzar una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        print(data)
        NlevelK = data.get('relhumidity')
        if NlevelK:
          NlevelK_value = NlevelK.get('value')
        if  NlevelK_value is not None:
           rounded_humidityk = round( NlevelK_value)
           return rounded_humidityk
       except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"

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
    item2 = InlineKeyboardButton('Polucion', callback_data='polucion_kennedy')
    item3 = InlineKeyboardButton('Humedad',callback_data='humedad_kennedy')
    item4 = InlineKeyboardButton('Nivel de Ruido',callback_data='NivelRuido_kennedy')
    item5 = InlineKeyboardButton('Volver', callback_data='VolverO')
    markup.add(item1, item2,item3,item4,item5)
    return markup

@bot.callback_query_handler(func=lambda message:message.data == 'VolverO')
def Volver(call):
    bot.send_message(call.message.chat.id, "Volviendo al menú de opciones...") 
    bot.send_message(call.message.chat.id, "¿De qué ubicación deseas saber la temperatura?", reply_markup=generar_teclado_ubicaciones())

@bot.callback_query_handler(func=lambda message:message.data == "polucion_kennedy")
def handlerPollK(call):
    polucionK = PolucionKennedy(device_keyK,token)
    if polucionK is not None:
     bot.send_message(call.message.chat.id, f"El nivel de polucion de Kennedy es: {polucionK} ppm")
     bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener el nivel de polucion de kennedy en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())


@bot.callback_query_handler(func=lambda message: message.data == 'polucion_campamento')
def handler_Pollc(call):
    polucionC = PolucionCampamento(device_keyC, token)
    if polucionC is not None:
        bot.send_message(call.message.chat.id, f"El nivel de polucion de Campamento {polucionC} ppm")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener el nivel de polucion de campamento en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())





@bot.callback_query_handler(func=lambda message:message.data == 'NivelRuido_kennedy')
def handler_NoiseK(call):
    noiceK = get_RuidoKennedy()
    if noiceK is not None:
        bot.send_message(call.message.chat.id, f"El nivel de ruido de Kennedy es {noiceK} db")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener el nivel de ruido  de Kennedy en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())




@bot.callback_query_handler(func=lambda call:call.data == 'NivelRuido_campamejnto')
def handle_noiseC(call):
    noiseC = get_RuidoCampamento(device_keyC,token)
    if noiseC is not None:
        bot.send_message(call.message.chat.id,f"El nivel de ruido en Campamento es {noiseC} db" )
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener el nivel de ruido  de Campamento en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())



@bot.callback_query_handler(func=lambda call: call.data == "humedad_kennedy")
def handle_humidity_K(call):
    humidityK = get_HumedadKennedy(device_keyK,token)
    if humidityK is not None:
        bot.send_message(call.message.chat.id, f"La Humedad en Kennedy es: {humidityK} %")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener la humedad de Kennedy en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())

@bot.callback_query_handler(func=lambda call: call.data == 'humedad_campamento' )
def handle_Humidity_callback(call):
    humidity = get_HumedadCampamento(device_keyC,token)
    if humidity is not None:
        bot.send_message(call.message.chat.id, f"La Humedad en Campamento es: {humidity} %")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener la humedad de Campamento en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())


@bot.callback_query_handler(func=lambda call: call.data == 'temp_campamento')
def handle_temperature_callback(call):
    temperature = get_temperatureCampamento(device_keyC,token)
    if temperature is not None:
        bot.send_message(call.message.chat.id, f"La temperatura de Campamento es: {temperature}°C")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener la temperatura de Campamento en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())

@bot.callback_query_handler(func=lambda call: call.data == 'temp_kennedy')
def handle_temperature_callbackK(call):
    temperature = get_temperatureKennedy(device_keyK,token)
    if temperature is not None:
        bot.send_message(call.message.chat.id, f"La temperatura de Kennedy es: {temperature}°C")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener la temperatura de Kennedy en este momento. Inténtalo de nuevo más tarde.")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())



@bot.callback_query_handler(func=lambda call: call.data == 'temp_kennedy')
def handle_temperature_callbackk(call):
    temperature = get_temperatureKennedy()
    if temperature is not None:
        bot.send_message(call.message.chat.id, f"La temperatura de Kennedy es: {temperature}°C")
        bot.send_message(call.message.chat.id, "¿Qué deseas hacer?", reply_markup=generar_teclado_opciones())
    else:
        bot.send_message(call.message.chat.id, "No se pudo obtener la temperatura de Kennedy en este momento. Inténtalo de nuevo más tarde.")
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
    item2 = InlineKeyboardButton('Polucion Campamento', callback_data='polucion_campamento')
    item3 = InlineKeyboardButton('Humedad',callback_data='humedad_campamento')
    item5 = InlineKeyboardButton('Volver', callback_data='VolverO')
    item4 = InlineKeyboardButton('Nivel de Ruido',callback_data='NivelRuido_campamejnto')
    markup.add(item1, item2,item4,item3,item5)
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

