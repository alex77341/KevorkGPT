
import requests , telebot
import hashlib
import hmac
import os
import time
from datetime import datetime, timezone
import re
from KeepAliva import keep_alive

bot = telebot.TeleBot("7929822230:AAFItSMmR-QKP6bm6i9Fikt1sDfD8xvaLH8")


class Clened:
    def __init__(self):
        self.headers_base = {
            'User-Agent': "LALALAI/2.8.2.146 (android-armv8)",
            'Accept-Encoding': "gzip",
            'authorization': "license"
        }
        self.file_id = None

    def sign(self, key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def Signature(self, key, date_stamp, region, service):
        k_date = self.sign(('AWS4' + key).encode('utf-8'), date_stamp)
        k_region = self.sign(k_date, region)
        k_service = self.sign(k_region, service)
        k_signing = self.sign(k_service, 'aws4_request')
        return k_signing

    def Upload(self):
        url = "https://www.lalal.ai/api/upload/credentials/"
        res = requests.post(url, headers=self.headers_base).json()
        self.file_id = res['result']['file_id']
        return res['result']

    def upload_audio(self, file_path, creds):
        method = 'PUT'
        service = 's3'
        host = f"lalalai.s3.{creds['region']}.amazonaws.com"
        endpoint = f"https://{host}/media/source/{self.file_id}"
        content_type = "audio/x-wav"
        region = creds['region']

        now = datetime.now(timezone.utc)
        amz_date = now.strftime('%Y%m%dT%H%M%SZ')
        date_stamp = now.strftime('%Y%m%d')

        with open(file_path, 'rb') as f:
            payload = f.read()

        Wav = hashlib.sha256(payload).hexdigest()
        MrBeast = f"/media/source/{self.file_id}"
        Quick = "x-id=PutObject"

        Coin = (
            f"content-disposition:attachment; filename*=UTF-8''audio.wav\n"
            f"content-type:{content_type}\n"
            f"host:{host}\n"
            f"x-amz-content-sha256:{Wav}\n"
            f"x-amz-date:{amz_date}\n"
            f"x-amz-security-token:{creds['credentials']['SessionToken']}\n"
        )

        signed_headers = "content-disposition;content-type;host;x-amz-content-sha256;x-amz-date;x-amz-security-token"

        Cool = (
            f"{method}\n{MrBeast}\n{Quick}\n"
            f"{Coin}\n{signed_headers}\n{Wav}"
        )

        algorithm = 'AWS4-HMAC-SHA256'
        Tom = f"{date_stamp}/{region}/{service}/aws4_request"
        Sorry = (
            f"{algorithm}\n{amz_date}\n{Tom}\n"
            f"{hashlib.sha256(Cool.encode('utf-8')).hexdigest()}"
        )

        signing_key = self.Signature(
            creds['credentials']['SecretAccessKey'], date_stamp, region, service
        )
        signature = hmac.new(signing_key, Sorry.encode('utf-8'), hashlib.sha256).hexdigest()

        Auth = (
            f"{algorithm} Credential={creds['credentials']['AccessKeyId']}/{Tom}, "
            f"SignedHeaders={signed_headers}, Signature={signature}"
        )

        headers = {
            "User-Agent": "aws-sdk-dart/0.3.1 aws-sigv4-dart/0.6.4",
            "Connection": "close",
            "Accept-Encoding": "gzip",
            "Content-Type": content_type,
            "x-amz-date": amz_date,
            "amz-sdk-invocation-id": os.urandom(16).hex(),
            "amz-sdk-request": "attempt=1; max=3",
            "authorization": Auth,
            "x-amz-content-sha256": Wav,
            "content-disposition": "attachment; filename*=UTF-8''audio.wav",
            "x-amz-security-token": creds['credentials']['SessionToken']
        }

        params = {"x-id": "PutObject"}
        res = requests.put(endpoint, headers=headers, params=params, data=payload)
        if res.status_code != 200:
            raise Exception("Upload failed", res.text)

    def Cc(self):
        url = "https://www.lalal.ai/api/check/"
        payload = {'id': self.file_id, 'response_format': "multistem"}
        res = requests.post(url, data=payload, headers=self.headers_base)
        return res.json()

    def Pro(self):
        url = "https://www.lalal.ai/api/preview/"
        payload = {
            'id': self.file_id,
            'stem': "voice",
            'with_segments': "true",
            'noise_cancelling_level': "1",
            'splitter': "perseus"
        }
        res = requests.post(url, data=payload, headers=self.headers_base)
        return res.json()

    def Download(self, url):
        headers = {
            'User-Agent': "just_audio/2.8.2 (Linux;Android 11) ExoPlayerLib/2.18.7",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "identity"
        }
        r = requests.get(url, headers=headers)
        with open("Clened.wav", "wb") as f:
            f.write(r.content)
        print("[*] Done Download Clened.wav File .!")
    def Voice(self, file_path):
        creds = self.Upload()
        print("[*] Waiting for Update Credentials...")
        self.upload_audio(file_path, creds)
        print("[*] Waiting for UploadAudio...")
        self.Cc()
        print("[*] Waiting for Check...")
        self.Pro()
        print("[*] Waiting for processing...")
        while True:
            result = self.Cc()
            print("[*] Waiting for Cleaning...")
            if 'playlist_file' in str(result):
                print("[+] File is ready!")              
                url = re.search(r"'label': 'voice', 'url': '([^']+)'", str(result)).group(1)
                self.Download(url)
                break
            else:
                time.sleep(3)

#Voice = input("[#] Enter The Audio File path Or Name (To Clean It From Noise Voice) : ")
#Clened().Voice(Voice)

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"hey")

@bot.message_handler(content_types=["audio","voice"])
def c(message):
	if message.voice :
		file_info = bot.get_file(message.voice.file_id)
	elif message.audio :
		file_info = bot.get_file(message.audio.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	bot.reply_to(message,"working...")
	with open("potato.mp3","wb") as bruh :
		bruh.write(downloaded_file)
	Clened().Voice("potato.mp3")
	bot.send_audio(chat_id=message.chat.id,audio="Clened.wav")

keep_alive()
bot.infinity_polling()
