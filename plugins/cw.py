#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE
#  Code edited By Cryptostark
import urllib
import urllib.parse
import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM22pe6lllPFfUMQfj47agK1PJ_Sb3P_jty9S9_yCNwT87DTolChZKFm091O3K6UCQ61qHUHBgJg811eub1T1Bqn2HHYPkGrrknKaHDgj-ofQZnWBUZJNMaKHfDFd5HoVbeQtqEgVDJHMO9Oq7q5YLIaX9MYaaDreXLDWkxzVvrng6HXTz3whbyoYzOv_4bks3_8HOqCcqkbQL6XZehh398zRw6zPjO42okH0WoX-KNmjcICMpg"
bc_url = (f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos")
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

@bot.on_message(filters.command(["cw"]))
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False

    url = "https://elearn.crwilladmin.com/api/v5/login-other"
    data = {
        "deviceType": "android",
        "password": "Rohit@123",
        "deviceIMEI": "08750aa91d7387ab",
        "deviceModel": "Google sdk_gphone_x86",
        "deviceVersion": "R(Android 11.0)",
        "email": "",
        "deviceToken": "e-vGpi82QmOcr0-twQikSD:APA91bFkMLCTwHnENgYIEvwyeOXsc0j7YXCkJleB76Swv2Z0-Bf6nb2sAAeCPk8lDz79RX_qv2jCQHFzrbOTiWg1lXa4r724v9NSqyP144Sk0Gqa-XLSPM7IQb31UfZzF7P5V0TLXIJU"
       }
    headers = {
        "Host": "elearn.crwilladmin.com",
        "Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MDg1Mzk5MzYsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZFhwRGJqaFdURUZLVXk5ckwwSmhPV3BSTldocWR6MDkiLCJmaXJzdF9uYW1lIjoiTm05cWRXRnFjbEpxSzA5eU5WTnFMekEzT1VNNVVUMDkiLCJlbWFpbCI6IlpIUXJhVWxYU0RaRmJqRXZiV2w2TUhSak5ucEZLekZNTldoTk5VdzNNVlppYW5CWVdXSXJaVmt5TUQwPSIsInBob25lIjoiVDNWS1JYaFlORFJITWtsRWRHdERPVEJ2Vm5WMVVUMDkiLCJyZWZlcnJhbF9jb2RlIjoiVTBGTFpFdERSVlo2TTJodGNUZHNaMjVsUkhaS1p6MDkiLCJkZXZpY2VfdHlwZSI6ImFuZHJvaWQiLCJkZXZpY2VfdmVyc2lvbiI6IlIoQW5kcm9pZCAxMS4wKSIsImRldmljZV9tb2RlbCI6Ikdvb2dsZSBzZGtfZ3Bob25lX3g4NiIsInJlbW90ZV9hZGRyIjoiMjIzLjE3OC4yMTMuNTQifX0.DUwvVT6ar1NqmYczhsT6Ijn35bPVn1HfenNuBLUk9tnX8wzDcwuFGcktpXBnYwkYgocA95_8SR3UB-oXZkXu_4hDYmN84GGunicDyrSed8OTcE-z7j_iD6as9HkWX9FiOEBL8mcDsen5XXtMFNeKdHCcPCjPzq2P9FfaztifFIi-2usm6w9jNHuq6mYk8etEIKIlWVh0giEdf_jHRjiX36bfNzNN3PIfWjnZyixK0z_1oeIUDGAC6CITTD53o5PlhlDnbPKnQeyOixFzWdOvZUPllBgfIqltNhwaM83BHQPOwtcne18SfnIRWQEVRBK4wVOu0Y-GKZ89NpzFfVM4XQ",
        "Usertype": "2",
        "Appver": "84",
        "Apptype": "android",
        "Content-Type": "application/json; charset=utf-8",
        "Content-Length": "352",
        "Accept-Encoding": "gzip, deflate",
        "user-agent": "okhttp/5.0.0-alpha",
        'Connection': 'Keep-Alive'
       }
     proxy_host = ['104.26.3.116']
     proxies = {
             'https': proxy_host,
             'http': proxy_host,
         }
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password** \n or \nSend **TOKEN** like This this:-  **TOKEN**" )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    s = requests.Session()
    if "*" in raw_text:
      data["email"] = raw_text.split("*")[0]
      data["password"] = raw_text.split("*")[1]
      await input1.delete(True)
      #s = requests.Session()
      response = s.post(url = url, headers=headers, json=data, timeout=10)
      if response.status_code == 200:
          data = response.json()
          token = data["data"]["token"]
          await m.reply_text(token)
      else:
           await m.reply_text("go back to response")
      #token = "4ffd1627981589c0a1261f7a114fbbf8bc87c6d9"
      await m.reply_text(f"```{token}```")
    else:
      token = raw_text
    html1 = s.get("https://elearn.crwilladmin.com/api/v5/comp/my-batch?&token=" + token).json()
    topicid = html1["data"]["batchData"]
    cool=""
    for data in topicid:
        instructorName=(data["instructorName"])
        FFF="**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa =f" ```{data['id']}```      - **{data['batchName']}**\n{data['instructorName']}\n\n"
        #aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}')>4096:
            await m.reply_text(aa)
            cool =""
        cool+=aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    html2 = s.get("https://elearn.crwilladmin.com/api/v5/comp/batch-topic/"+raw_text2+"?type=class&token="+token).json()
    topicid = html2["data"]["batch_topic"]
    bn = html2["data"]["batch_detail"]["name"]
    vj=""
    for data in topicid:
        tids = (data["id"])
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            await m.reply_text(idid)
            vj = ""
        vj+=idid
    vp = ""
    for data in topicid:
        tn = (data["topicName"])
        tns=f"{tn}&"
        if len(f"{vp}{tn}")>4096:
            await m.reply_text(tns)
            vp=""
        vp+=tns
    cool1 = ""
    for data in topicid:
        t_name=(data["topicName"].replace(" ",""))
        tid = (data["id"])
        scraper = cloudscraper.create_scraper()
        ffx = s.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+tid+"&token="+token).json()
            #ffx = json.loads(html3)
        vcx =ffx["data"]["class_list"]["batchDescription"]
        vvx =ffx["data"]["class_list"]["classes"]
        vvx.reverse()
        zz= len(vvx)
        BBB = f"{'**TOPIC-ID - TOPIC - VIDEOS**'}"
        hh = f"```{tid}```     - **{t_name} - ({zz})**\n"

#         hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"

        if len(f'{cool1}{hh}')>4096:
            await m.reply_text(hh)
            cool1=""
        cool1+=hh
    await m.reply_text(f'Batch details of **{bn}** are:\n\n{BBB}\n\n{cool1}\n\n**{vcx}**')
    editable2= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")    
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    try:
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
        
#              xvv = raw_text9.split('&')
#              for z in range(0,len(xvv)):
#                  p =xvv[z]

            #gettting all json with diffrent topic id https://elearn.crwilladmin.com/api/v1/comp/batch-detail/881?redirectBy=mybatch&topicId=2324&token=d76fce74c161a264cf66b972fd0bc820992fe57
            #scraper = cloudscraper.create_scraper()
            html4 = s.get("https://elearn.crwilladmin.com/api/v1/comp/batch-detail/"+raw_text2+"?redirectBy=mybatch&topicId="+t+"&token="+token).content
            ff = json.loads(html4)
            #vc =ff.json()["data"]["class_list"]["batchDescription"]
            mm = ff["data"]["class_list"]["batchName"].replace("/ "," ")
            vv =ff["data"]["class_list"]["classes"]
            vv.reverse()
            #clan =f"**{vc}**\n\nNo of links found in topic-id {raw_text3} are **{len(vv)}**"
            #await m.reply_text(clan)
            count = 1
            try:
                for data in vv:
                    vidid = (data["id"])
                    lessonName = (data["lessonName"]).replace("/", "_")
                    
                    bcvid = (data["lessonUrl"][0]["link"])
                     #lessonName = re.sub('\|', '_', cf)

                    if bcvid.startswith("62"):
                        try:
                            #scraper = cloudscraper.create_scraper()
                            html6 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video = json.loads(html6)
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            #print(video_url)
                            #scraper = cloudscraper.create_scraper()
                            html5 = s.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl = json.loads(html5)
                            stoken = surl["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url+"&bcov_auth="+stoken)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    elif bcvid.startswith("63"):
                        try:
                            #scraper = cloudscraper.create_scraper()
                            html7 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video1 = json.loads(html7)
                            video_source1 = video1["sources"][5]
                            video_url1 = video_source1["src"]
                            #print(video_url)
                            #scraper = cloudscraper.create_scraper()
                            html8 = s.get("https://elearn.crwilladmin.com/api/v1/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl1 = json.loads(html8)
                            stoken1 = surl1["data"]["token"]
                            #print(stoken)
                            
                            link = (video_url1+"&bcov_auth="+stoken1)
                            #print(link)
                        except Exception as e:
                            print(str(e))
                    #cc = (f"{lessonName}:{link}")
                    #await m.reply_text(cc)
                    else:
                        link=("https://www.youtube.com/embed/"+bcvid)
                    cc = (f"{lessonName}::{link}")
                    with open(f"{mm }{t_name}.txt", 'a') as f:
                        f.write(f"{lessonName}:{link}\n")
                    #await m.reply_document(f"{mm }{t_name}.txt")
            except Exception as e:
                await m.reply_text(str(e))
        await m.reply_document(f"{mm }{t_name}.txt")
        #os.remove(f"{mm }{t_name}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5:message = await bot.listen (editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            scraper = cloudscraper.create_scraper()
            html7 = scraper.get("https://elearn.crwilladmin.com/api/v1/comp/batch-notes/"+raw_text2+"?topicid="+raw_text2+"&token="+token).content
            pdfD=json.loads(html7)
            k=pdfD["data"]["notesDetails"]
            bb = len(pdfD["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                
                for data in k:
                    name=(data["docTitle"])
                    s=(data["docUrl"]) 
                    xi =(data["publishedAt"])
                    with open(f"{mm }{t_name}.txt", 'a') as f:
                        f.write(f"{name}:{s}\n")
                    continue
                await m.reply_document(f"{mm }{t_name}.txt")
                    
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("Done")
