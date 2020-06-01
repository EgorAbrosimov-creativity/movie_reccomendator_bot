import telebot
from telebot import types
import random
import omdb_parse, tmdb_reccomendator

bot = telebot.TeleBot('1200425822:AAFE_ACXYmtXXvB-m4lK-xu8p_yBUc9t3QE')


class ListOfMoviesToShow:
    id_list_main = []
    current_element = 0
    latest_message = None

    def set_latest_message(self, mes):
        self.latest_message = mes

    def __init__(self):                     # Инициализация
        self.id_list_main = []
        self.current_element = 0
        self.latest_message = None

    def set_list(self, id_list):            # Сеттер
        self.id_list_main = id_list
        self.current_element = 0

    def set_to_next_elem(self, message):             # Следующий элемент
        if self.current_element + 1 >= len(self.id_list_main):
            self.current_element = 0
        else:
            self.current_element += 1
        self.send_info_1(message, 'existing')

    def set_to_prev_elem(self, message):             # Предыдущий элемент
        if self.current_element -1 < 0:
            self.current_element = len(self.id_list_main) - 1
        else:
            self.current_element += 1
        self.send_info_1(message, 'existing')

    def if_list_empty(self):
        if len(self.id_list_main) == 0:
            return True
        else:
            return False

    def get_element_text_1(self):                   # Текст описания
        return omdb_parse.construct_movie_description(self.id_list_main[self.current_element])

    def get_element_text_2(self):                   # Последующая инфа
        return omdb_parse.construct_following_info(self.id_list_main[self.current_element])

    def get_menu_1(self):
        keyboard_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        key_1 = types.KeyboardButton('⬅️')
        key_2 = types.KeyboardButton('➡️')
        key_3 = types.KeyboardButton('Further info')
        keyboard_1.add(key_1, key_2, key_3)
        return keyboard_1

    def get_menu_2(self):
        keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        key_1 = types.KeyboardButton('Back to main info')
        keyboard_2.add(key_1)
        return keyboard_2

    def send_info_1(self, message, type):               # types = ['new', 'existing']
        if self.if_list_empty():
            self.latest_message = bot.send_message(message.chat.id, 'The list of results is empty, try to start search')
        else:
            text = 'Result %i / %i \n' % (self.current_element + 1, len(self.id_list_main))\
                       + self.get_element_text_1()
            self.latest_message = bot.send_message(message.chat.id, text, reply_markup=self.get_menu_1())

    def send_info_2(self, message):
        if self.if_list_empty():
            self.latest_message = bot.send_message(message.chat.id, 'The list of results is empty, try to start search')
        else:
            text = 'Result %i / %i \n' % (self.current_element + 1, len(self.id_list_main)) +\
                   self.get_element_text_2()
            self.latest_message = bot.send_message(message.chat.id, text, reply_markup=self.get_menu_2())

    def start_to_show(self, message):
        self.send_info_1(message, 'new')
        self.current_element=0


my_list = ListOfMoviesToShow()


@bot.message_handler(commands=['start'])
def start_message(message):
    my_list.latest_message = bot.send_message(message.chat.id,
                     'oh hi Harry, wanna watch some movies, huh? \n'
                     'Send me one of those:\n'
                     ' /movie_title + <movie title>\n'
                     ' or /movie_title_year + <movie title, movie year>',
                     )
    print(message)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == '⬅️':
        my_list.set_to_prev_elem(message)
    if message.text == '➡️':
        my_list.set_to_next_elem(message)
    if message.text == 'Further info':
        my_list.send_info_2(message)
    if message.text == 'Back to main info':
        my_list.send_info_1(message, 'existing')

    if '/movie_title' in message.text:
        query = message.text[13:]
        id_list = omdb_parse.title_search(query)
        my_list.set_list(id_list)
        my_list.start_to_show(message)

    if '/movie_title_year' in message.text:
        query = message.text[17:]
        id_list = omdb_parse.title_year_search(query, query)
        my_list.set_list(id_list)
        my_list.start_to_show(message)

    if 'popular_now' in message.text:
        id_list_popular = tmdb_reccomendator.popular_list()
        #print(id_list_popular)
        my_list.set_list(id_list_popular)
        my_list.start_to_show(message)
"""
    if '/movie_for_family' in message.text:
        id_list = tmdb_reccomendator.top_family_list()
        print(id_list)
        my_list.set_list(id_list[:20])
        my_list.start_to_show(message)

    if '/movie_comedy' in message.text:
        id_list = tmdb_reccomendator.top_comedies_list()
        #print(id_list)
        my_list.set_list(id_list[:20])
        my_list.start_to_show(message)

    if '/movie_romance' in message.text:
        id_list = tmdb_reccomendator.top_romantic_list()
        #print(id_list)
        my_list.set_list(id_list[:20])
        my_list.start_to_show(message)

    if '/movie_horror' in message.text:
        id_list = tmdb_reccomendator.top_horror_list()
        #print(id_list)
        my_list.set_list(id_list[:20])
        my_list.start_to_show(message)

    if '/movie_documentary' in message.text:
        id_list = tmdb_reccomendator.top_documentaries_list()
        #print(id_list)
        my_list.set_list(id_list[:20])
        my_list.start_to_show(message)

    if '/movie_scifi' in message.text:
        id_list = tmdb_reccomendator.top_scifi_list()
        #print(id_list)
        my_list.set_list(id_list[:20])
        my_list.start_to_show(message)

    if '/movie_war' in message.text:
        id_list = tmdb_reccomendator.top_war_list()
        #print(id_list)
        my_list.set_list(id_list[:20])
        my_list.start_to_show(message)
"""

@bot.message_handler(commands=['movie_title'])
def movie_title_search(message):
    query = message.text[13:]
    id_list = omdb_parse.title_search(query)
    my_list.set_list(id_list)
    my_list.start_to_show(message)


@bot.message_handler(commands=['movie_title_year'])
def movie_title_year_search(message):
    query = message.text[17:]

    a = query.str.split(separator=[',', ' '])

    if len(a) < 2:
        bot.send_message(message.chat.id, 'Incorrect input text, please try again')
    else:
        year = a[-1]
        title = a[:-1]
        id_list = omdb_parse.title_year_search(title, year)
        my_list.set_list(id_list)
        my_list.start_to_show(message)


def listener(messages):
    for m in messages:
        print(str(m), '\n'*5)


bot.set_update_listener(listener)
bot.polling()

# БУМАЖКА С ОПИСАНИЕМ АРХИТЕКТУРЫ
# ВСЕ_ЕЩЕ НАДО СДЕЛАТЬ ОТОБРАЖЕНИЕ ОПИСАНИЯ, КНОПКИ ДЛЯ ВЫБОРА
# ПЛЮС СДЕЛАТЬ ЕЩЕ ФИШЕЧКИ text="тру-ту-ту", reply_markup=key )