import requests

response = requests.post("https://playground.learnqa.ru/api/show_all_headers")

# Заголовки которые сервер получил от клиента
print(response.text)
"""
{
   "result":{
      "Host":"playground.learnqa.ru",
      "Port":"443",
      "X-Forwarded-For":"5.35.22.169",
      "X-Real-IP":"5.35.22.169",
      "X-Forwarded-Port":"443",
      "X-MH-Host":"playground.learnqa.ru",
      "MH_GEOIP_COUNTRY_CODE":"RU",
      "Content-Length":"0",
      "User-Agent":"python-requests\/2.26.0",
      "Accept-Encoding":"gzip, deflate",
      "Accept":"*\/*"
   }
}
"""
# Заголовки ответа сервера на запрос с заголовками напечатанами выше
print(response.headers)
"""
{
   "Date":"Sat, 01 Jan 2022 00:29:29 GMT",
   "Content-Type":"application/json",
   "Transfer-Encoding":"chunked",
   "Connection":"keep-alive",
   "Keep-Alive":"timeout=10",
   "Vary":"Accept-Encoding",
   "Server":"Apache",
   "Cache-Control":"max-age=0",
   "Expires":"Sat, 01 Jan 2022 00:29:29 GMT",
   "Content-Encoding":"gzip"
}
"""