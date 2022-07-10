import requests
API_KEY = "4fba7777a650143b8cc1e97b9df53cb2"
cidade = "rio de janeiro"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, temperatura)
