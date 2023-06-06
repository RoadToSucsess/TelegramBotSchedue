import openpyxl
import telebot
from telebot import types

bot = telebot.TeleBot('5491305347:AAF9vS2Ij7poZvizw2AJJisMITIVFM8NFRo')

book = openpyxl.open("Data.xlsx", read_only=True)
book_open = openpyxl.open("Data.xlsx")
sheet = book.active
sheets = book_open.active


# Даня - комитит
def get_all_bd():  # Вызов всей базы
    book
    # strok = []
    tim = []

    for row in sheet.iter_rows(min_row=2, max_row=25, min_col=1, max_col=3):
        for cell in row:
            print(cell.value, end=" ")
        print()

    # tim = sheet["A2":"C13"]

    # for i in range(2, 72 + 2):
    # for j in range(3):
    # if sheet[i][j].value == None:
    # continue
    # else:
    # strok.append(sheet[i][j].value)
    # tim.append([strok])
    # tim.append(sheet[i][1].value)

    book_open.close()
    return tim


print(get_all_bd())


# --------------------------------------------------------------------------------------------------------------------------------------------------
def get_bd1(val):  # Вызов базы данных для любого дня недели
    book
    tim = []
    for i in range(val + 1, val + 8 + 4):
        tim.append(sheet[i][0].value)

    book_open.close()
    return tim


# --------------------------------------------------------------------------------------------------------------------------------------------------

def mess_take(val, message):  # Создание кнопок с временем
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=6)
    timetable = types.KeyboardButton('Расписание')
    markup.add(timetable)

    for i in range(len(get_bd1(val))):
        get_bd1(val)[i] = types.KeyboardButton(get_bd1(val)[i])

    markup.add(*get_bd1(val))
    bot.send_message(message.chat.id, f"<b>{get_all_bd()[val - 2]}:</b>", reply_markup=markup, parse_mode='html')
    bot.send_message(message.chat.id, '\n'.join(get_bd1(val)), reply_markup=markup, parse_mode='html')


def save_data(val, message):
    for i in range(len(get_bd1(val))):
        if message.text == get_bd1(val)[i]:
            book_open
            sheet
            if sheet[i + val][3].value != None:
                sheet[i + val][3].value = message.from_user.first_name

                book_open.save("Data.xlsx")
                book_open.close()
                bot.send_message(message.chat.id, "Жоска! ты записался!")


# --------------------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])  # /start с кнопками 
def start(message):
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>', parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    monday = types.KeyboardButton('Понедельник')
    tuesday = types.KeyboardButton('Вторник')
    wednesday = types.KeyboardButton('Среда')
    thursday = types.KeyboardButton('Четверг')
    friday = types.KeyboardButton('Пятница')
    saturday = types.KeyboardButton('Суббота')
    timetable = types.KeyboardButton('Расписание')
    markup.add(monday, tuesday, wednesday, thursday, friday, saturday, timetable)
    bot.send_message(message.chat.id, "Выберете из списка на какой день вы бы хотели записаться?", reply_markup=markup)


# --------------------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['setup'])  # /setup с кнопками (секретная менюшка по id)
def setup(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    monday = types.KeyboardButton('Понедельник[Р]')
    tuesday = types.KeyboardButton('Вторник[Р]')
    wednesday = types.KeyboardButton('Среда[Р]')
    thursday = types.KeyboardButton('Четверг[Р]')
    friday = types.KeyboardButton('Пятница[Р]')
    saturday = types.KeyboardButton('Суббота[Р]')
    timetable = types.KeyboardButton('Расписание[Р]')
    exit = types.KeyboardButton('Выйти из отладчика')

    if message.chat.id == 870779877 or message.chat.id == 1160704466:
        markup.add(monday, tuesday, wednesday, thursday, friday, saturday, timetable, exit)
        bot.send_message(message.chat.id, f"Это режим настройки рассписания 😉", parse_mode='HTML')
        bot.send_message(message.chat.id,
                         "Валерия, выбери день, а потом время в которые ты бы хотела проводить занятия, остальные дни для пользовотелей доступны не будут! 😌",
                         reply_markup=markup)
    else:
        get_all_bd()


@bot.message_handler()
def get_time(message):
    if message.text == "Понедельник":  # 2
        val = 2
        book_open
        sheets["D2"] = val
        book_open.save("Data.xlsx")
        book_open.close()
        mess_take(val, message)
        bot.send_message(message.chat.id, parse_mode='HTML')
    elif message.text == "Вторник":  # 14
        val = 14
        book_open
        sheets["D2"] = val
        book_open.save("Data.xlsx")
        book_open.close()
        mess_take(val, message)
    elif message.text == "Среда":  # 26
        val = 26
        book_open
        sheets["D2"] = val
        book_open.save("Data.xlsx")
        book_open.close()
        mess_take(val, message)
    elif message.text == "Четверг":  # 38
        val = 38
        book_open
        sheets["D2"] = val
        book_open.save("Data.xlsx")
        book_open.close()
        mess_take(val, message)
    elif message.text == "Пятница":  # 50
        val = 50
        book_open
        sheets["D2"] = val
        book_open.save("Data.xlsx")
        book_open.close()
        mess_take(val, message)
    elif message.text == "Суббота":  # 62
        val = 62
        book_open
        sheets["D2"] = val
        book_open.save("Data.xlsx")
        book_open.close()
        mess_take(val, message)
        # --------------------------------------------------------------------------------------------------------------------------------------------------

    elif message.text == "Расписание" or message.text == "Выйти из отладчика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        monday = types.KeyboardButton('Понедельник')
        tuesday = types.KeyboardButton('Вторник')
        wednesday = types.KeyboardButton('Среда')
        thursday = types.KeyboardButton('Четверг')
        friday = types.KeyboardButton('Пятница')
        saturday = types.KeyboardButton('Суббота')
        timetable = types.KeyboardButton('Расписание')
        markup.add(monday, tuesday, wednesday, thursday, friday, saturday, timetable)
        bot.send_message(message.chat.id, "Выберете удобное для вас день из списка:", reply_markup=markup)
        bot.send_message(message.chat.id, '\n'.join(get_all_bd()), reply_markup=markup)

    elif message.text == [get_bd1(int(sheets["D2"]))[i] for i in range(len(get_bd1(int(sheets["D2"]))))]:  # Разобраться
        # take = sheets["D2"]
        bot.send_message(message.chat.id, "Маленькая победа!", reply_markup=markup)
        save_data(take, message)
        # book_open

        # sheets["C3"] = message.from_user.first_name

        # book_open.save("Data.xlsx")
        # book_open.close()
        # bot.send_message(message.chat.id, f"Вы записались на {message.text}:")

    # elif message.text == "13:00":
    # save_data(val, message)
    # [get_bd1(2)[i] for i in range(len(get_bd1(2)))]

    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
    elif message.text == "Привет" or "привет" or "здарова" or "превет" or "Привед" or "Превед" or "здорова" or "Здарова" or "Здорова" or "здравствуйте" or "Здравствуйте" or "hi" or "Hi" or "hello" or "Hello":
        bot.send_message(message.chat.id,
                         f"И тебе привет, <b>{message.from_user.first_name}</b>, предлагаю записаться на урок! Проверь актуальное расписание! ;)",
                         parse_mode='html')


bot.polling(none_stop=True)
