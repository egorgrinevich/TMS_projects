import telebot
from telebot import TeleBot, types
import csv
from datetime import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datasets import load_dataset
subjqa = load_dataset("subjqa", name="electronics")
import pandas as pd

dfs = {split: dset.to_pandas() for split, dset in subjqa.flatten().items()}

for split, df in dfs.items():
    print(f"Number of questions in {split}: {df['id'].nunique()}")
qa_cols = ["title", "question", "answers.text", 
           "answers.answer_start", "context"]
sample_df = dfs["train"][qa_cols].sample(2, random_state=7)
start_idx = sample_df["answers.answer_start"].iloc[0][0]
end_idx = start_idx + len(sample_df["answers.text"].iloc[0][0])
#sample_df["context"].iloc[0][start_idx:end_idx]
counts = {}
question_types = ["What", "How", "Is", "Does", "Do", "Was", "Where", "Why"]

for q in question_types:
    counts[q] = dfs["train"]["question"].str.startswith(q).value_counts()[True]

from transformers import AutoTokenizer

model_ckpt = "deepset/minilm-uncased-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
from datasets import get_dataset_config_names
domains = get_dataset_config_names("subjqa")


import torch
from transformers import AutoModelForQuestionAnswering

model = AutoModelForQuestionAnswering.from_pretrained(model_ckpt)


token = '6202417152:AAGOP0-Czt7huFKujx082YNOqu7NzMTFflU'
bot = telebot.TeleBot(token)
flag: bool = False
@bot.message_handler(commands=['start'])
def start(message):
    #bot.reply_to(message, message.from_user.first_name)
    first_name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton("Ok, I understand", callback_data="understand")
    but2 = types.InlineKeyboardButton("I wanna quit", callback_data="quit")
    markup.add(but1, but2)
    bot.send_message(message.chat.id, text=f"👋 Hello,  {first_name} !\nWellcome to GPT-2 question  chat by Egor\n"
                                           f"This chat was created for demostration the power of NLP\n", reply_markup=markup)
question: str = ""
context: str = ""
status: str = ""

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        if call.data == 'understand':
            global problem
            global status
            global model
            status = ''
            bot.send_message(chat_id=call.message.chat.id, text=f"Please, enter a question:")#, reply_markup=markup)
        elif call.data == 'ans_1':
            # markup = types.InlineKeyboardMarkup() #resize_keyboard=True)  # создание новых кнопок
            # btn1 = types.InlineKeyboardButton("elearning.bseu.by", callback_data="ans_7")
            # btn2 = types.InlineKeyboardButton("i.bseu.by", callback_data="ans_8")
            # markup.add(btn1)
            # markup.add(btn2)
            
              
            # question = "For what purposes can I use HDMI?"
            # context = """High-Definition Multimedia Interface (HDMI) is a proprietary audio/video \
            #     interface for transmitting uncompressed video data and compressed or uncompressed \
            #     digital audio data from an HDMI-compliant source device, such as a display controller, \
            #     to a compatible computer monitor, video projector, digital television, or digital audio \
            #     device. HDMI is a digital replacement for analog video standards. """
            inputs = tokenizer(question, context, return_tensors="pt")  
            input_df = pd.DataFrame.from_dict(tokenizer(question, context), orient="index")
            

            with torch.no_grad():
                outputs = model(**inputs)
            start_logits = outputs.start_logits
            end_logits = outputs.end_logits
            import numpy as np
            import matplotlib.pyplot as plt

            s_scores = start_logits.detach().numpy().flatten()
            e_scores = end_logits.detach().numpy().flatten()
            tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
            token_ids = range(len(tokens))
            
            start_idx = torch.argmax(start_logits)  
            end_idx = torch.argmax(end_logits) + 1  
            answer_span = inputs["input_ids"][0][start_idx:end_idx]
            answer = tokenizer.decode(answer_span)
            # print(f"Question: {question}")
            # print(f"Answer: {answer}")

            bot.send_message(chat_id=call.message.chat.id, text=f"My answer:\n"
                                                                f'{answer}')#, reply_markup=markup)
        elif call.data == 'ans_7':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Да, всё верно", callback_data="ans_9")
            btn2 = types.InlineKeyboardButton("Нет, у меня ошибка...", callback_data="ans_9")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(chat_id=call.message.chat.id, text=f"Логин и пароль написаны строчными (маленькими) латинскими символами?",
                             reply_markup=markup)
        elif call.data == 'ans_9':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Да, спасибо", callback_data="ans_10")
            btn2 = types.InlineKeyboardButton("Нет, я хочу написать администратору", callback_data="ans_11")
            markup.add(btn1)
            markup.add(btn2)
            bot.send_message(chat_id=call.message.chat.id, text=f"Вы решили свою проблему?",
                             reply_markup=markup)
        elif call.data == 'ans_10':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Начать заново", callback_data="student")
            markup.add(btn1)
            bot.send_message(chat_id=call.message.chat.id, text=f"Всего доброго!",
                             reply_markup=markup)
        elif call.data == 'ans_11':
            markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            btn1 = types.InlineKeyboardButton("Нет, я еще подумаю", callback_data="student")
            global flag
            flag = True
            markup.add(btn1)
            bot.send_message(chat_id=call.message.chat.id, text=f"Пожалуйста, сообщите Ваши фамилию, имя отчество, а так же шифр группы и введите свой вопрос.",
                             reply_markup=markup)
        elif call.data == 'ans_12':
            # data_csv = [status, str(datetime.now()), problem]
            # with open('admin_message.csv', 'w', newline='') as csvfile:
            #     spamwriter = csv.writer(csvfile, delimiter=' ',
            #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #     spamwriter.writerow(data_csv)
            # markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
            # btn1 = types.InlineKeyboardButton("В начало", callback_data="student")
            # markup.add(btn1)
            # bot.send_message(chat_id=call.message.chat.id,
            #                  text=f"Всего доброго!\nАдминистратор в ближайшее время свяжется с Вами!!!",
            #                  reply_markup=markup)
            bot.send_message(chat_id=call.message.chat.id, text=f"Please, enter a context:")#, reply_markup=markup)
            status = 'que'


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global status
    global flag
    global question
    global context
    if message.text != '' and status == '':
        question = message.text
        status = 'que'
        markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
        btn1 = types.InlineKeyboardButton("Yes? it is correct", callback_data="ans_12")
        btn2 = types.InlineKeyboardButton("No, I wanna enter another text", callback_data="understand")
        markup.add(btn1, btn2)
        flag = False
        bot.send_message(chat_id=message.chat.id,
                         text=f"Is this correct?\n{question}", reply_markup=markup)
    elif message.text != '' and status == 'que':
        context = message.text
        markup = types.InlineKeyboardMarkup()  # resize_keyboard=True)  # создание новых кнопок
        btn1 = types.InlineKeyboardButton("Yes? it is correct", callback_data="ans_1")
        btn2 = types.InlineKeyboardButton("No, I wanna enter another context", callback_data="ans_12")
        markup.add(btn1, btn2)
        #flag = False
        status = 'con'
        bot.send_message(chat_id=message.chat.id,
                         text=f"Is this correct?\n{context}", reply_markup=markup)
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=f"Выберите один из предложенных вариантов", reply_markup=markup)


bot.polling(none_stop=True, interval=0)