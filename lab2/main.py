import requests

s_city = 'Moscow, Ru'
appid = '8893c7496687e9083f71f231831bbb43'
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPIDЫЫ': appid})
data = res.json()

print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])

