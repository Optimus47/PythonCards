import requests, json
import ssl
print(ssl.OPENSSL_VERSION)

response = requests.get("https://api.github.com")
print(response.status_code)
# print(response.json())

parsed = json.loads(response.text)
# for key, value in parsed.items():
    # print(f"{key}:\n\t {value}")

params = {"q": "python"}
r = requests.get("https://www.google.com/search", params=params)
print(r.url)
print(r.status_code)
print(r.text)