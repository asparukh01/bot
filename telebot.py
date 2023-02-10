import requests
import pprint
from config import open_wether_token

def get_wether(city, open_wether_token):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_wether_token}')
        data = r.json()
        pprint(data)
    except Exception as ex:
        print(ex)
        print('Check city name')


def main():
    city = input('Enter city: ')
    get_wether(city, open_wether_token)


if __name__ == '__main__':
    main()
