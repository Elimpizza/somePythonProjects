import requests
from time import sleep

base_url = "https://official-joke-api.appspot.com/jokes/"

print("One joke, or ten jokes? (1, 10)>")
num = input()

if num == "1":
    response = requests.get(base_url+"random")
else:
    response = requests.get(base_url+"ten")
if (response.status_code == 200):
    data = response.json()
    if (num == "1"):
        print(f"{data['setup']}")
        sleep(4)
        print(f"{data['punchline']}")
    else:
        for joke in data:
            print(f"{joke['setup']}")
            sleep(4)
            print(f"{joke['punchline']}\n")
            sleep(4)

