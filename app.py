import telebot
from credentials import bot_token
import requests
from io import BytesIO


bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'for start use /start')

@bot.message_handler(commands=['start'])
def send(message):
    try:
        index = 39554
        URL = f'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20%28Hosted%20Webcast%29-wbSwFU6tY1c/frame/{index}/'
        response = requests.get(URL)
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            bot.send_photo(message.chat.id, image_bytes)
            bot.reply_to(message, f'{index} - did the rocket launch yet?')
        else:
            bot.send_message(message.chat.id, f'No se pudo descargar la imagen desde la URL: {URL}')
    except Exception as e:
            bot.send_message(message.chat.id, f'Ocurrió un error: {str(e)}')

'''
@bot.message_handler(func = lambda message:True)
def receive_response(message):
    response = message.text
    if response.lower() == 'y':
        pass
    else:
        pass
    # bot.reply_to(message, f'{index} - did the rocket launch yet?')
    bot.reply_to(message, message.text)
'''

bot.polling()

# message confirm: f"{index} - did the rocket launch yet?"
# message final: f"Found! Take-off = {bisector.index}"

    # requests.get(f'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20%28Hosted%20Webcast%29-wbSwFU6tY1c/frame/{index}/')
    # print(message) # core.telegram.org/bots/api#sendPhoto
    # requests.post(f'https://api.telegram.org/bot{bot_token}/sendPhoto', files=file)
    # bot.send(image)
    # bot.send_photo(6199381027, 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20%28Hosted%20Webcast%29-wbSwFU6tY1c/frame/39554/')
    # with open('./theBotFather.png', 'rb') as photo:
        # bot.send_photo(message.chat.id, photo)
