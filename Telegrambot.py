import pyowm
import telebot

 
owm = pyowm.OWM('12dae92ed6a64b461ffdedb00c6d4f77', language = 'ua')
telebot.apihelper.proxy = {'https': 'https://78.47.202.24:8081'}
bot = telebot.TeleBot("701199951:AAGm5uAUEDfnXiDtmex0GLizwqcXwDR37s0")

@bot.message_handler(content_types=['text'])


def send_echo(message):
  try:
      observation = owm.weather_at_place(message.text) 
      w = observation.get_weather()
      temp = w.get_temperature('celsius')['temp']

      answer = ' В місці ' + message.text + ' зараз ' + w.get_detailed_status() + '\n'
      answer += 'Температура в районі ' + str(temp) + 'C°' + '\n\n'

  except pyowm.exceptions.api_response_error.NotFoundError:
    answer = 'Ви шо зовсім тупі?'
    
  finally:  
       
   bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )


