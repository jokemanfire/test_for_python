import requests

session = requests.session()

params = {'username':'hubaba','password':'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print(s.cookies.get_dict())
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)
