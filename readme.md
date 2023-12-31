# Telegram-бот «Words_memory_bot»

Для создания приложения в работе использовался TelegramAPI.

Цель работы - создание telegram-бота, предназначенного для тренировки памяти путем воспроизведения пользователем рандомного набора слов. 

Telegram-бот «Words_memory_bot» является игровым инструментом с функцией тренажера памяти.

Перед использованием telegram-бота необходимо в консоли интерпретатора Python ввести логин и пароль. Если данные введены верно telegram-бот начинает работать, если введенные данные не верны на экран выводится предложение придумать новый логин и пароль. После успешной регистрации telegram-бот «Words_memory_bot» начинает работать.

Telegram-бот выводит на экран несколько слов, после чего слова скрываются. В момент вывода слов необходимо запомнить их и написать после их исчезновения с экрана в любом порядке через запятую, без пробелов.
После ввода слов пользователем telegram-бот выводит на экран угаданные слова и их количество, после чего предлагает продолжить тренировку.


## Описание функций приложения

Telegram-бот обладает следующими функциональными характеристиками:
- бот имеет кнопки для удобной навигации пользователей по функционалу бота (выбор начала или окончания игры);
- отправляет текстовые сообщения (информацию о назначении игры – бота, правила использования игры, результат подсчета количества совпавших слов, текст с предложением и условием продолжения игры, сообщение в случае отказа от начала игры);
- принимает и обрабатывает текст, введенный пользователем;
- обрабатывает команды, введенные пользователями, и выполнять соответствующие действия (нажатие кнопки);
- функция сверки и подсчета количества совпавших слов пользователя со словами, выведенными ранее на экран ботом;
- регистрация и сверка логина и пароля: для запуска telegram-бота перед его использованием администратору необходимо зарегистрироваться, ввести логин и пароль.

## Стадии и этапы разработки 
Для создания бота с использованием TelegramAPI необходимо выполнить следующие шаги:
1. Зарегистрироваться в Telegram и создать новый бот, следуя инструкциям на официальном сайте Telegram.
2. Получить API ключ для бота, который будет использоваться для взаимодействия с TelegramAPI.
3. Выбрать язык программирования, который будет использоваться для написания бота. Для работы с TelegramAPI можно использовать различные языки программирования, такие как Python, Java, C++, JavaScript и др.
4. Установить необходимые библиотеки и фреймворки для выбранного языка программирования.
5. Написать код для бота, который будет обрабатывать запросы от пользователей и отправлять им ответы.
6. Запустить бота на сервере или локальном компьютере, используя специальный скрипт или приложение.
7. Протестировать работу бота и внести необходимые изменения в код, если это необходимо.
8. Опубликовать бота в Telegram и начать его использование.

 
## Реализация приложения 
## Написание программного кода 
Программный код telegram-бота будет реализован по следующей схеме:

блок с кодом установки библиотек

блок с кодом авторизации (`def autorization()`)

блок с кодом регистрации (`def registration()`)

блок с кодом игры-бота (`def play_game()`)

блок с кодом запуска игры с авторизацией

блок с кодом запуска игры с регистрацией


## Блок с кодом установки библиотек
В окне терминала устанавливается библиотека для создания и отправки запросов по протоколу HTTP для дальнейшего парсинга кода страницы со словами:
```python
pip install requests
```
Устанавка библиотеки BeautifulSoup:
```python
pip install beautifulsoup4
```
Импорт библиотеки для создания и отправки запросов по протоколу HTTP:
```python 
import requests
```
Импорт библиотеки для анализа веб-сайтов, построенных на технологиях HTML и CSS:
```python
from bs4 import BeautifulSoup as be
```
Импортируем модуль telebot:
```python
import telebot
```
Импорт типов из модуля telebot, чтобы создавать кнопки:
```python
from telebot import types
```
Импорт модуля random, для организации вывода в случайном порядке слов:
```python
import random
```
Импорт способа choice из модуля random, для вывода в случайном порядке слов из списка:
```python
from random import choice
```
Импорт модуля time для настройки и установления необходимого времени написания пользователем слов:
```python
import time
```
## Блок с кодом авторизации
Функция авторизации администратора для запуска бота:
```python
def autorization():
'''чтение логинов и паролей с файла'''
    f = open('E:/python/Лекции Python/telegrambot/db.txt', 'r') 
	  log = input('Введите логин:  ')
    pas = input('Введите пароль:  ')

    if log and pas in f.read(): # проверка совпадения логина и пароля
        print('логин и пароль верные')
        f.close()
        return True

    else:
        print('Не верные логин или пароль. Хотите зарегистрироваться?')
        f.close()
        return False
```
## Блок с кодом регистрации
Функция регистрации логина и пароля администратора для запуска telegram-бота:
```python
def registration():
    '''открываем файл на запись, добавляем данные в конец файла, не удаляя cуществующие. Если файл не существует, он будет создан.'''

    with open ('E:/python/Pyth_learn_Katya/Pyth_learn_Katya/db.txt', 'a') as file:
        log = input('Придумайте логин:  ')
        pas = input('Придумайте пароль:  ')
        file.write(log + '\n')
        file.write(pas + '\n')
```
## Блок с кодом игры-бота
```python
flag = True
main_array = [] 
array_words = []
URL = 'https://klavogonki.ru/vocs/559/'
def play_game():
```
Создание парсера слов со стороннего сайта:
```python
    def parser(URL):    
        r = requests.get(URL)
        # print(r.status_code)# проверка соединения с сайтом
        soup = be(r.text, 'html.parser')

	    # код для определения тегов перед словами для их выборки:
        token = soup.find_all('td', class_='text') 
        clear_token = [c.text for c in token]
        return [c.text for c in token]

    random.shuffle(parser(URL)) # код для случайного выбора слов с сайта
```
Создание экземпляра бота:
```python
 bot = telebot.TeleBot('5973571826:AAHxi_wgxOKwfLGhzH3ZuTRZ3RG6iLozaFo')
```
Функция для обработки команды «ввод произвольного текста»:
```python
    @bot.message_handler(content_types=['text'])
    def hello(message):
        count = 0
	    # Глобальные переменные:
        global flag
        global array_words
        global main_array 
```
Для создания клавиатуры используется InlineKeyboardMarkup() — это кастомная клавиатура. Она привязывается к сообщению, с которым была отправлена. В кнопки можно заложить любой текст размером от 1 до 64 байт. Инлайн кнопки позволяют скрыть в себе внутреннюю телеграм ссылку, ссылку на внешний ресурс, а также шорткат для инлайн запроса.
```python
keyboard = types.InlineKeyboardMarkup()
```
Далее по очереди готовим текст, и обработчик для каждой программы и добавляем кнопки на экран:
```python
time_string = ''
if (flag):
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') # Добавляем кнопки на экран
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_yes, key_no)
    bot.send_message(message.chat.id, text='Привет! Это телеграм бот для тренировки памяти.\nПравила: Бот выводит на экран несколько слов, после чего слова скрываются. \nВ момент вывода слов необходимо запомнть их и написать в любом порядке. Начнем?', reply_markup=keyboard)
    flag = False
else:
```
Код для обработки списка слов от пользователя и подсчета количества верных и не верных слов:
```python
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
```
Функция, обрабатывающая команду «нажатие на кнопку»:
```python
@bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        # Если нажали на кнопку 'да', то выводим список слов
        if call.data == 'yes':
```
Код для составления списка слов, выбранных со стороннего сайта случайным образом:
```python
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
```
Слова подаются с сайта в виде списка, в произвольном порядке отбираются с помощью choice. Если слово не дублируется оно добавляется в конец составляемого списка 'msg' для последующего вывода на экран. 
```python
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
		elif ((a != tmp) and (b != tmp) and (c != tmp) and (d != tmp) and (e != tmp) and (f != tmp) and (flag_g == False)):
			flag_g = True
			g = tmp
		elif ((a != tmp) and (b != tmp) and (c != tmp) and (d != tmp) and (e != tmp) and (f != tmp) and (g != tmp) and (flag_h == False)):
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
	bot.send_message(call.message.chat.id,'Введите слова,которые запомнили. Вводите БЕЗ ПРОБЕЛОВ,слова разделяйте ЗАПЯТОЙ!')
# Если нажали на кнопку 'нет', то выводится сообщение 'Пока!':
elif call.data == 'no':
	bot.send_message(call.message.chat.id, 'Пока!')
```
Функция для обработки команды «ввод произвольного текста»:
```python
@bot.message_handler(content_types=['text'])
def delete_message(message):
    message_1 = bot.send_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, message_1.id)
```
Запуск бота на исполнение:
```python
bot.polling(none_stop=True, interval=0)
```
Блок с кодом запуска игры с авторизацией:
```python
if (autorization()):
    play_game()
```
Блок с кодом запуска игры с регистрацией:
```python
else:
    registration()
    play_game()
```

## Тестирование приложения 

После нажатия в интерпретаторе кнопки «Run» для запуска бота требуется ввести логин и пароль. 

В случае не существующего логина или пароля предлагается зарегистрироваться и заново запустить программу (рис.1):

![рис. 1.1](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок1.1.png)
![рис. 1.2](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок1.2.png)

Рисунок 1 – Пример ввода и регистрации логина и пароля

После ввода команды /start можно увидеть следующий вид (рис.2):

![рис. 2](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок2.png)

Рисунок 2 – Вид диалога с telegram bot после ввода слова от пользователя

![рис. 3](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок3.png)

Рисунок 3 – Отправка сообщения пользователю после нажатия кнопки «Нет»

![рис. 4](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок4.png)

Рисунок 4 – Отправка сообщения со списком слов пользователю после нажатия кнопки «Да»


Когда на экране появился рандомный список слов у пользователя есть 10 секунд на их запоминание, после чего список слов исчезает и пользователю на экран выводится сообщение с предложением ввести запомнившиеся слова через запятую (рис.5):

![рис. 5](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок5.png)

Рисунок 5 – Вид после исчезновения списка слов с экрана и появившемся сообщении о необходимости ввести запомнившиеся слова.


После ввода слов пользователем telegram bot выводит количество и список угаданных слов, а также сообщение с предложением написать любое слово чтобы продолжить игру (рис.6):

![рис. 6](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок6.png)

Рисунок 6 – Отправка сообщений пользователю с результатами его ответа боту и информации о способе продолжения игры.


После получения ботом от пользователя слова для продолжения игры процесс начинается заново (рис. 7):

![рис. 7](https://github.com/Lappa-EV/Words_memory_bot/blob/master/images/Рисунок7.png)

Рисунок 7 – Вид после ввода слова-подтверждения продолжения игры пользователем.



