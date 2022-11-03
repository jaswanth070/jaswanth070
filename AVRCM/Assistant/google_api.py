import requests

request = requests.get('https://google.com/search?q=current+prime+minister+of+india')

# print(request.status_code)
print(request.content)