import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of experience that you want to test
payload = {
	'exp':"비가 오늘 날이다. 기분이 꿀꿀하다. 술이 생각난다."
}

#r = requests.post(url,json=payload)
r = requests.post(url, files = payload).json()
print( r )