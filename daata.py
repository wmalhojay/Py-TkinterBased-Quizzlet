import requests

res = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
res.raise_for_status()
qAndA = res.json()["results"]