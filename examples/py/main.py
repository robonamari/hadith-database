import random

import requests  # pip install requests==2.32.3

request = random.choice(
    requests.get("https://hadith.robonamari.com/database.json").json()["texts"]
)

print(request["text"])
print(request["name"])
