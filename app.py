
import requests ,telebot
from KeepAliva import keep_alive

bot = telebot.TeleBot("7564960170:AAGMzCRpROoE4jmeiOcbcoe6F-0P-Vp8yrc")

def download(link):
	url = "https://api.downloadsound.cloud/track"
	params = {"url": link} 
	response = requests.post(url, json=params)
	if response.status_code == 200:
	   res = response.json()
	   mp3 = res['url'];title = res['title']
	   return(mp3)
	else:
		return("No sounds added!")

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"ارسل اسم الاغنية")

@bot.message_handler(func=lambda message:True)
def search(message):
	word = message.text
	url = "https://api-mobile.soundcloud.com/search/query"
	params = {
  'client_id': "dbdsA8b6V6Lw7wzu1x0T4CLxt58yd4Bf",
  'limit': "1",
  'q': word,
  'filter.content_type': "tracks",
  'version': "v2",
  'previous_urn': "soundcloud:search:11ef9bfa-1fcf-409a-b16f-587a96312aef"
}
	headers = {
  'User-Agent': "SoundCloud/2024.05.22-release (Android 12.0.0; OPPO CPH2477)",
  'Connection': "Keep-Alive",
  'Accept': "application/json; charset=utf-8",
  'Accept-Encoding': "gzip",
  'ADID': "fed2f546-cf3e-43c5-928f-dc4215081968",
  'ADID-TRACKING': "true",
  'Authorization': "OAuth 2-293571-921962155-lbaqyrfzZ2Srf3",
  'App-Locale': "en",
  'Device-Locale': "en-MM",
  'App-Version': "244050",
  'UDID': "501fc0e1eaa88aed3e5c9be75ed21f6f",
  'App-Requested-Features': "system_playlist_in_library=true",
  'App-Environment': "prod"
}
	response = requests.get(url, params=params, headers=headers)
	songs = response.json()
	song = songs["entities"][next(iter(songs["entities"]))]["data"]["permalink_url"]
	title = songs["entities"][next(iter(songs["entities"]))]["data"]["title"]
	bot.send_audio(message.chat.id,download(song),title=title)

keep_alive()
bot.infinity_polling()