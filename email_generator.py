from bs4 import BeautifulSoup
import requests
import time
import os

def getEmail():
	URL_Email = "https://10minutemail.net/"
	email_page = requests.get(URL_Email)
	handle_email = BeautifulSoup(email_page.content, 'html.parser')
	email = handle_email.find(class_='div-m-0 text-c')
	email = str(email)[84:].replace("\"/></div>", '')
	return email

def clear(): 
	if os.name == 'nt':
		os.system('cls') 
	else:
		os.system('clear')

def banner():
	clear()
	print("""
 _____                 _ _    ____                           _             
| ____|_ __ ___   __ _(_) |  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  _| | '_ ` _ \\ / _` | | | | |  _ / _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|
| |___| | | | | | (_| | | | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_____|_| |_| |_|\\__,_|_|_|  \\____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   
		""")
	print("\t\t\tDeveloped by @TheFlash2k\n\n")

def writeToFile(email):
	file = open("emails.txt", 'a')
	write = ''
	write += email + '\n'
	file.write(write)
	file.close()

def main():
	banner()
	try:
		numEmails = int(input("[+] Enter the number of emails you want to create: "))
	except:
		print("[!] Invalid Value Entered. Restarting in 2 secs...")
		time.sleep(2)
		main()
	writeOrNot = str(input("[+] Do you want to save to a file or not? (Y/N): "))
	write = False
	if 'y' == writeOrNot[0].lower():
		write = True
	if write == True:
		print("[*] Writing to file has been enabled!")
	print("[*] Creating {} emails".format(numEmails))
	try:
		for x in range(numEmails):
			email = getEmail()
			if '@' not in email:
				print("""
					[!] YOUR IP HAS BEEN BANNED BY 10MINUTEMAIL.NET.
						PLEASE CHANGE IP USING A VPN OR RESTART YOUR ROUTER.
					""")
				break
			else:
				if write == True:
					writeToFile(email)
				print("Email number {} : {}".format(x+1, email))
	except:
		print("Exiting...")
		exit()
if __name__ == "__main__":
	main()
