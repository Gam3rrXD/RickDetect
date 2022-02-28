import ctypes
import time
import os
from pathlib import Path
import re
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
try:
	import requests
except ModuleNotFoundError:
	os.system("pip install requests")
from colorama import init
from colorama import Fore, Back, Style
init()
def login():
    os.system('cls')
    print(Fore.WHITE + """                          _____  _      _    _____       _            _   
                         |  __ \(_)    | |  |  __ \     | |          | |  
                         | |__) |_  ___| | _| |  | | ___| |_ ___  ___| |_ 
                         |  _  /| |/ __| |/ / |  | |/ _ \ __/ _ \/ __| __|
                         | | \ \| | (__|   <| |__| |  __/ ||  __/ (__| |_ 
                         |_|  \_\_|\___|_|\_\_____/ \___|\__\___|\___|\__|""")
    if os.path.exists("creds.rick"):
        user = Path('creds.rick').read_text()
        print("\nWelcome Back " + Fore.GREEN + user)
        time.sleep(3)
    else:
        user = input("\nUsername : ")
        if user == "Gam3rr" or "gam3rr":
            print(Fore.RED + "You Cant Choose The Developers Name LOL")
            login()
        with open('creds.rick', 'w') as f:
            f.write(user)
        print(Fore.GREEN + "Welcome " + user)
        time.sleep(3)
    main()
def main():
    user = Path('creds.rick').read_text()
    ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | By Gam3rr#0015 | Github Edition | Version 1.0/Alpha | User : " + user)
    os.system('cls')
    print(Fore.WHITE + """                          _____  _      _    _____       _            _   
                         |  __ \(_)    | |  |  __ \     | |          | |  
                         | |__) |_  ___| | _| |  | | ___| |_ ___  ___| |_ 
                         |  _  /| |/ __| |/ / |  | |/ _ \ __/ _ \/ __| __|
                         | | \ \| | (__|   <| |__| |  __/ ||  __/ (__| |_ 
                         |_|  \_\_|\___|_|\_\_____/ \___|\__\___|\___|\__|""")


    urll = input(Fore.WHITE + "Enter URL: ")
    aaa = requests.get(urll)
    print(aaa.text)
    time.sleep(1000)
    word = ["https://","http://","www.",".com", ".net", ".co.uk", '.org',".gg",".tech",".cs"]
    validity = bool(re.findall("|".join(word), urll, re.MULTILINE))
    if validity == True:
        real = requests.get(urll)
        if real.status_code in [200]:
            print(Fore.GREEN + urll + " is a VALID URL")
        else:
            print(Fore.RED + urll + "IS NOT A VALID URL!")
    if validity == False:
        print(Fore.RED + urll + ' IS NOT A VALID URL!')
        time.sleep(4)
        main()
    url = "https://pastebin.com/raw/UKCdAKFJ"
    req = requests.get(url)
    if req.status_code in [200]:
        html = req.text
    else: 
    	print("An Unknown Error Has Occurred")
    if os.path.exists("rd.rick"):
      os.remove("rd.rick")
    with open('rd.rick', 'w') as f:
        f.write(html)
    
    txt = Path('rd.rick').read_text()
    length = txt.count('\n')
    lines = txt.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    isitrick = any(rick in urll for rick in non_empty_lines)
    if isitrick == True:
        print(Fore.RED + urll + Fore.WHITE + ' is a Confirmed ' + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
        ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | RickRoll Detected From DB | By Gam3rr#0015 | Github Edition | Version 1.0/Alpha | User : " + user)
        time.sleep(3)
    if isitrick == False:
        source = str(requests.get(urll).content).lower()
        phrases = ["rickroll","rick roll","rick astley","never gonna give you up", "You can still view the page if you decline, but your experience may be impacted."]
        a = bool(re.findall("|".join(phrases), source, re.MULTILINE))
        if a == True:
            print(Fore.RED + urll + Fore.WHITE + ' is a Confirmed ' + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
            ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | RickRoll Detected | By Gam3rr#0015 | Github Edition | Version 1.0/Alpha | User : " + user)
            time.sleep(3)
        if a == False:
            print(Fore.GREEN + urll + Fore.WHITE + " is NOT a suspected " + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
            time.sleep(3)
    main()
login()