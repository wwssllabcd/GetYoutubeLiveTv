from flask import Flask

from get_youtube_live_to_m3u8 import gen_m3u8

app = Flask(__name__)
@app.route("/")

def home():
    return aaa

aaa = gen_m3u8()

app.run() #啟動伺服器
