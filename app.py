
import random,requests,re,os,pytz
from datetime import datetime
from time import sleep
from telebot import *
from pytube import YouTube , Search
from KeepAliva import keep_alive
import speedtest

bot = telebot.TeleBot("6499740840:AAG3eRq5-MPw8SIZ_Pbe4ZA6Oy79MKHdRMw")

##############################################

asker = []

#def gpt(message):
#	global asker
#	mc = message.chat.id + message.from_user.id
#	if mc in asker and La > 0 :
#		mess = message.text
#		rr = requests.get(f"https://chatgpt.apinepdev.workers.dev/?question={mess}").json()
#		nn = rr["answer"]
#		bot.reply_to(message ,nn)
#		asker.remove(mc)

members=[]
def get_photos(user):
    user_photos = bot.get_user_profile_photos(user)
    user_photos = user_photos.photos
    photos_ids = []
    for photo in user_photos:
        photos_ids.append(photo[0].file_id)
    return photos_ids

def check_admin_rights(chat_id, user_id):
    member = bot.get_chat_member(chat_id, user_id)
    return member.status == 'creator' or member.status == 'administrator'
games = """قائمة الالعاب :
• احكام
• حجرة
• خاتم
~"""
la3b = []
rdod = ["مرحباً"]
a7bk = ["انقلع"]
akrhk = ["احسن"]
a7lf = ["سيء"]

##############################################

A = "🪨"
B = "📜"
C = "✂️"
D = [A,B,C]
E = types.InlineKeyboardMarkup(row_width=3)
F = types.InlineKeyboardButton

##############################################

aa = F(f"{A}",callback_data="a")
bb = F(f"{B}",callback_data="b")
cc = F(f"{C}",callback_data="c")
E.add(aa,bb,cc)

##############################################

G = types.InlineKeyboardMarkup(row_width=1)
dd = F("🙂",url="https://t.me/RR6NR")
G.add(dd)

##############################################

keyboardGame = types.InlineKeyboardMarkup(row_width=4)
keyboardGame.add(
    F('👊🏻', callback_data='bt1'),
    F('👊🏼', callback_data='bt2'),
    F('👊🏽', callback_data='bt3'),
    F('👊🏾', callback_data='bt4')
)

##############################################

user_is_search_youtube = ""
search_word = ""
rep = ""
dow0 = ""

def SendOpSr(srWod:str):
    yt = Search(srWod)

    ur = yt.results
    urls = []
    a = 0
    for i in ur:
        if a == 5:
            break
        i = str(i)
        urs = i[i.find("videoId"): i.find(">")].replace("videoId=", "")
        urls.append("https://www.youtube.com/watch?v=" +urs)
        a += 1
    return urls

def extract_video_id(text):
    pattern = r'https://www\.youtube\.com/watch\?v=([^\s&]+)'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None

def MrkSr(word):
    mrk = types.InlineKeyboardMarkup(row_width=1)
    btns = []
    for url in SendOpSr(word):
        title_video = YouTube(url).title
        btn = types.InlineKeyboardButton(text=title_video, callback_data=url)
        btns.append(btn)
    mrk.add(*btns)
    return mrk

dow = types.InlineKeyboardMarkup(row_width=2)
dow1 = types.InlineKeyboardButton(text="تحميل الفيديو",callback_data="video")
dow2 = types.InlineKeyboardButton(text="تحميل الصوت",callback_data="audio")
dow.add(dow1,dow2)
##############################################

@bot.message_handler(commands=["/ping"])
def ping(message):
	s = speedtest.Speedtest()
	bot.reply_to(message,f"Upload speed : {s.upload()} m/s\nDownload speed : {s.download()} m/s")

@bot.message_handler(func=lambda message : True)

def st(message):
	global members,la3b,asker
	if message.chat.type == "private" :
		if message.text in ("/start","/help") :
			bot.send_message(message.chat.id,"هاي")
		elif message.from_user.id != 5989554287 :
			bot.reply_to(message,"تم ارسال رسالتك الى المطور")
			bot.forward_message(5989554287,from_chat_id=message.chat.id,message_id=message.message_id)
		elif message.from_user.id == 5989554287 :
			rere = message.reply_to_message.forward_from
			if rere and message.content_type == "text" :
					try :
						bot.send_message(rere.id,message.text)
						bot.reply_to(message,"تم ارسال رسالتك الى العضو")
					except :
						bot.reply_to(message,"لم يتم ارسال الرسالة الى العضو")
			elif message.content_type != "text" :
					bot.forward_message(chat_id=rere.id,from_chat_id=message.chat.id,message_id=message.message_id)
					bot.reply_to(message,"تم ارسال رسالتك الى العضو")
			
	elif message.chat.type == "supergroup" :
		if message.text == "حجرة"  :
			bot.reply_to(message,f"""اختار حجرة {A} / ورقة {B} / مقص {C}""",reply_markup=E)
			mc = message.chat.id + message.from_user.id
			la3b.append(mc)
		elif message.text.startswith("ترجمي ") :
			text = message.text.replace("ترجمي ","")
			url = f"https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=ar&q={text}"
			R = requests.get(url)
			Alklma = R.json()
			Trgma = Alklma[0][0][0]
			bot.reply_to(message,Trgma)
		elif message.text in ("العاب","الالعاب") :
			bot.reply_to(message,games)
		elif message.text == "احكام"  :
		  	if len(members) > 0 :
		  		bot.send_message(message.chat.id,"في لعبة شغالة")
		  	else :
		  		bot.reply_to(message,"""بدأت لعبة الاحكام و اضفت اسمك للقائمة
	   	اللي يريد يلعب يرسل (انا)
	   	لما ينتهي العدد يرسل (تم) اللي بدأ اللعبة""")
		  		members.append(message.from_user.id)
		elif message.text == "انا" and len(members) > 0 :
		  		if message.from_user.id in members :
		  			bot.reply_to(message,"اسمك موجود بالقائمة")
		  		else :
		  			bot.reply_to(message,"ضفت اسمك للقائمة")
		  			members.append(message.from_user.id)
		elif message.text in ["تم"] :
			if 0 < len(members) > 1  and message.from_user.id == members[0] :
				rand_member = random.choice(members)
				mem = bot.get_chat_member(chat_id=message.chat.id,user_id=rand_member).user
				bot.send_message(message.chat.id,f"""تم اختيار  [{mem.first_name}](t.me/{mem.username})""",parse_mode="Markdown")
				members=[]
			elif len(members) < 0 :
				pass
			elif len(members) > 0 and message.from_user.id != members[0] :
				bot.reply_to(message,"لا تعيدها ، مو انت اللي بدأت اللعبة")
			elif 0 < len(members) < 2 and message.from_user.id == members[0]:
					bot.reply_to(message,"لتبدأ اللعبة تحتاج لاعبين اثنين عالاقل")
		elif message.text == "الساعة"   :
			tz = pytz.timezone("Asia/Damascus")
			now = datetime.now(tz)
			bot.reply_to(message,now.strftime("\r %I:%M"))
		elif message.text == "ثبتي" :
			if check_admin_rights(message.chat.id,message.from_user.id) or message.from_user.id == 5989554287 :
				re_mess = message.reply_to_message
				if re_mess :
					bot.pin_chat_message(message.chat.id,re_mess.message_id)
					bot.reply_to(message,"تم تثبيت الرسالة")
				else :
					bot.reply_to(message,"رد على الرسالة اللي تريد تثبتها")
		elif message.text == "الغي التثبيت":
			if check_admin_rights(message.chat.id,message.from_user.id) or message.from_user.id == 5989554287 :
				re_mess = message.reply_to_message
				if re_mess :
					bot.unpin_chat_message(chat_id=message.chat.id,message_id=re_mess.message_id)
					bot.reply_to(message,"تم الغاء تثبيت الرسالة")
				else :
					bot.reply_to(message,"رد على الرسالة اللي تريد تلغي تثبيتها")
		elif message.text == "الغي الكل":
			if check_admin_rights(message.chat.id,message.from_user.id) or message.from_user.id == 5989554287 :
				try :
					bot.unpin_all_chat_messages(message.chat.id)
					bot.reply_to(message,"تم الغاء تثبيت جميع الرسائل")
				except :
					bot.reply_to(message, "لا يوجد رسائل مثبتة")
		elif message.text == "اكشفي":
			reo = message.reply_to_message
			bb = bot.get_chat_member(message.chat.id,reo.from_user.id)
			if bb.status == "creator" :
				st ="المالك"
			elif bb.status == "administrator" :
				st = "ادمن"
			elif bb.status == "member" :
				st = "عضو"
			bot.reply_to(message,f"""• Name : {reo.from_user.first_name}\n• Username : @{reo.from_user.username}\n• ID : {reo.from_user.id}\n• STE : {st}""")
		elif message.text.startswith("مؤقت ") :
			mt = message.text.replace("مؤقت","")
			try :
				ss = int(mt)
				bot.reply_to(message,f"تم بدأ مؤقت لمدة {ss} ثانية من الان")
				sleep(ss)
				bot.reply_to(message,"انتهى الوقت المحدد")
			except :
				bot.reply_to(message,"حط رقم بعد الامر")
		elif message.text.startswith("قولي ") :
			mt = message.text.replace("قولي ","")
			bot.send_message(message.chat.id,mt)
		elif message.text == "مسح" :
			if check_admin_rights(message.chat.id,message.from_user.id) or message.from_user.id == 5989554287 :
				rer = message.reply_to_message
				mt = message.message_id
				bot.delete_message(chat_id=message.chat.id,message_id=rer.message_id)
				bot.delete_message(chat_id=message.chat.id,message_id=mt)
			else :
				bot.reply_to(message,"الامر مخصص للادمن")
		#elif message.text.startswith("احذفي "):
#			mt = message.text.replace("احذفي ","")
#			mt = int(mt)
#			mt = -mt 
#			dele = -1
#			bbb = []
#			while dele != mt :
#				messs = message[dele].message_id
#				bbb.append(messs)
#				dele-=1
#			bot.delete_message(chat_id=message.chat.id,message_id=bbb)
		elif message.text == "برا" and check_admin_rights(message.chat.id,message.from_user.id) or message.text == "برا" and message.from_user.id == 5989554287 :
			rero = message.reply_to_message.from_user.id
			rero1 = message.reply_to_message
			mem = bot.get_chat_member(message.chat.id,rero)
			if rero and mem.status == "member" :
				bot.send_message(message.chat.id,f"بباي @{rero1.from_user.username}")
				bot.kick_chat_member(message.chat.id,user_id=rero)
				bot.unban_chat_member(message.chat.id,user_id=rero)
			elif rero and mem.status == "administrator" :
				bot.reply_to(message,"ماتقدر تنفذ الامر على ادمن")
			elif rero and mem.status == "creator" :
				bot.reply_to(message,"ماتقدر تنفذ الامر على المالك")
		elif message.text in ("ايدي","ا") :
			user_id = message.from_user.id
			photos_ids = get_photos(user_id)
			reo = message
			bb = bot.get_chat_member(message.chat.id,reo.from_user.id)
			if bb.status == "creator" :
				st ="المالك"
			elif bb.status == "administrator" :
				st = "ادمن"
			elif bb.status == "member" :
				st = "عضو"
			bot.send_photo(message.chat.id,photos_ids[0],f"""• Name : {reo.from_user.first_name}\n• Username : @{reo.from_user.username}\n• ID : {reo.from_user.id}\n• STE : {st}""",reply_to_message_id=message.message_id)
		elif message.text.startswith("معنى ") :
		  	try:
		  		text = message.text.replace("معنى","")
		  		url = "https://3amyah.com/?s="+text
		  		req = requests.get(url).text
		  		m = re.findall('<meta name="description" content="(.*?)"/>',req)[0]
		  		bot.reply_to(message, m,parse_mode="markdown")
		  	except:
		  		bot.reply_to(message,'مالاقيت معنى')
		elif message.text.startswith("حملي ") :
			link = message.text.replace("حملي ","")
			yt = YouTube(link)
			video = yt.streams.get_highest_resolution()
			video_name = video.download()
			with open(f"{video_name}","rb") as w :
				bot.send_video(message.chat.id,w,reply_to_message_id=message.message_id)
			os.remove(f"{video_name}")
		elif message.text.startswith("يوت ") or message.text.startswith("yt ") or message.text.startswith("يوتيوب ") :
			baa = types.InlineKeyboardMarkup()
			b = types.InlineKeyboardButton(text="🙂",url="https://t.me/RR6NR")
			baa.add(b)
			searchw = " ".join(message.text.split(" ")[1:])
			test = SendOpSr(searchw)
			v_id = extract_video_id(str(test[1]))
			if v_id :
				main_url = "https://www.youtube.com/watch?v=" + str(v_id)
				yt = YouTube(main_url)
				aud = yt.streams.get_audio_only().download()
				with open(f"{aud}.jpg","wb") as S :
					r = requests.get(yt.thumbnail_url).content
					S.write(r)
				with open(f"{aud}","rb") as H :
					bot.send_audio(message.chat.id,H,reply_to_message_id=message.message_id,parse_mode="HTML",thumbnail=open(f"{aud}.jpg","rb") ,performer=yt.author,duration=yt.length,reply_markup=baa)
					os.remove(f"{aud}")
					os.remove(f"{aud}.jpg")
		elif message.text.startswith("بحث ") and len(message.text.split(" ")) > 1 :
			global user_is_search_youtube , search_word , rep
			rep = message.message_id
			user_is_search_youtube = message.from_user.id
			search_word = " ".join(message.text.split(" ")[1:])
			bot.reply_to(message,"نتائج البحث :\n~",reply_markup=MrkSr(search_word))
		elif message.text == "خاتم":
			bot.reply_to(message,"- اختار اليد اللي تتوقع فيها الخاتم\n~",reply_markup=keyboardGame)
			la3b.append(message.from_user.id)
		elif message.text == "روزان":
			if message.from_user.id == 6436896200 :
				bot.reply_to(message,"نعم ماما")
			elif message.from_user.id == 5989554287 :
				bot.reply_to(message,"نعم بابا")
			else :
				bot.reply_to(message,random.choice(rdod))
		elif message.text == "احبك":
			if message.from_user.id == 6436896200 :
				bot.reply_to(message,"احبك اكثرر مامااا")
			elif message.from_user.id == 5989554287 :
				bot.reply_to(message,"احبك اكثرر بابااا")
			else :
				bot.reply_to(message,random.choice(a7bk))
		elif message.text == "اكرهك":
			bot.reply_to(message,random.choice(akrhk))
		elif message.text == "احلف":
			bot.reply_to(message,random.choice(a7lf))
		elif message.text == "سؤال" :
			bot.reply_to(message,"هات سؤالك و بيجاوبك ChatGPT !!!")
			mc = message.chat.id + message.from_user.id
			asker.append(mc)
		elif len(asker) > 0 :
			mc = message.chat.id + message.from_user.id
			if mc in asker :
				mt = message.text
				rr = requests.get(f"https://chatgpt.apinepdev.workers.dev/?question={mt}").json()
				answer = rr["answer"]
				bot.reply_to(message,answer)
				asker.remove(mc)

##############################################

@bot.callback_query_handler(func=lambda call : True)

def wr(call):
	global la3b,dow0
	mc = call.message.chat.id + call.from_user.id
	if call.data in ("a","b","c") and mc in la3b :
		if call.data == "a":
			ant = A
		elif call.data == "b":
			ant = B
		elif call.data == "c":
			ant = C
		la3b=[]
		ana = random.choice(D)
		if ana == ant :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""انت : {ant}
انا : {ana}
النتيجة : تعادل\n~""",reply_markup=G)
		elif ana == B and ant == A :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""انت : {ant}
انا : {ana}
النتيجة : انا فزت\n~""",reply_markup=G)
		elif ana == A and ant == B :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""انت : {ant}
انا : {ana}
النتيجة : انت فزت\n~""",reply_markup=G)
		elif ana == B and ant == C :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""انت : {ant}
انا : {ana}
النتيجة : انت فزت\n~""",reply_markup=G)
		elif ana == C and ant == B :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""انت : {ant}
انا : {ana}
النتيجة : انا فزت\n~""",reply_markup=G)
		elif ana == A and ant == C :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""انت : {ant}
انا : {ana}
النتيجة : انا فزت\n~""",reply_markup=G)
		elif ana == C and ant == A :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""انت : {ant}
انا : {ana}
النتيجة : انت فزت\n~""",reply_markup=G)
	elif call.data in ("bt1","bt2","bt3","bt4") and call.from_user.id == la3b[0] :
		ran = random.randint(1,4)
		if call.data == "bt1" :
			bt = 1
		elif call.data == "bt2" :
			bt = 2
		elif call.data == "bt3" :
			bt = 3
		elif call.data == "bt4" :
			bt = 4
		if bt == ran :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- مبروك ربحت و اخذت الخاتم و حصلت 3 نقاط")
		elif bt != ran :
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="- خسرت و ضاع الخاتم ")
		la3b.remove(mc)
	elif call.data in ("video","audio") and user_is_search_youtube == call.from_user.id :
		yt = YouTube(dow0)
		bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
		with open("pic.jpg","wb") as Hadil :
			r = requests.get(yt.thumbnail_url).content
			Hadil.write(r)
		if call.data == "video":
			vid = yt.streams.get_highest_resolution().download()
			bot.send_video(call.message.chat.id,open(f"{vid}","rb"),caption=yt.title,duration=yt.length,thumbnail=open("pic.jpg","rb"),reply_to_message_id=rep)
			os.remove(f"{vid}")
			os.remove("pic.jpg")
		elif call.data == "audio" :
			audio = yt.streams.get_audio_only().download()
			bot.send_audio(call.message.chat.id,open(f"{audio}","rb"),caption=yt.title,duration=yt.length,thumbnail=open("pic.jpg","rb"),reply_to_message_id=rep)
			os.remove(f"{audio}")
			os.remove("pic.jpg")
	else :
		if user_is_search_youtube == call.from_user.id :
			data = call.data
			v_id = extract_video_id(data)
			if v_id :
				main_url = "https://www.youtube.com/watch?v=" + str(v_id)
				dow0 = main_url
				yt = YouTube(main_url)
				with open("pic.jpg","wb") as Sara :
					r = requests.get(yt.thumbnail_url).content
					Sara.write(r)
				bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
				bot.send_photo(call.message.chat.id,open("pic.jpg","rb"),reply_to_message_id=rep,reply_markup=dow,caption=yt.title)
				os.remove("pic.jpg")

##############################################

keep_alive()
bot.infinity_polling()
