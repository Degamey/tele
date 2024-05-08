import telebot
from g4f import ChatCompletion

TOKEN = '6722111669:AAFCiQdorbyweyKUIlswYpWgW0O3WrcCDvA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    question = message.text
    response = ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"],
        messages=[{"role": "system", "content": ("Ты должен помогать пользователям и отвечать на все вопросы", "Твоё имя - Артем, ты искусственный интелект от Дмитрий Нелова", "Ты должен помогать пользователям")}, {"role": "user", "content": question}]
    )

    bot.reply_to(message, response)

bot.polling()
#by DN 8/05/2024
# @LogKmr