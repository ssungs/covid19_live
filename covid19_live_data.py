import requests


def Covid19_live_data():
    url = 'https://apiv2.corona-live.com/updates.json?timestamp=1613547340934'
    response = requests.get(url)
    covid19_live_data = response.json()
    return covid19_live_data
