import requests

params = {'username':'huababa','password':'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print("cookies is set to:")
print(r.cookies.get_dict())
print("-----------")
print("GOING TO profile page")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)
print(r.text)