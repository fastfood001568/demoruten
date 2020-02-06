#-*coding:utf-8-*
import codecs
import requests
import http.client
http.client._MAXHEADERS = 1000

ruten_url= "https://www.ruten.com.tw/"
headers={
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
response=requests.get(url=ruten_url,headers=headers)
data=response.content.decode("big5")
with codecs.open("ruten02.html","w",encoding='utf-8') as f:
        f.write(data)