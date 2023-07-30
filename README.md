## Бот присылающий твои работы с [Девмана](https:/devman.org/)

Этот бот с помощью твоего Devman Api Key и твоего ID в [Telegram](https://web.telegram.org/)(его можно узнать у @userinfobot) присылает
тебе твои проверенные работы и их результат.

### Как установить
 
Создайте бота в телеграмме у @BotFather.

Создайте и запишите в корневой файл ```.env```:
```
DEVMAN_API_KEY=ваш Devman Api Key
TELEGRAM_BOT_KEY=ваш токен бота
MY_CHAT_ID=ваш ID в Telegram(как его узнать написано в начале)
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Для запуска введите в терминал команду:
```
python main.py
```
