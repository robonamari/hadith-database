import random

import requests  # pip install requests

request = random.choice(
    requests.get("https://hadith.robonamari.com/database.json").json()["texts"]
)

print(request["text"])
print(request["name"])
