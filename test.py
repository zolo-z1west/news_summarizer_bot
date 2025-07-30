import requests

api_key = "1f3123af79514b33a3a07cefac4fbf3d"
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
response = requests.get(url)
print(response.status_code)
print(response.json())