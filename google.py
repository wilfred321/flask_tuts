import requests

def main():

    API_KEY = "access_key=de93c2c03afac117dea9ca3eb291e4e5"
    url = "http://data.fixer.io/api/latest?"
    api_url = url + API_KEY
    res = requests.get(api_url)
    if res.status_code != 200:
        raise Exception("ERROR: API request Unsuccessful")
    data = res.json()
    rate = data
    print(rate)


if __name__ == "__main__":
    main()
