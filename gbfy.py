import requests
import threading
uid = input("请输入uid:")
url = "https://cat-match.easygame2021.com/sheep/v1/game/user_info?uid="+uid+"&t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQzMjcyNDYsIm5iZiI6MTY2MzIyNTA0NiwiaWF0IjoxNjYzMjIzMjQ2LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo4MzU0MzAxNCwiZGVidWciOiIiLCJsYW5nIjoiIn0.5qpiRRjxwUmN1U8Qst8dFBMWMQyWi26DcfTgHIITZds&content-type=application%2Fjson&User-Agent=Mozilla%2F5.0%20(iPhone%3B%20CPU%20iPhone%20OS%2015_6%20like%20Mac%20OS%20X)%20AppleWebKit%2F605.1.15%20(KHTML%2C%20like%20Gecko)%20Mobile%2F15E148%20MicroMessenger%2F8.0.28(0x18001c26)%20NetType%2FWIFI%20Language%2Fzh_CN"
r = requests.get(url)
wx_open_id = r.json()['data']['wx_open_id']
url = "https://cat-match.easygame2021.com/sheep/v1/user/login_oppo?uid="+wx_open_id+"&avatar=1&nick_name=1&sex=1&t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQzMjcyNDYsIm5iZiI6MTY2MzIyNTA0NiwiaWF0IjoxNjYzMjIzMjQ2LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo4MzU0MzAxNCwiZGVidWciOiIiLCJsYW5nIjoiIn0.5qpiRRjxwUmN1U8Qst8dFBMWMQyWi26DcfTgHIITZds&content-type=application%2Fjson&User-Agent=Mozilla%2F5.0+(iPhone%3B+CPU+iPhone+OS+15_6+like+Mac+OS+X)+AppleWebKit%2F605.1.15+(KHTML%2C+like+Gecko)+Mobile%2F15E148+MicroMessenger%2F8.0.28(0x18001c26)+NetType%2FWIFI+Language%2Fzh_CN"
r = requests.post(url)
token = r.json()['data']['token']
url = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=0&rank_role=1&skin=1&t="+token+"&content-type=application%2Fjson&User-Agent=Mozilla%2F5.0%20(iPhone%3B%20CPU%20iPhone%20OS%2015_6%20like%20Mac%20OS%20X)%20AppleWebKit%2F605.1.15%20(KHTML%2C%20like%20Gecko)%20Mobile%2F15E148%20MicroMessenger%2F8.0.28(0x18001c26)%20NetType%2FWIFI%20Language%2Fzh_CN"
def request():
    for i in range(1000000):
        r = requests.get(url)
        print(r.json())
if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=request)
        t.start()
        
