import requests
from time import sleep

url = "https://discord.com/api/webhooks/922985884549279774/_8IUCO-jT2EOND7ejKAkU0nkzvKAHnD-2JNoj3Rh9Xa8FuZzHe7IpesNRfAbgd3hvFKi"

while True:
    requests.post(url, {"content": "hey"})
    sleep(10)