import requests

share_url = "https://v.douyin.com/JcpmyPt/"
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
r = requests.get(share_url,headers)
# 获取ID
item_ids =r.url.split("/?")[0].split("video/")[1]

base_url='https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+item_ids

res=requests.get(base_url,headers)
# 获取无水印下载链接
play_addr = res.json()["item_list"][0]["video"]["play_addr"]["url_list"][0].replace("playwm","play")

video = requests.get(play_addr,headers)

with open(item_ids+".mp4","wb") as f:
    f.write(video.content)
    f.close()