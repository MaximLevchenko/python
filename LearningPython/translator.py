import requests

# after post code>
# ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMU9UUTJOalU1TmpBc0lrMXZaR1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pNMk16SXNJbFZ1YVhGMVpVbGtJam9pTnpObE5UVTNPR1l0WW1FMk5TMDBaVGt3TFRoallXVXRZMlEzWWpWaVlUZ3hORGhsSW4xOS5YRjFoZDltQ2hGRkpKel96UXZ5TFNJcXhTZFpucklWeXppZ1R6NWJCVHBV
URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'NzNlNTU3OGYtYmE2NS00ZTkwLThjYWUtY2Q3YjViYTgxNDhlOjc4NDM0MDRmMjNmODRlMTc5MzJlNTRiNThhMGM4MGQy'  # key before post
headers_auth = {"Authorization": "Basic " + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
if auth.status_code == 200:
    token = auth.text
    while True:
        word = input("Enter your text")
        if word:
            headers_translate = {"Authorization": "Bearer " + token}
            params = {
                "text": word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('You are entering wrong symboles, try again')
else:
    print("You have a problem")

