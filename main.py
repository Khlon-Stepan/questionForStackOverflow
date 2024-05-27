import aioschedule as schedule
import asyncio
import config

from telethon import TelegramClient, events, sync
from datetime import datetime

api_id = config.api_id
api_hash = config.api_hash

client = TelegramClient('test_session', api_id, api_hash)
client.start()

global stageOfWorking
global topic
global info

stageOfWorking = "relaxing"
topic = ""
info = ""

# haval_marks = ["Haval", "H2", "H3", "H5", "H6", "H9", "M6", "F7", "Dargo", "Jolion"]
haval_marks = ["Haval", "H2"]
autos = [haval_marks]


# Подготовка постов
async def preparation_posts():
    print("Подготовка запросов пошла")
    
    for auto in autos:
        for i in range(1, len(auto)):
            await ask_topic(auto[0], auto[i])
            

# Запрос темы для поста
async def ask_topic(nameAuto, model):
    global stageOfWorking
    global topic
    global info
    
    await client.send_message("@chatsgpts_bot", f"Придумай и отправь уникальную тему для {nameAuto} модели {model}")
    stageOfWorking = f"{nameAuto} {model} askTopic"
    

# Запрос информации для поста
async def ask_info(nameAuto, model):
    global stageOfWorking
    global topic
    global info
    
    await client.send_message("@chatsgpts_bot", f"Придумай и отправь уникальную информацию на тему: {topic}")
    stageOfWorking = f"{nameAuto} {model} askInfo"
    

# Отправка готового поста
async def send_post(nameAuto, model):
    global stageOfWorking
    global topic
    global info
    
    if (nameAuto == "Haval"):
        if (model == "H2"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=2)
            
        elif (model == "H3"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=3)
            
        elif (model == "H5"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=4)
            
        elif (model == "H6"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=5)
        
        elif (model == "H9"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=6)
            
        elif (model == "M6"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=7)
            
        elif (model == "F7"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=8)
            
        elif (model == "Dargo"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=9)
            
        elif (model == "Jolion"):
            await client.send_message("@testing_gpt", f"{topic}\n\n{info}", reply_to=10)
            
        stageOfWorking = "relaxing"
        

# Обработчик сообщений от @chatsgpts_bot
@client.on(events.NewMessage(chats=('@chatsgpts_bot')))
async def chatGPT_messages_handler(msg):
    global stageOfWorking
    global topic
    global info
        
    if (msg.message.to_dict()["from_id"]["user_id"] != 951908728 and msg.message.to_dict()["message"] not in ["Обрабатываем ваш вопрос...", "Не удалось выполнить запрос, попробуйте повторить"]):
        stage = stageOfWorking.split()
        if (stage[2] == "askTopic"):
            topic = msg.message.to_dict()["message"][1:-1]
            await ask_info(stage[0], stage[1])
            
        elif (stage[2] == "askinfo"):
            info = msg.message.to_dict()["message"]
            await send_post(stage[0], stage[1])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(preparation_posts)
    client.run_until_disconnected()
    
