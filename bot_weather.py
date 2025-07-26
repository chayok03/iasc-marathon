import telebot
import requests

# === Налаштування токенів ===

from dotenv import load_dotenv
import os

load_dotenv()


TELEGRAM_BOT_TOKEN : str | None = os.getenv("7169216593:AAGs2IEF8JDIM_hD5IiFxya_uYt0DCgMZBg")
WEATHER_API_KEY : str | None = os.getenv("bcb4db6a69767d454faa976a3c974d23")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# === Функція для отримання погоди ===
def fetch_weather(city):
    print(f"[LOG] Запит погоди для міста: {city}")  # логування

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ua"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        try:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            return (f"Погода в {city.capitalize()}:\n"
                    f"🌡 Температура: {temp}°C\n"
                    f"☁ Опис: {desc.capitalize()}\n"
                    f"💧 Вологість: {humidity}%\n"
                    f"💨 Вітер: {wind} м/с")
        except KeyError:
            return "Помилка при обробці даних від сервера."
    elif response.status_code == 404:
        return f"Місто '{city}' не знайдено. Перевірте назву."
    else:
        return "Помилка отримання даних з API."

# === /start ===
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message,
                 "Привіт! Я бот для отримання погоди.\n"
                 "Привіт! Напиши команду /weather <місто>, щоб дізнатися погоду.")

# === /help ===
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message,
                 "Команди:\n"
                 "/start – Привітання\n"
                 "/help – Допомога\n"
                 "/weather <місто> – Погода у вказаному місті\n")

# === /weather ===
@bot.message_handler(commands=['weather'])
def weather_command(message):
    try:
        city = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.reply_to(message, "Будь ласка, вкажи місто. Наприклад: /weather Київ")
        return

    weather_info = fetch_weather(city)
    bot.reply_to(message, weather_info)

# === Відповіді на звичайні повідомлення (місто) ===
@bot.message_handler(func=lambda message: True)
def handle_city(message):
    city = message.text.strip()

bot.infinity_polling()