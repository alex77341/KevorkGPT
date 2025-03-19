import os
import requests, base64, json, telebot
from bs4 import BeautifulSoup
from KeepAliva import keep_alive

bot = telebot.TeleBot("7564960170:AAEM9321ViN7FQrW1sQIwBXHkCLXErYDrLg")

CLIENT_ID = '0a91bd93f2af480cbcaa90134f39bef3'
CLIENT_SECRET = '5d2823db8f8d439c999601fe12fbbfbe'
REDIRECT_URI = 'https://t.me/KEV0RK'

def get_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = {
        'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode('utf-8')).decode('utf-8')
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(auth_url, headers=auth_header, data=auth_data)
    response_data = response.json()
    return response_data['access_token']

def get_track_details(spotify_url, token):
    track_id = spotify_url.split("/")[-1].split("?")[0]
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}  
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    track_data = response.json()
    track_name = track_data["name"]
    artist_name = ", ".join(artist["name"] for artist in track_data["artists"])
    duration_ms = track_data["duration_ms"]
    duration_sec = duration_ms // 1000
    
    return track_name, artist_name, duration_sec

def get_name(spot):
    spotify_url = spot
    token = get_access_token()
    try:
        track_name, artist_name, duration_sec = get_track_details(spotify_url, token)
        return track_name, artist_name, duration_sec
    except Exception as e:
        print(f"An error occurred: {e}")

def search_track(query):
    access_token = get_access_token()
    search_url = 'https://api.spotify.com/v1/search'
    params = {
        'q': query,
        'type': 'track',
        'limit': 1
    }
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['tracks']['items']:
            first_song = data['tracks']['items'][0]
            return first_song['external_urls']['spotify']
        else:
            return "No songs found."
    else:
        return f"Error {response.status_code}: {response.text}"

def download_song(link):
    url = "https://spotisongdownloader.to/api/composer/spotify/wertyuht9847635.php"
    s = requests.Session()
    ss = s.get(url)
    PHPSESSID = s.cookies.get("PHPSESSID")
    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Language":"en-GB,en;q=0.9,es-MX;q=0.8,es;q=0.7,ru-BY;q=0.6,ru;q=0.5,en-US;q=0.4,ar-AE;q=0.3,ar;q=0.2","Content-Length":"136","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":f"_ga=GA1.1.1137895648.1737412882; PHPSESSID={PHPSESSID}; _ga_X67PVRK9F0=GS1.1.1741024949.2.1.1741024967.0.0.0; quality=m4a","Origin":"https://spotisongdownloader.to","Referer":"https://spotisongdownloader.to/track.php","Sec-Ch-Ua":'"Not A(Brand";v="8", "Chromium";v="132"',"Sec-Ch-Ua-Mobile":"?1","Sec-Ch-Ua-Platform":'"Android"',"Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36","X-Requested-With":"XMLHttpRequest"}
    data = {"url": link}
    r = requests.post(url,headers=headers,data=data).json()
    return r["dlink"]

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "ارسل اسم الاغنية")

@bot.message_handler(func=lambda message: True)
def work(message):
    song = search_track(message.text)
    bot.send_message(message.chat.id,song)
    title, performer, duration = get_name(song)
    url = download_song(song)
    #bot.send_audio(message.chat.id, url, title=title, performer=performer, duration=duration)
    output_file = title+".mp3"
    print(output_file)
    try:
        #response = requests.get(url, stream=True)
#        response.raise_for_status()
        with open(output_file, "wb") as file:
            file.write(requests.get(url).content)
            #for chunk in response.iter_content(chunk_size=8192):
#                file.write(chunk)
        with open(output_file, "rb") as F:
            bot.send_audio(message.chat.id, F, title=title, performer=performer, duration=duration)
        os.remove(output_file)
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"An error occurred: {e}")

keep_alive()
bot.infinity_polling()