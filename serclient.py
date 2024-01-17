import requests
import asyncio


# Отправка числа в API для записи в файл
def send_number_to_api(number, iduser):
    url = 'https://2c7a-79-165-25-253.ngrok-free.app/write_number'
    data = {'number': number, 'iduser': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response)
    if response.status_code == 200:
        print('Number has been sent to the API and written to the file')
    else:
        print('Failed to send the number to the API')


def can(iduser):
    url = 'https://2c7a-79-165-25-253.ngrok-free.app/can'
    data = {'nick': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())
    if response.status_code == 200 and response.json()["can"]:
        return True
    elif response.status_code == 200:
        return False
    else:
        return False