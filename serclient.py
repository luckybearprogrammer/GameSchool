import asyncio
import requests

urlServer = "https://0ca5-79-165-25-253.ngrok-free.app"


async def send_number_to_api(number, iduser):
    url = f'{urlServer}/write_number'
    data = {'number': number, 'iduser': iduser}
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: requests.post(url, json=data))
    print(response.status_code)
    if response.status_code == 200:
        print('Number has been sent to the API and written to the file')
    else:
        print('Failed to send the number to the API')


async def mesto(nick):
    data = {"iduser": nick}
    url = f"{urlServer}/mesto"
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: requests.post(url, json=data))
    print(response.status_code)
    if response.status_code == 200:
        result = response.json()
        print(result["index"])


async def main():
    await asyncio.gather(mesto("wkemefe"), send_number_to_api(9999999, "wkemefe"), mesto("wkemefe"))


asyncio.run(main())
