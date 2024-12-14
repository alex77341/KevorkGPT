import requests, base64, json, telebot, os
from bs4 import BeautifulSoup
from KeepAliva import keep_alive

proxy = "UbGMph:w4mknx@194.67.222.230:9242"

proxies = {
    "http": f"http://{proxy}",
    "https": f"https://{proxy}",
}

bot = telebot.TeleBot("7564960170:AAGMzCRpROoE4jmeiOcbcoe6F-0P-Vp8yrc")

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
    response = requests.post(auth_url, headers=auth_header, data=auth_data, proxies=proxies)
    response_data = response.json()
    return response_data['access_token']

def get_track_details(spotify_url, token):
    track_id = spotify_url.split("/")[-1].split("?")[0]
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}  
    response = requests.get(url, headers=headers, proxies=proxies)
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
    response = requests.get(search_url, headers=headers, params=params, proxies=proxies)
    if response.status_code == 200:
        data = response.json()
        if data['tracks']['items']:
            first_song = data['tracks']['items'][0]
            return first_song['external_urls']['spotify']
        else:
            return "No songs found."
    else:
        return f"Error {response.status_code}: {response.text}"

def linko(title, ytid, id):
    url = "https://spotiflyer.app/wp-content/plugins/codehap_spotifyDownloader/download.php"
    headers = {"Accept":"*/*","Accept-Language":"en-GB,en;q=0.9,es-MX;q=0.8,es;q=0.7,ru-BY;q=0.6,ru;q=0.5,en-US;q=0.4,ar-AE;q=0.3,ar;q=0.2","Content-Length":"562","Content-Type":"application/x-www-form-urlencoded","Cookie":"_ga_CQDPPTQ2K9=GS1.1.1734134607.1.0.1734134607.0.0.0; cf_clearance=wX4gky7iL1Y2anD1Nsb3RNX0fmTIOZemmQcln5xuTKQ-1734134607-1.2.1.1-H1B9BYzb2TG8xkEWrd5PlqTz3dlk._gRYOsPkLqEX_cD48iHYuHv1pmjb1dBvLiEqM4BdRH_PqKG.gIM59qGIN0dMxf0cPgUIsLX4qCy5aaEUoInWLLBKQ_rfqG160Ovmra9BTUvzURJZ48hdLgZN3UnxRySP4Syek81u3NZ7AGXvCUCG75CzzGULRj8jYCCdd5UmyGxkYwbnFgShMq2mmJrJvecwO_nZwTL.Z38AC63rLyKsAvKS9PtOKK4I_CZO6n2wBfA5N95798QjkfZLn8pyOSJ74nputhN2h5_dEXPhqC4o5TckgD1Gwt8_MgL_8Ut1p7lkyXcBBtbE7JfLxyV9MSguoo7oi94dM6OsuufXX7XDKeH0xO16tE1fGIgk7O2pg5TLKqKBzBRIHurIQ; _ga=GA1.2.794173983.1734134607; _gid=GA1.2.490855167.1734134608; _gat_gtag_UA_254550169_1=1; gads=ID=37fc9e336bbe1354:T=1734134608:RT=1734134608:S=ALNI_MbBq8O-l6-p6403vATy5U_eDnP-4w; gpi=UID=00000fbc01192373:T=1734134608:RT=1734134608:S=ALNI_Mb5pE-Wy8EMe7y3SJzw3ICWmflhQw; __eoi=ID=12897829e5ede89c:T=1734134608:RT=1734134608:S=AA-AfjY7rznXTyQBI6G2-TxSNc8v; FCNEC=%5B%5B%22AKsRol_hdODvCasic6VDib4uZuVDMmZWGOT465KiVaKYu753XCYdF1BVf1-w0DzUW7C9XNK8WjCu5J91bXgZSfSjEoEZS_vy-_Jp7BV6mHkBmte6IfVSBdj4oGUAIj6Xlr6AKqANRNKTx1u6jtBABzWUV6kKV_Oq4A%3D%3D%22%5D%5D","Origin":"https://spotiflyer.app","Referer":"https://spotiflyer.app/","Sec-Ch-Ua":'"Not-A.Brand";v="99", "Chromium";v="124"',"Sec-Ch-Ua-Mobile":"?1","Sec-Ch-Ua-Platform":'"Android"',"Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"}
    data = {"previewUrl": "", "id": f"{id}", "ytid": f"{ytid}", "title": f"{title}", "type": 3}
    response_content = requests.post(url=url, headers=headers, data=data, proxies=proxies).content
    soup = BeautifulSoup(response_content, 'html.parser')
    meta_tag = soup.find('meta', {'http-equiv': 'refresh'})
    if meta_tag and 'content' in meta_tag.attrs:
        content_value = meta_tag['content']
        url = content_value.split('URL=')[-1]
        return url
    else:
        return None

def download_song(link):
    url = "https://spotiflyer.app/wp-content/plugins/codehap_spotifyDownloader/result.php"
    headers = {"Accept":"*/*","Accept-Language":"en-GB,en;q=0.9,es-MX;q=0.8,es;q=0.7,ru-BY;q=0.6,ru;q=0.5,en-US;q=0.4,ar-AE;q=0.3,ar;q=0.2","Content-Length":"98","Content-Type":"application/x-www-form-urlencoded","Cookie":"_ga_CQDPPTQ2K9=GS1.1.1734134607.1.0.1734134607.0.0.0; cf_clearance=wX4gky7iL1Y2anD1Nsb3RNX0fmTIOZemmQcln5xuTKQ-1734134607-1.2.1.1-H1B9BYzb2TG8xkEWrd5PlqTz3dlk._gRYOsPkLqEX_cD48iHYuHv1pmjb1dBvLiEqM4BdRH_PqKG.gIM59qGIN0dMxf0cPgUIsLX4qCy5aaEUoInWLLBKQ_rfqG160Ovmra9BTUvzURJZ48hdLgZN3UnxRySP4Syek81u3NZ7AGXvCUCG75CzzGULRj8jYCCdd5UmyGxkYwbnFgShMq2mmJrJvecwO_nZwTL.Z38AC63rLyKsAvKS9PtOKK4I_CZO6n2wBfA5N95798QjkfZLn8pyOSJ74nputhN2h5_dEXPhqC4o5TckgD1Gwt8_MgL_8Ut1p7lkyXcBBtbE7JfLxyV9MSguoo7oi94dM6OsuufXX7XDKeH0xO16tE1fGIgk7O2pg5TLKqKBzBRIHurIQ; _ga=GA1.2.794173983.1734134607; _gid=GA1.2.490855167.1734134608; _gat_gtag_UA_254550169_1=1; gads=ID=37fc9e336bbe1354:T=1734134608:RT=1734134608:S=ALNI_MbBq8O-l6-p6403vATy5U_eDnP-4w; gpi=UID=00000fbc01192373:T=1734134608:RT=1734134608:S=ALNI_Mb5pE-Wy8EMe7y3SJzw3ICWmflhQw; __eoi=ID=12897829e5ede89c:T=1734134608:RT=1734134608:S=AA-AfjY7rznXTyQBI6G2-TxSNc8v; FCNEC=%5B%5B%22AKsRol_hdODvCasic6VDib4uZuVDMmZWGOT465KiVaKYu753XCYdF1BVf1-w0DzUW7C9XNK8WjCu5J91bXgZSfSjEoEZS_vy-_Jp7BV6mHkBmte6IfVSBdj4oGUAIj6Xlr6AKqANRNKTx1u6jtBABzWUV6kKV_Oq4A%3D%3D%22%5D%5D","Origin":"https://spotiflyer.app","Referer":"https://spotiflyer.app/","Sec-Ch-Ua":'"Not-A.Brand";v="99", "Chromium";v="124"',"Sec-Ch-Ua-Mobile":"?1","Sec-Ch-Ua-Platform":'"Android"',"Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"}
    data = {"data": f"{link}"}
    b = requests.post(url=url, headers=headers, data=data, proxies=proxies)
    response_content = b.text
    soup = BeautifulSoup(response_content, "html.parser")
    form = soup.find("form", {"id": "downloadForm"})
    title = form.find("input", {"name": "title"})["value"]
    ytid = form.find("input", {"name": "ytid"})["value"]
    id = form.find("input", {"name": "id"})["value"]
    down_url = linko(title, ytid, id)
    return down_url

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "ارسل اسم الاغنية")

@bot.message_handler(func=lambda message: True)
def work(message):
    song = search_track(message.text)
    title, performer, duration = get_name(song)
    url = download_song(song)
    output_file = url.split("=")[2] + ".mp3"
    try:
        response = requests.get(url, stream=True, proxies=proxies)
        response.raise_for_status()
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        with open(output_file, "rb") as F:
            bot.send_audio(message.chat.id, F, title=title, performer=performer, duration=duration)
        os.remove(output_file)
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"An error occurred: {e}")

keep_alive()
bot.infinity_polling()