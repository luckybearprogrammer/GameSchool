import requests

urlServer = "https://0ca5-79-165-25-253.ngrok-free.app"


# Отправка числа в API для записи в файл
def send_number_to_api(number, iduser):
    url = f'{urlServer}/write_number'
    data = {'number': number, 'iduser': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response)
    if response.status_code == 200:
        print('Number has been sent to the API and written to the file')
    else:
        print('Failed to send the number to the API')


def can(iduser):
    url = f'{urlServer}/can'
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


def top():
    url = f'{urlServer}/top'
    response = requests.post(url)
    if response.status_code == 200:
        return response.json()["top"].split("lol")
    else:
        return "иди лесом"


def result(nick):
    data = {"nick": nick}
    response = requests.post(f"{urlServer}/myresult", json=data)
    if response.status_code == 200:
        return response.json()["result"]


def mesto(nick):
    data = {"iduser": nick}
    response = requests.post(f"{urlServer}/mesto", json=data)
    if response.status_code == 200:
        return response.json()["index"]
# send_number_to_api(1212348797213, "цувцуауц")
