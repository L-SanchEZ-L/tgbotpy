import pyowm
import telebot

 
owm = pyowm.OWM('12dae92ed6a64b461ffdedb00c6d4f77', language = 'ua')
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

if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://dashboard.heroku.com/apps/weather-tg-botpy")
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)

