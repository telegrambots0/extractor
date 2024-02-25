import json
import requests
import cloudscraper
from pyrogram import Client, filters
from pyrogram.types import Message

ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1VmXspFMod94-pT7xDCvmBEYt8U7f0mRB6XnG5huPE7I9qjhDW0qpx3LRyTD9WX7W6JvUGtgKN-qf1pJoZO-QXBMIykDivtAOgkJOmN-kyv4m_F0thrJ45z95hqWON0nsKBwvd"
bc_url = f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos"
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}

bot = Client("my_account")

@bot.on_message(filters.command(["cw"]))
async def account_login(bot: Client, m: Message):
    url = "https://elearn.crwilladmin.com/api/v5/login-other"
    data = {
        "deviceType": "android",
        "password": "",
        "deviceIMEI": "08750aa91d7387ab",
        "deviceModel": "Realme RMX2001",
        "deviceVersion": "R(Android 11.0)",
        "email": "",
        "deviceToken": "fYdfgaUaQZmYP7vV4r2rjr:APA91bFPn3Z4m_YS8kYQSthrueUh-lyfxLghL9ka-MT0m_4TRtlUu7cy90L8H6VbtWorg95Car6aU9zjA-59bZypta9GNNuAdUxTnIiGFxMCr2G3P4Gf054Kdgwje44XWzS9ZGa4iPZh"
    }
    headers = {
        "Host": "elearn.crwilladmin.com",
        "token": "",
        "usertype": "",
        "appver": "84",
        "apptype": "android",
        "content-type": "application/json; charset=UTF-8",
        "content-Length": "326",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/5.0.0-alpha.2",
        'Connection': 'Keep-Alive'
    }  
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password** \n or \nSend **TOKEN** like This this:-  **TOKEN**" )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    s = requests.Session()
    if "*" in raw_text:
        data["email"] = raw_text.split("*")[0]
        data["password"] = raw_text.split("*")[1]
        await input1.delete(True)
        response = s.post(url=url, headers=headers, json=data, timeout=10)
        if response.status_code == 200:
            data = response.json()
            token = data["data"]["token"]
            await editable.edit("**login Successful**")
            await m.reply_text(token)
        else:
            await m.reply_text("go back to response")
        await m.reply_text(f"```{token}```")
    else:
        token = raw_text
    url1 = s.get("https://elearn.crwilladmin.com/api/v5/my-batch?&token=" + token).json()
    b_data = url1["data"]["batchData"]
    cool = ""
    for data in b_data:
        aa = f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}') > 4096:
            await m.reply_text(aa)
            cool = ""
        cool += aa
    await m.reply(cool)
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    url2 = s.get("https://elearn.crwilladmin.com/api/v5/batch-topic/" + raw_text2 + "?type=class&token=" + token).json()
    b_data = url2["data"]["batch_topic"]
    bn = url2["data"]["batch_detail"]["name"]
    await m.reply_text(f'Batch details of **{bn}** are :')
    cool1 = ""
    for data in b_data:
        t_name = (data["topicName"].replace(" ", ""))
        tid = (data["id"])
        scraper = cloudscraper.create_scraper()
        ffx = s.get("https://elearn.crwilladmin.com/api/v5/batch-detail/" + raw_text2 + "?redirectBy=mybatch&b_data=" + tid + "&token=" + token).json()
        vcx = ffx["data"]["class_list"]["batchDescription"]
        vvx = ffx["data"]["class_list"]["classes"]
        vvx.reverse()
        zz = len(vvx)
        BBB = f"{'**TOPIC-ID - TOPIC - VIDEOS**'}"
        hh = f"```{tid}```     - **{t_name} - ({zz})**\n"
        hh = f"**Topic -** {t_name}\n**Topic ID - ** ```{tid}```\nno. of videos are : {zz}\n\n"
        if len(f'{cool1}{hh}') > 4096:
            await m.reply_text(hh)
            cool1 = ""
        cool1 += hh
    await m.reply_text(f'Batch details of **{bn}** are:\n\n{BBB}\n\n{cool1}\n\n**{vcx}**')
    editable2 = await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{vj}```")    
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    try:
        xv = raw_text3.split('&')
        for y in range(0, len(xv)):
            t = xv[y]
            html4 = s.get("https://elearn.crwilladmin.com/api/v5/batch-detail/" + raw_text2 + "?redirectBy=mybatch&b_data=" + t + "&token=" + token).content
            ff = json.loads(html4)
            mm = ff["data"]["class_list"]["batchName"].replace("/ ", " ")
            vv = ff["data"]["class_list"]["classes"]
            vv.reverse()
            count = 1
            try:
                for data in vv:
                    vidid = data["id"]
                    lessonName = data["lessonName"].replace("/", "_")
                    bcvid = data["lessonUrl"][0]["link"]
                    if bcvid.startswith("62"):
                        try:
                            html6 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video = json.loads(html6)
                            video_source = video["sources"][5]
                            video_url = video_source["src"]
                            html5 = s.get("https://elearn.crwilladmin.com/api/v5/livestreamToken?type=brightcove&vid=" + vidid + "&token=" + token).content
                            surl = json.loads(html5)
                            stoken = surl["data"]["token"]
                            link = video_url + "&bcov_auth=" + stoken
                        except Exception as e:
                            print(str(e))
                    elif bcvid.startswith("63"):
                        try:
                            html7 = s.get(f"{bc_url}/{bcvid}", headers=bc_hdr).content
                            video1 = json.loads(html7)
                            video_source1 = video1["sources"][5]
                            video_url1 = video_source1["src"]
                            html8 = s.get("https://elearn.crwilladmin.com/api/v5/livestreamToken?type=brightcove&vid=" + vidid + "&token=" + token).content
                            surl1 = json.loads(html8)
                            stoken1 = surl1["data"]["token"]
                            link = video_url1 + "&bcov_auth=" + stoken1
                        except Exception as e:
                            print(str(e))
                    else:
                        link = "https://www.youtube.com/embed/" + bcvid
                    cc = f"{lessonName}::{link}"
                    with open(f"{mm}{t_name}.txt", 'a') as f:
                        f.write(f"{lessonName}:{link}\n")
            except Exception as e:
                await m.reply_text(str(e))
        await m.reply_document(f"{mm}{t_name}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    try:
        notex = await m.reply_text("Do you want download notes ?\n\nSend **y** or **n**")
        input5 = message = await bot.listen(editable.chat.id)
        raw_text5 = input5.text
        if raw_text5 == 'y':
            scraper = cloudscraper.create_scraper()
            html7 = scraper.get("https://elearn.crwilladmin.com/api/v5/batch-notes/" + raw_text2 + "?b_data=" + raw_text2 + "&token=" + token).content
            pdfD = json.loads(html7)
            k = pdfD["data"]["notesDetails"]
            bb = len(pdfD["data"]["notesDetails"])
            ss = f"Total PDFs Found in Batch id **{raw_text2}** is - **{bb}** "
            await m.reply_text(ss)
            k.reverse()
            count1 = 1
            try:
                for data in k:
                    name = data["docTitle"]
                    s = data["docUrl"] 
                    xi = data["publishedAt"]
                    with open(f"{mm}{t_name}.txt", 'a') as f:
                        f.write(f"{name}:{s}\n")
                    continue
                await m.reply_document(f"{mm}{t_name}.txt")
            except Exception as e:
                await m.reply_text(str(e))
            #await m.reply_text("Done")
    except Exception as e:
        print(str(e))
    await m.reply_text("Done")

bot.run()
