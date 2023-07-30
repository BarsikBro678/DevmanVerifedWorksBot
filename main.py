import os

import requests
import telegram


def get_verifed_work(devman_api_key, timestamp=None):
	url = "https://dvmn.org/api/long_polling/"
	if timestamp:
		url = f"{url}?timestamp={timestamp}"
	headers = {
		"Authorization": f"Token {devman_api_key}"
	}
	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
		return response.json()
	except requests.exceptions.ReadTimeout or ConnectionError:
		return get_my_verifed_work(devman_api_key)


def telegram_bot(bot, chat_id, devman_api_key):
	timestamp = None
	while True:
		my_work = get_verifed_work(devman_api_key, timestamp=timestamp)
		if my_work["status"] == "timeout":
			timestamp = my_work["timestamp_to_request"]
		else:
			timestamp = None
			if my_work["new_attempts"][0]["is_negative"]:
				bot.send_message(chat_id=chat_id, text=f"Преподаватель оценил вашу работу <<{my_work['new_attempts'][0]['lesson_title']}>>!	                                                                К сожалению, в работе нашлись ошибки.")
			else:
				bot.send_message(chat_id=chat_id, text=f"Преподаватель оценил вашу работу <<{my_work['new_attempts'][0]['lesson_title']}>>!	                                                                Преподавателю все понравилось, можно приступать к следуещему уроку!")

	
def main():
	chat_id = os.environ["MY_CHAT_ID"]
	telegram_bot_key = os.environ["TELEGRAM_BOT_KEY"]
	devman_api_key = os.environ["DEVMAN_API_KEY"]
	bot = telegram.Bot(token=telegram_bot_key)
	telegram_bot(bot, chat_id, devman_api_key)
