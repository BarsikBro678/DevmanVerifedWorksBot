import os

import requests
import telegram


def get_verifed_work(devman_api_key, timestamp=None):
    url = "https://dvmn.org/api/long_polling/"
    payload = {
	"timestamp": timestamp,
    }
    headers = {
	"Authorization": f"Token {devman_api_key}"
    }
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()


def telegram_bot(bot, chat_id, devman_api_key):
    timestamp = None
    while True:
	try:
	    work = get_verifed_work(devman_api_key, timestamp=timestamp)
				
	    if work["status"] == "timeout":
		timestamp = work["timestamp_to_request"]
	    else:
		timestamp = None
		if work["new_attempts"][0]["is_negative"]:
		    bot.send_message(chat_id=chat_id, text=f"Преподаватель оценил вашу работу 
      <<{work['new_attempts'][0]['lesson_title']}>>!	                       
      К сожалению, в работе нашлись ошибки.")
		else:
		    bot.send_message(chat_id=chat_id, text=f"Преподаватель оценил вашу работу 
      <<{work['new_attempts'][0]['lesson_title']}>>!	                       
      Преподавателю все понравилось, можно приступать к следуещему уроку!")

	except requests.exceptions.ReadTimeout or ConnectionError:
	    pass

	
def main():
    chat_id = os.environ["CHAT_ID"]
    telegram_bot_key = os.environ["TELEGRAM_BOT_KEY"]
    devman_api_key = os.environ["DEVMAN_API_KEY"]
    bot = telegram.Bot(token=telegram_bot_key)
    telegram_bot(bot, chat_id, devman_api_key)


if __name__ == "__main__":
    main()
