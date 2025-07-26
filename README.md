Weather Telegram Bot
Бот для отримання прогнозу погоди за назвою міста. Використовує OpenWeatherMap API.

Вимоги
Python 3.10+

Токен Telegram Bot (створюється через @BotFather)

Ключ OpenWeatherMap API (реєстрація на openweathermap.org)

Встановлення

git clone https://github.com/your-username/iasc-marathon.git
cd iasc-marathon
python -m venv venv
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
Налаштування
Створити файл .env у корені проєкту та вказати дані:

TELEGRAM_BOT_TOKEN=тут_токен_бота
WEATHER_API_KEY=тут_api_key

Запуск

python bot_weather.py
Команди
/start – привітання та інструкція

/help – коротка допомога

/weather <місто> - Введіть назву міста, щоб отримати погоду

Приклад відповіді

Погода в Київ:
Температура: 23°C
Опис: Хмарно
Вологість: 65%
Вітер: 4 м/с
