import requests
# having a browser without the browser

# k animity
url = "https://api.pwnedpasswords.com/range/" + "CBFDA"

res = requests.get(url)
print(res)
