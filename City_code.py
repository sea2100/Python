#1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.
import requests
import json

while True:

    search=input('Введите город (для выхода наберите: Exit ): \n')
    if search.lower()=='exit':
        break
    try:
        link='http://autocomplete.travelpayouts.com/places2?term='+search+'&locale=ru&types[]=city'
        data=json.loads(requests.get(link).text)
        print ('iata код города:',data[0]["code"])
    except:
        print('Sorry')


