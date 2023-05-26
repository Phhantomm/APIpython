import requests
import json
request = requests.get('https://openweathermap.org')
print(request)
print(request.status_code)
print(request.headers)
city = 'Telavi'
key = '887aaff89bee4fd742287bfd4afa2483'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
ha = requests.get(url)
r=json.loads(ha.text)
print(json.dumps(r, indent=5))
print("ტემპერატურა იგრძნობა: ", r['main']['feels_like'])
print("ქარის სისწრაფე: ", r['wind']['speed'])
print("ტენიანობა: ", r['main']['humidity'])
with open('weather.json', 'w') as file:
    file.write(f'{request.status_code}')