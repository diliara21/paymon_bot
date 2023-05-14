import telebot
from telebot import types
import setting

bot = telebot.TeleBot(setting.API_KEY)


@bot.message_handler(commands=["start"])
def welcome(message):
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_wel = types.KeyboardButton('Давай')
    markup_inline.add(item_wel)
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}! Давай расскажу о своих возможностях'.format(message.from_user), reply_markup=markup_inline)


@bot.message_handler(content_types=['text'])
def men(message):
    if message.text == 'Давай':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Карта')
        item2 = types.KeyboardButton('Персонажи')
        item3 = types.KeyboardButton('Паймон')
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id, 'Я карманный помощник по игре Genshin Impact; могу подсказать, как прокачать персонажей и что можно найти на карте Тейвата. А так же можно поболтать со мной.', reply_markup=markup)

    if message.text == 'Карта':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Анемокулы')
        item2 = types.KeyboardButton('Геокулы')
        item3 = types.KeyboardButton('Электрокулы')
        item4 = types.KeyboardButton('Багровые агаты')
        item5 = types.KeyboardButton('Усыпальницы')
        back = types.KeyboardButton('Меню')
        markup.add(item1, item2, item3, item4, item5, back)
        bot.send_message(message.chat.id, 'Что именно ищете?', reply_markup=markup)
    if message.text == 'Анемокулы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/jhExtVqWsuo.jpg', 'rb'), reply_markup=markup)
    if message.text == 'Геокулы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/Pmp8BEIXG4Q.jpg', 'rb'), reply_markup=markup)
    if message.text == 'Электрокулы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/hjqCU7yAH-k.jpg', 'rb'), reply_markup=markup)
    if message.text == 'Багровые агаты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/ccLceF3ZIac.jpg', 'rb'), reply_markup=markup)
    if message.text == 'Усыпальницы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/усып2.png', 'rb'), reply_markup=markup)
        bot.send_photo(message.chat.id, photo=open('inf/усып1.png', 'rb'), reply_markup=markup)

    elif message.text == 'Персонажи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Барбара')
        item2 = types.KeyboardButton('Беннет')
        item3 = types.KeyboardButton('Бэйдоу')
        item4 = types.KeyboardButton('Джинн')
        item5 = types.KeyboardButton('Дилюк')
        item6 = types.KeyboardButton('Кэйа')
        back = types.KeyboardButton('Меню')
        markup.add(item1, item2, item3, item4, item5, item6, back)
        bot.send_message(message.chat.id, 'Кого ищете?', reply_markup=markup)
    if message.text == 'Барбара':
        bot.send_photo(message.chat.id, photo=open('inf/KhrpOUHLvgw.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton('🎤Оружие')
        it2 = types.KeyboardButton('🎤Артефакты')
        it3 = types.KeyboardButton('🎤Уровни')
        back = types.KeyboardButton('Меню')
        markup.add(it1, it2, it3, back)
        bot.send_message(message.chat.id, 'Что именно хотите прокачать?', reply_markup=markup)
    if message.text == 'Беннет':
        bot.send_photo(message.chat.id, photo=open('inf/0ReyQLxRaq4.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton('👍Оружие')
        it2 = types.KeyboardButton('👍Артефакты')
        it3 = types.KeyboardButton('👍Уровни')
        back = types.KeyboardButton('Меню')
        markup.add(it1, it2, it3, back)
        bot.send_message(message.chat.id, 'Что именно хотите прокачать?', reply_markup=markup)
    if message.text == 'Бэйдоу':
        bot.send_photo(message.chat.id, photo=open('inf/6ulqe7EvoXM.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton('⚓Оружие')
        it2 = types.KeyboardButton('⚓Артефакты')
        it3 = types.KeyboardButton('⚓Уровни')
        back = types.KeyboardButton('Меню')
        markup.add(it1, it2, it3, back)
        bot.send_message(message.chat.id, 'Что именно хотите прокачать?', reply_markup=markup)
    if message.text == 'Дилюк':
        bot.send_photo(message.chat.id, photo=open('inf/e2SxUZ_Kz4M.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton('🍷Оружие')
        it2 = types.KeyboardButton('🍷Артефакты')
        it3 = types.KeyboardButton('🍷Уровни')
        back = types.KeyboardButton('Меню')
        markup.add(it1, it2, it3, back)
        bot.send_message(message.chat.id, 'Что именно хотите прокачать?', reply_markup=markup)
    if message.text == 'Кэйа':
        bot.send_photo(message.chat.id, photo=open('inf/iEa-RtVLnvw.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton('🦚Оружие')
        it2 = types.KeyboardButton('🦚Артефакты')
        it3 = types.KeyboardButton('🦚Уровни')
        back = types.KeyboardButton('Меню')
        markup.add(it1, it2, it3, back)
        bot.send_message(message.chat.id, 'Что именно хотите прокачать?', reply_markup=markup)
    if message.text == 'Джинн':
        bot.send_photo(message.chat.id, photo=open('inf/mrj1n3VIfgA.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        it1 = types.KeyboardButton('🌼Оружие')
        it2 = types.KeyboardButton('🌼Артефакты')
        it3 = types.KeyboardButton('🌼Уровни')
        back = types.KeyboardButton('Меню')
        markup.add(it1, it2, it3, back)
        bot.send_message(message.chat.id, 'Что именно хотите прокачать?', reply_markup=markup)

    if message.text == '🎤Оружие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/42x53CxvLxI.jpg', 'rb'), reply_markup=markup)
    if message.text == '🎤Артефакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/6SaVnayfDAI.jpg', 'rb'), reply_markup=markup)
    if message.text == '🎤Уровни':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/Y-2uW9r4O4Y.jpg', 'rb'), reply_markup=markup)
    if message.text == '👍Оружие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/wZxhBBimRB8.jpg', 'rb'), reply_markup=markup)
    if message.text == '👍Артефакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/cFDdNeS1AmY.jpg', 'rb'), reply_markup=markup)
    if message.text == '👍Уровни':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/_TA5fy5aTJY.jpg', 'rb'), reply_markup=markup)
    if message.text == '⚓Оружие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/1BQR0nRXSfI.jpg', 'rb'), reply_markup=markup)
    if message.text == '⚓Артефакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/AQlkvWdoLFM.jpg', 'rb'), reply_markup=markup)
    if message.text == '⚓Уровни':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/P0l54W7uCa4.jpg', 'rb'), reply_markup=markup)
    if message.text == '🍷Оружие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/HKzQXdSr4X8.jpg', 'rb'), reply_markup=markup)
    if message.text == '🍷Артефакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/yFbbox9T8zM.jpg', 'rb'), reply_markup=markup)
    if message.text == '🍷Уровни':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/3_9JeIg_0rU.jpg', 'rb'), reply_markup=markup)
    if message.text == '🦚Оружие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/xttStIuAQBM.jpg', 'rb'), reply_markup=markup)
    if message.text == '🦚Артефакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/v4AQ4c-ngRg.jpg', 'rb'), reply_markup=markup)
    if message.text == '🦚Уровни':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/mAIa8pXoUvA.jpg', 'rb'), reply_markup=markup)
    if message.text == '🌼Оружие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/zDSetfVKaBw.jpg', 'rb'), reply_markup=markup)
    if message.text == '🌼Артефакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/iUEAhT7oJi4.jpg', 'rb'), reply_markup=markup)
    if message.text == '🌼Уровни':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        markup.add(back)
        bot.send_photo(message.chat.id, photo=open('inf/u-cl2D4GDDE.jpg', 'rb'), reply_markup=markup)

    elif message.text == 'Паймон':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Меню')
        bot.send_message(message.chat.id, 'ехе??те нандайо', reply_markup=markup)

    elif message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Карта')
        item2 = types.KeyboardButton('Персонажи')
        item3 = types.KeyboardButton('Паймон')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)
    if message.text == 'кайф':
        bot.send_message(message.chat.id, 'Кайф ты поймала, тебе всегда мало. Ты не представляешь, как мне тебя не хватало. Сильно бьётся сердце, сама не ожидала. Наконец-то твоя совесть тебя наказала')

bot.polling()