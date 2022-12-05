import requests
import send_message

API_KEY = "c83c15eeb2694775b3be60f34b779e65"
url1 = "https://finance.yahoo.com/"
url2 = f"https://newsapi.org/v2/top-headlines/sources?apiKey={API_KEY}&language=en"


request = requests.get(url2)
code = request.json()
list = code["sources"]

message = "News :" + 2 * "\n"

for i in range(len(list)):
    if list[i]["name"] and list[i]["description"] is not None:
        message = message + list[i]["name"] + "\n" + list[i]["description"] + 2 * "\n"


message = message.encode("utf-8")
send_message.send_email(message)

