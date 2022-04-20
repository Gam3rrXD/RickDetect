import ctypes
import time
import os
from pathlib import Path
import re
import subprocess
user = "NewUser"
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
"""
MIT License

Copyright (c) 2022 Gam3rr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def login():
    ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | By Gam3rr#0015 | Github Edition | Version 2 | Login")
    os.system('cls')
    print(Fore.WHITE + """                          _____  _      _    _____       _            _   
                         |  __ \(_)    | |  |  __ \     | |          | |  
                         | |__) |_  ___| | _| |  | | ___| |_ ___  ___| |_ 
                         |  _  /| |/ __| |/ / |  | |/ _ \ __/ _ \/ __| __|
                         | | \ \| | (__|   <| |__| |  __/ ||  __/ (__| |_ 
                         |_|  \_\_|\___|_|\_\_____/ \___|\__\___|\___|\__|""")
    if os.path.exists("creds.rick"):
        user = Path('creds.rick').read_text()
        if "gam3rr" in user.lower():
            print(Fore.RED + "Imagine Trying To Edit The File To Get The Developers Name")
            os.remove("creds.rick")
            time.sleep(2)
            login()
        else:
            print("\nWelcome Back " + Fore.GREEN + user)
            time.sleep(3)
            menu()
    else:
        user = input("\nUsername: ")
        if "gam3rr" in user.lower():
            print(Fore.RED + "Imagine Trying To Get The Developers Name")
            if os.path.exists("creds.rick"):
                os.remove("creds.rick")
            time.sleep(2)
            login()
        else:
            with open('creds.rick', 'w') as f:
                f.write(user)
            print(Fore.WHITE + "Welcome " + Fore.GREEN + user)
            time.sleep(3)
            menu()

def setting():
        os.system('cls')
        user = Path('creds.rick').read_text()
        cmd = 'wmic csproduct get uuid'
        uuid = str(subprocess.check_output(cmd))
        pos1 = uuid.find("\\n")+2
        uuid = uuid[pos1:-15]
        ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)
        print(Fore.WHITE + """                          _____  _      _    _____       _            _   
                         |  __ \(_)    | |  |  __ \     | |          | |  
                         | |__) |_  ___| | _| |  | | ___| |_ ___  ___| |_ 
                         |  _  /| |/ __| |/ / |  | |/ _ \ __/ _ \/ __| __|
                         | | \ \| | (__|   <| |__| |  __/ ||  __/ (__| |_ 
                         |_|  \_\_|\___|_|\_\_____/ \___|\__\___|\___|\__|""")
        print("Username: " + Fore.GREEN +  user)
        print(Fore.WHITE + "Version: " + Fore.CYAN + "2")
        print(Fore.WHITE + "HWID: " + Fore.BLUE +  uuid)
        print(Fore.WHITE + "Created By:" + Fore.RED + " Gam3rr#0015")
        print(Fore.WHITE + "Edition: " + Fore.LIGHTGREEN_EX + "Github")
        print(Fore.WHITE + "[S] " + Fore.RED + "Sign Out")
        print(Fore.WHITE + "[X] " + Fore.GREEN + "Go Back")
        a1 = input(Fore.WHITE + "Option: ").lower()
        if a1 == "x":
            menu()
        if a1 == "s":
            os.remove("creds.rick")
            print("Signed Out!")
            time.sleep(3)
            login()
        else:
            print(Fore.RED + "Invalid Option!")
            time.sleep(3)
            setting()
def menu():
    user = Path('creds.rick').read_text()
    ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)
    os.system('cls')
    print(Fore.WHITE + """                          _____  _      _    _____       _            _   
                         |  __ \(_)    | |  |  __ \     | |          | |  
                         | |__) |_  ___| | _| |  | | ___| |_ ___  ___| |_ 
                         |  _  /| |/ __| |/ / |  | |/ _ \ __/ _ \/ __| __|
                         | | \ \| | (__|   <| |__| |  __/ ||  __/ (__| |_ 
                         |_|  \_\_|\___|_|\_\_____/ \___|\__\___|\___|\__|""")
    print("[1] Single URL")
    print("[2] Multi URL")
    print("[3] Settings")
    print("[X] Exit")
    menua = input(Fore.GREEN + "Option : ")
    if menua == "1":
        main()
    if menua == "2":
        multi()
    if menua == "3":
        setting()
    if menua == "x":
        exit()
    else:
        print(Fore.RED + "Invalid Option!")
        time.sleep(3)
        menu()

def main():
    user = Path('creds.rick').read_text()
    ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)
    os.system('cls')
    print(Fore.WHITE + """                          _____  _      _    _____       _            _   
                         |  __ \(_)    | |  |  __ \     | |          | |  
                         | |__) |_  ___| | _| |  | | ___| |_ ___  ___| |_ 
                         |  _  /| |/ __| |/ / |  | |/ _ \ __/ _ \/ __| __|
                         | | \ \| | (__|   <| |__| |  __/ ||  __/ (__| |_ 
                         |_|  \_\_|\___|_|\_\_____/ \___|\__\___|\___|\__|""")
    urll = input(Fore.WHITE + "Enter URL: ")
    word = ["https://","http://","www.",".com", ".net", ".co.uk", '.org',".gg",".tech",".cs",".ly",".st", "."]
    validity = bool(re.findall("|".join(word), urll, re.MULTILINE))
    which = ""
    if validity == True:
            try:
                real = requests.get(urll)
                if real.status_code in [200]:
                    print(Fore.GREEN + urll + " is a VALID URL")
                    which = "N"
                else:
                    url2 = "https://" + urll
                    url3 = "http://" + urll
                    try:
                        new1 = requests.get(url2)
                        if new1.status_code in [200]:
                            print(Fore.GREEN + new1.url + " is a VALID URL")
                            which = "O"
                        else:
                            new2 = requests.get(url3)
                            if new2.status_code in [200]:
                                print(Fore.GREEN + new2.url + " is a VALID URL")
                                which = "T"
                            else:
                                print(Fore.RED + urll + " IS NOT A VALID URL!")
                                time.sleep(3)
                                menu()
                    except:
                        url3 = "http://" + urll
                        new2 = requests.get(url3)
                        if new2.status_code in [200]:
                            print(Fore.GREEN + new2.url + " is a VALID URL")
                            which = "T"
                        else:
                            print(Fore.RED + urll + " IS NOT A VALID URL!")
                            time.sleep(3)
                            menu()
                    
                    
            except:
                    url2 = "https://" + urll
                    url3 = "http://" + urll
                    try:
                        new1 = requests.get(url2)
                        if new1.status_code in [200]:
                            print(Fore.GREEN + new1.url + " is a VALID URL")
                            which = "O"
                        else:
                            new2 = requests.get(url3)
                            if new2.status_code in [200]:
                                print(Fore.GREEN + new2.url + " is a VALID URL")
                                which = "T"
                            else:
                                print(Fore.RED + urll + " IS NOT A VALID URL!")
                                time.sleep(3)
                                menu()
                    except:
                        url3 = "http://" + urll
                        new2 = requests.get(url3)
                        if new2.status_code in [200]:
                            print(Fore.GREEN + new2.url + " is a VALID URL")
                            which = "T"
                        else:
                            print(Fore.RED + urll + " IS NOT A VALID URL!")
                            time.sleep(3)
                            menu()
                
                
    if validity == False:
        print(Fore.RED + urll + ' IS NOT A VALID URL!')
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
        ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | RickRoll Detected From DB | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)
        time.sleep(3)
    if isitrick == False:
        if which == "N":
            ve = requests.get(urll)
            source = str(requests.get(ve.url).content).lower()
        if which == "O":
            ve = requests.get(url2)
            source = str(requests.get(ve.url).content).lower()
        if which == "T":
            ve = requests.get(url3)
            source = str(requests.get(ve.url).content).lower()
        phrases = ["rickroll","rick roll","rick astley","never gonna give you up", "You can still view the page if you decline, but your experience may be impacted."]
        a = bool(re.findall("|".join(phrases), source, re.MULTILINE))
        if a == True:
            print(Fore.RED + ve.url + Fore.WHITE + ' is a Confirmed ' + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
            ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | RickRoll Detected | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)

            time.sleep(3)
        if a == False:
            print(Fore.GREEN + ve.url + Fore.WHITE + " is NOT a suspected " + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
            time.sleep(3)
    menu()
def multi():
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
    user = Path('creds.rick').read_text()
    ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)
    os.system('cls')
    print(Fore.WHITE + """                          _____  _      _    _____       _            _   
                         |  __ \(_)    | |  |  __ \     | |          | |  
                         | |__) |_  ___| | _| |  | | ___| |_ ___  ___| |_ 
                         |  _  /| |/ __| |/ / |  | |/ _ \ __/ _ \/ __| __|
                         | | \ \| | (__|   <| |__| |  __/ ||  __/ (__| |_ 
                         |_|  \_\_|\___|_|\_\_____/ \___|\__\___|\___|\__|""")
    urll = input(Fore.WHITE + "Drop URL File: ")
    file1 = open(urll, 'r')
    Lines = file1.readlines()
    for urla in Lines:
        word = ["https://","http://","www.",".com", ".net", ".co.uk", '.org',".gg",".tech",".cs"]
        validity = bool(re.findall("|".join(word), urla, re.MULTILINE))
        if validity == True:
            try:
                real = requests.get(urla)
                if real.status_code in [200]:
                    print()
                else:
                    print(Fore.RED + real.url + " IS NOT A VALID URL!")
            except:
                print(Fore.RED + real.url + " IS NOT A VALID URL")    
        if validity == False:
            print(Fore.RED + urla + ' IS NOT A VALID URL!')
            
        txt = Path('rd.rick').read_text()
        length = txt.count('\n')
        lines = txt.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        isitrick = any(rick in urla for rick in non_empty_lines)
        if isitrick == True:
            print(Fore.RED + real.url + Fore.WHITE + ' is a Confirmed ' + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
            ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | RickRoll Detected From DB | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)
            
        if isitrick == False:
            source = str(requests.get(real.url).content).lower()
            phrases = ["rickroll","rick roll","rick astley","never gonna give you up", "You can still view the page if you decline, but your experience may be impacted.", "roll rick", "astley roll", "Wreck Roll"]
            a = bool(re.findall("|".join(phrases), source, re.MULTILINE))
            if a == True:
                print(Fore.RED + real.url + Fore.WHITE + ' is a Confirmed ' + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
                ctypes.windll.kernel32.SetConsoleTitleW("RickDectect | RickRoll Detected | By Gam3rr#0015 | Github Edition | Version 2 | User : " + user)
                
            if a == False:
                print(Fore.GREEN + real.url + Fore.WHITE + " is NOT a suspected " + Fore.RED + 'R' + Fore.GREEN + 'i' + Fore.BLUE + 'c' + Fore.CYAN + 'k ' + Fore.MAGENTA + 'R' + Fore.YELLOW + 'o' + Fore.GREEN + 'l' + Fore.BLUE + 'l')
    time.sleep(3)            
    menu()
login()
