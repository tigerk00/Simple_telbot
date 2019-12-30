#Импортируем нобходимые библиотеки
import telebot 
import constants
import os
import random
import requests

# Тут нужно написать свой токен для роботы с ботом , который можно взять у Bot Father'a
bot = telebot.TeleBot('YOUR_TOKEN')      


@bot.message_handler(commands=['start'])    #Действия , которые будет выполнять бот при команде /start 
def handle_start(message):
    #
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)   #Клавиатура телеграмм-бота 
    user_markup.row('аниме-арты про любовь :3', 'эпические арты', 'Если есть за кем грустить')
    user_markup.row("скинь аниме-гифку", 'аниме-мемы', "гули , вампиры и прочие причуды" , 'релакс-арты')
    bot.send_message(message.from_user.id, "Приветсвую...", reply_markup=user_markup)




# Ответ бота при определенных запросах пользователя
@bot.message_handler(content_types=['text', 'document'])
def handle_text_document(message):
    if message.text == "аниме-арты про любовь :3":
        
        all_files_in_directory = os.listdir(r"full_path_to_folder_with_your_files")       # Тут он выбирает случайный файл из директории, пишет его название в консоль ,
        random_file = random.choice(all_files_in_directory)            # для вашего удобства и отправляет его пользователю 
        print(all_files_in_directory)
        img = open(r"D:\never feel it" + "/" + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        print(img, 'Фото')
        print(random_file, 'Случайный файл')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == "эпические арты":                           # Тоже самое , что и в предущем примере
        
        all_files_in_directory = os.listdir(r"full_path_to_folder_with_your_files")
        random_file = random.choice(all_files_in_directory)
        print(all_files_in_directory)
        img = open(r"D:\epic arts" + "/" + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        print(img, 'Фото')
        print(random_file, 'Случайный файл')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'Если есть за кем грустить':               # Повторяет предущие действия , только теперь задействует аудио,которое пользователь
        
        directory = r"full_path_to_folder_with_your_files"            # может скачать или просто послушать
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        song =  open(directory + "/" + random_file, "rb")
        bot.send_chat_action(message.from_user.id, "upload_audio")
        bot.send_audio(message.from_user.id , song)
        song.close()
    elif message.text == "скинь аниме-гифку":                       # Повторяет предущие действия , только теперь задействует gif файлы  
        
        directory = r"full_path_to_folder_with_your_files"
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        giff = open(directory + "/" + random_file, "rb")
        bot.send_chat_action(message.from_user.id, "upload_video")
        bot.send_video(message.from_user.id, giff)
        giff.close()
    elif message.text == "аниме-мемы":
        
        all_files_in_directory = os.listdir(r"full_path_to_folder_with_your_files") 
        random_file = random.choice(all_files_in_directory)
        print(all_files_in_directory)
        img = open(r"D:\anime memes telegram" + "/" + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        print(img, 'Фото')
        print(random_file, 'Случайный файл')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == "гули , вампиры и прочие причуды":
        
        all_files_in_directory = os.listdir(r"full_path_to_folder_with_your_files")
        random_file = random.choice(all_files_in_directory)
        print(all_files_in_directory)
        img = open(r"D:\for tgbot" + "/" + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        print(img, 'Фото')
        print(random_file, 'Случайный файл')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == "релакс-арты":
        
        all_files_in_directory = os.listdir(r"full_path_to_folder_with_your_files")
        random_file = random.choice(all_files_in_directory)
        print(all_files_in_directory)
        img = open(r"C:\Users\111\pain bot\peaceful arts" + "/" + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        print(img, 'Фото')
        print(random_file, 'Случайный файл')
        bot.send_photo(message.from_user.id, img)
        img.close()





# Для нон-стоп работы бота без пауз
bot.polling(none_stop=True, interval=0)
