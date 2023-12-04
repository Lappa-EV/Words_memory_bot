import requests
from bs4 import BeautifulSoup as be
import random
from random import choice
import telebot
from telebot import types
import time


def autorization():
    f = open('E:/python/Лекции Python/telegrambot/db.txt', 'r')
    log = input('Введите логин:  ')
    pas = input('Введите пароль:  ')

    if log and pas in f.read():
        print('логин и пароль верные')
        f.close()
        return True

    else:
        print('Вы ввели не верные данные! Зарегистрируйте новый логин и пароль и запустите бот заново заново.')
        f.close()
        return False

def registration():
    '''открываем файл на запись, добавляем данные в конец файла, не удаляя существующие. Если файл не существует, он будет создан.'''
    with open ('E:/python/Pyth_learn_Katya/Pyth_learn_Katya/db.txt', 'a') as file:
        log = input('Придумайте новый логин:  ')
        pas = input('Придумайте новый пароль:  ')
        file.write(log + '\n')
        file.write(pas + '\n')


flag = True
main_array = []
array_words = []
URL = 'https://klavogonki.ru/vocs/559/'
def play_game():
    def parser(URL):
        r = requests.get(URL)
        # print(r.status_code)# проверка соединения с сайтом
        soup = be(r.text, 'html.parser')
        # код для определения тегов перед словами для их выборки:
        token = soup.find_all('td', class_='text')
        clear_token = [c.text for c in token]
        return [c.text for c in token]

    random.shuffle(parser(URL)) # код для случайного выбора слов с сайта

    bot = telebot.TeleBot('5973571826:AAHxi_wgxOKwfLGhzH3ZuTRZ3RG6iLozaFo')
    @bot.message_handler(content_types=['text'])
    def hello(message):
        count = 0

        global flag
        global array_words
        global main_array

        time_string = ''
        if (flag):
            # Кнопки да и нет
            keyboard = types.InlineKeyboardMarkup()
            # Добавляем кнопки на экран
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
            key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(key_yes, key_no)
            bot.send_message(message.chat.id,
                             text='Привет! Это телеграм бот для тренировки памяти.\nПравила: Бот выводит на экран несколько слов, после чего слова скрываются. \nВ момент вывода слов необходимо запомнть их и написать в любом порядке. Начнем?',
                             reply_markup=keyboard)
            flag = False
        else:
            array_text = message.text

            for i in range(len(array_text)):
                if (array_text[i] != ','):
                    time_string += array_text[i]
                else:
                    if (time_string in main_array):
                        count += 1
                        array_words.append(time_string)
                        time_string = ''
                    else:
                        time_string = ''

            if (time_string in main_array):
                count += 1
                array_words.append(time_string)
                time_string = ''

            bot.send_message(message.chat.id, text=f'Вы правильно написали {count} слов(а). Верные слова: {array_words}')
            array_words = []
            flag = True
            bot.send_message(message.chat.id, text=f'Напишите любое слово, чтобы продолжить...')


    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        # Если нажали на кнопку 'да', то выводим список слов
        if call.data == 'yes':
            a = choice(parser(URL))
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            flag_b = False
            flag_c = False
            flag_d = False
            flag_e = False
            flag_f = False
            flag_g = False
            flag_h = False

            while (True):
                tmp = choice(parser(URL))
                if ((a != tmp) and (flag_b == False)):
                    flag_b = True
                    b = tmp
                elif ((a != tmp) and (b != tmp) and (flag_c == False)):
                    flag_c = True
                    c = tmp
                elif ((a != tmp) and (b != tmp) and (c != tmp) and (flag_d == False)):
                    flag_d = True
                    d = tmp
                elif ((a != tmp) and (b != tmp) and (c != tmp) and (d != tmp) and (flag_e == False)):
                    flag_e = True
                    e = tmp
                elif ((a != tmp) and (b != tmp) and (c != tmp) and (d != tmp) and (e != tmp) and (flag_f == False)):
                    flag_f = True
                    f = tmp
                elif ((a != tmp) and (b != tmp) and (c != tmp) and (d != tmp) and (e != tmp) and (f != tmp) and (
                        flag_g == False)):
                    flag_g = True
                    g = tmp
                elif ((a != tmp) and (b != tmp) and (c != tmp) and (d != tmp) and (e != tmp) and (f != tmp) and (
                        g != tmp) and (flag_h == False)):
                    flag_h = True
                    h = tmp
                    break
            main_array.append(a)
            main_array.append(b)
            main_array.append(c)
            main_array.append(d)
            main_array.append(e)
            main_array.append(f)
            main_array.append(g)
            main_array.append(h)
            msg = f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}'
            # Код для вывода списка слов на экран:
            test = bot.send_message(call.message.chat.id, msg)
            time.sleep(10) # Код с таймингом 10 секунд
            # Код для удаления списка слов с экрана:
            bot.delete_message(test.chat.id, test.id)
            # Отправляем информацию с правилами ввода слов в Телеграм:
            bot.send_message(call.message.chat.id,
                             'Введите слова,которые запомнили. Вводите БЕЗ ПРОБЕЛОВ,слова разделяйте ЗАПЯТОЙ!')
        # Если нажали на кнопку 'нет', то выводится сообщение 'Пока!':
        elif call.data == 'no':
            bot.send_message(call.message.chat.id, 'Пока!')

    @bot.message_handler(content_types=['text'])
    def delete_message(message):
        message_1 = bot.send_message(message.chat.id, message.id)
        bot.delete_message(message.chat.id, message_1.id)
    bot.polling(none_stop=True, interval=0) # Запускаем бот на исполнение:


if (autorization()):
    play_game()

else:
    registration()
    play_game()
