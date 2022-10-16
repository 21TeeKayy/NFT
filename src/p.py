from ctypes import addressof
from genericpath import exists
from pickle import TRUE
from sqlite3 import dbapi2
from flask import Flask, render_template, request
import requests

import psycopg2

conn = psycopg2.connect(database="postgres", user = "postgres", password = "04120412", host = "127.0.0.1", port = "5433")

cur = conn.cursor()

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def my_form_post():
    ans = ''
    nft = request.form['text']
    cur.execute("select addres from INFO_FOR_NFT where addres = '"+nft+"'")
    if cur.fetchone() is None:
        url = f"https://solana-gateway.moralis.io/nft/mainnet/{nft}/metadata"
        headers = {
            "accept": "application/json",
            "X-API-Key": "S77RJTmiMoBbTQTEed5MExSDfHQ2HolnDEXy7GZRoo3Eah6t1YAR20dfdGIJASaT"
        } 
        response = requests.get(url, headers=headers)
        ans = response.text
        index = ans.find("name")
        index2 = 0
        for element in range(index+7, len(ans)):
            if ans[element] == '"':
                index2 = element
                break
        name = ans[index+7:index2]
        index = ans.find("metadataUri")
        index2 = 0
        for element in range(index+14, len(ans)):
            if ans[element] == '"':
                index2 = element
                break
        url = ans[index+14:index2]
        cur.execute(
            "INSERT INTO INFO_FOR_NFT (ADDRES,NAME,INF,URL) VALUES ('"+nft+"', '"+name+"', '"+response.text+"', '"+url+"')"
        )
        conn.commit()
        ans = 'Sorry, but we will enter this NFT sooner, try again'
        return render_template('index3.html')
        

    else:
        cur.execute("select inf from INFO_FOR_NFT where addres = '"+nft+"'")
        result = cur.fetchone()
        info = result[0]
        cur.execute("select url from INFO_FOR_NFT where addres = '"+nft+"'")
        result = cur.fetchone()
        url = result[0]
        cur.execute("select name from INFO_FOR_NFT where addres = '"+nft+"'")
        result = cur.fetchone()
        name = result[0]
        return render_template('index2.html', add = nft, n = name ,inf = info, u = url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

