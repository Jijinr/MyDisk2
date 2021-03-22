from telethon import TelegramClient, events, Button
import requests
#from headers import headers
#import urls
import os
import requests
import cryptg
import asyncio
import shutil
import subprocess
from mega import Mega
mega = Mega()
m = mega.login()
#from flask import request

client = TelegramClient('Tamilmv',1667813,"1f6921c27bf6cd01aba471a14ff33bcb").start(bot_token="1629668032:AAFBZ-JS7fxlTfvQNpSJYO-YSk6iGFvWvsU")


        
@client.on(events.NewMessage(pattern='/url'))
async def handler(event):
    link =event.text.split(' ')[1]
    l =link.split('/')[-1]
    chat = await event.get_chat()
    
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid=35989439&title={l}&description=Join%20our%20Official%20Telegram%20Channel%20to%20see%20more%20movies.%20Click%20on%20the%20link%20below.0A%0A%https://t.me/Fx_Movies"
    r = requests.get(s).json()
    z=r['data']["item_id"]
    await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("🔗 PDisk Link 🔗",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "__Here it is..!\nI am__ **uploading** __what you gave me to upload. After a couple of minutes,__ **click on the link below and take a look.** \n\n __Join Our Channel__ ©\n**@Fx_Movies**", buttons=markup)
            
            #rgx = w
@client.on(events.NewMessage(pattern='/magnet'))
async def handler(event):
    link =event.text.split(' ')[1]
    l =link.split('/')[-1]
    chat = await event.get_chat()
    
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid=35989439&title={l}&description=Join%20our%20Official%20Telegram%20Channel%20to%20see%20more%20movies.%20Click%20on%20the%20link%20below.0A%0A%https://t.me/Fx_Movies"
    r = requests.get(s).json()
    z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("🔗 PDisk Link 🔗",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "__Here it is..!\nI am__ **uploading** __what you gave me to upload. After a couple of minutes,__ **click on the link below and take a look.** \n\n __Join Our Channel__ ©\n**@Fx_Movies**", buttons=markup)
            
@client.on(events.NewMessage(pattern='/telepdisk'))
async def handler(event):
   # 
    chat = await event.get_chat()
    dw = await event.get_reply_message()
    #links =event.text.split(" ")[1]
    await client.send_message(chat,"**Downloading....** ⬇️ \n __please wait__")
    ss=await dw.download_media()
    shutil.move(f"/app/{ss}",f"/app/Downloads/{ss}")
    #await client.send_message(chat,f"")
    link =f"https://tamilmvic.herokuapp.com/files/{ss}"
    l =link.split('/')[-1]
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid=35989439&title={l}&description=Join%20our%20Official%20Telegram%20Channel%20to%20see%20more%20movies.%20Click%20on%20the%20link%20below.0A%0A%https://t.me/Fx_Movies"
    r = requests.get(s).json()
    z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("🔗 PDisk Link 🔗",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "__Here it is..!\nI am__ **uploading** __what you gave me to upload. After a couple of minutes,__ **click on the link below and take a look.** \n\n __Join Our Channel__ ©\n**@Fx_Movies**", buttons=markup)
            
@client.on(events.NewMessage(pattern='(?i)/ls'))

async def handler(event):

    chat = await event.get_chat()

    link =event.text.split(" ")[1]

    c = subprocess.getoutput(f"pip install {link}")
    print (c)
    await client.send_message(chat,"finish")
@client.on(events.NewMessage(pattern='(?i)/upload'))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    #links =event.text.split(" ")[1]
    await client.send_message(chat,"**Downloading....** ⬇️ \n __please wait__")
    ss=await dw.download_media()
    shutil.move(f"/app/{ss}",f"/app/templates/download/{ss}")
    await client.send_message(chat,f"https://tm-pdisk.herokuapp.com/files/{ss}")

        

      #  os.rename(ss,links)

        

    if os.path.exists(f"/app/Download/{chat.username}"):
        await client.send_message(chat,"**Downloading....** ⬇️ \n __please wait__")
        ss=await dw.download_media()
        await client.send_message(chat,f"https://tm-pdisk.herokuapp.com/u?url={ss}")
  
@client.on(events.NewMessage(pattern='(?i)/del'))

async def handler(event):

    chat = await event.get_chat()

    

    print(chat.username)

    

    #dw = await event.get_reply_message()

    shutil.rmtree("./Downloads/")
    os.mkdir("./Downloads")
    await client.send_message(chat,"ss")
@client.on(events.NewMessage(pattern='/torrent'))
async def handler(event):
    link =event.text.split(' ')[1]
    l =link.split('/')[-1]
    chat = await event.get_chat()
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid=35989439&title={l}&description=Join%20our%20Official%20Telegram%20Channel%20to%20see%20more%20movies.%20Click%20on%20the%20link%20below.0A%0A%https://t.me/Fx_Movies"
    r = requests.get(s).json()
    z=r['data']["item_id"]
    await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("🔗 PDisk Link 🔗",f"https://tm-pdisk.herokuapp.com/e?url={z}"))
    await client.send_message(chat, "It has been an hour since I posted this torrent link. So I call this dead torrent and stop it.\n\n __Join Our Channel__ ©\n**@Fx_Movies**", buttons=markup)
            
            #rgx = w
    


client.start()
client.run_until_disconnected()
