# Coded by kWAY#1701
# Github: https://github.com/kWAYTV
# Discord: kWAY#1701

# Auto Import Installer
import os
try:
    import requests, os, threading, random, time, sys
    from colorama import Fore, Back, Style
    from pystyle import Colors, Colorate, Center
    print(f"\n{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Imports successful!")
    time.sleep(1)
except:
    print("\nImports failed! Trying to install...")
    z = "python -m pip install "; os.system('%srequests' % (z)); os.system('%scolorama' % (z)); os.system('%spystyle' % (z)); os.system('%sthreading' % (z)); os.system('%sos-sys' % (z)); os.system('%sthreading' % (z)); os.system('%srandom' % (z)); os.system('%stime' % (z))
    print(f"\n{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Imports successful!")
    time.sleep(1)

## Imports

import requests, os, threading, random, time, sys
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Center

# Variables
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
# create check.txt if it doesn't exist, if it does, read and split lines into users list
if not os.path.exists("check.txt"):
    with open("check.txt", "w") as f:
        f.write("")
else:
    with open("check.txt", "r") as f:
        users = f.read().splitlines()

count = 0
free = 0
taken = 0
error = 0
proxyDebug = False
proxyless = False
started = False
os.system(f"title Roblox Username Checker - Starting...")
clear()


# Vanity Generator Logo
logo = """
██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝"""

# Prints the logo
def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

# Checker
def check():
    global count, free, taken, error, proxyDebug, proxyLess
    session = requests.Session()
    while True:
        for line in users: 
            if len(line) < 3:
                print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}] {Fore.RED}{line}{Fore.RESET} is too short! Skipping...")
                continue
            if len(line) > 20:
                print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}] {Fore.RED}{line}{Fore.RESET} is too long! Skipping...")
                continue
            if proxyless == True:
                r = requests.get(f"https://api.roblox.com/users/get-by-username?username={line}").text
                if proxyDebug == True:
                    print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.MAGENTA}{proxyDict}{Fore.RESET}")
                else:
                    pass
            elif proxyless == False:
                proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
                r = requests.get(f"https://api.roblox.com/users/get-by-username?username={line}", proxies=proxyDict).text
                r = str(r)
                if proxyDebug == True:
                    print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.MAGENTA}{proxyDict}{Fore.RESET}")
                else:
                    pass
            count += 1
            if "User not found" in r:
                free += 1
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Free: {Fore.GREEN}" + line + f"{Fore.RESET}")
                with open('free.txt', 'a') as f:
                    f.write(line + '\n')
            else:
                taken += 1
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Taken: {Fore.RED}" + line + f"{Fore.RESET}")
                with open('taken.txt', 'a') as f:
                    f.write(line + '\n')
            if proxyless == True:
                os.system(f"title Roblox Username Checker - Status: {count}/{len(users)} - Free: {free} - Taken: {taken} - Error: {error} - Mode: Proxyless [WARNING]")
            elif proxyless == False:
                os.system(f"title Roblox Username Checker - Status: {count}/{len(users)} - Free: {free} - Taken: {taken} - Error: {error} - Using proxy: {proxyDict}")

# Start the tool
clear()
printLogo()
try:
    if os.stat("check.txt").st_size == 0:
        clear()
        print(f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}] {Fore.RESET}No usernames in check.txt! Exiting...")
        os.system(f"title Roblox Username Checker - check.txt is empty! Exiting...")
        time.sleep(1)
        sys.exit()
    print(f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}] {Fore.RESET}Found {Fore.YELLOW}{len(users)}{Fore.RESET} accounts to check.")
    print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Do you want to use a proxy?")
    print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}1.{Fore.GREEN} Yes{Fore.RESET}")
    print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}2.{Fore.RED} No{Fore.RESET}")
    proxyChoice = input(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Choice: ")
    if proxyChoice == "1":
        proxyless = False
        print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Using a proxy")
    elif proxyChoice == "2":
        proxyless = True
        print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Not using a proxy")
    if proxyless == False and not os.path.exists("proxies.txt"):
        with open("proxies.txt", "w") as f:
            f.write("")
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} proxies.txt does not exist! Exiting...")
        os.system(f"title Roblox Username Checker - proxies.txt does not exist! Exiting...")
        time.sleep(1)
        sys.exit()
    elif proxyless == False and os.path.exists("proxies.txt"):
        if os.stat("proxies.txt").st_size == 0:
            clear()
            print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}] {Fore.RESET}No proxies in proxies.txt! Exiting...")
            os.system(f"title Roblox Username Checker - proxies.txt is empty! Exiting...")
            time.sleep(1)
            sys.exit()
        else:
            print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Do you want to use proxy debug?")
            print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}1.{Fore.GREEN} Yes{Fore.RESET}")
            print(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}2.{Fore.RED} No{Fore.RESET}")
            proxyDebugChoice = input(f"{Fore.MAGENTA}[{Fore.RESET}?{Fore.MAGENTA}] {Fore.RESET}Choice: ")
            if proxyDebugChoice == "1":
                proxyDebug = True
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Using proxy debug")
            elif proxyDebugChoice == "2":
                proxyDebug = False
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Not using proxy debug")
    elif proxyless == True:
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}] {Fore.RESET}Starting the tool with proxyless mode. Be aware of your ip.")
        time.sleep(0.5)
        pass
    while True:
        check()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting. If it keeps, just close the program.")
    os.system(f"title Roblox Username Checker - Exiting. If it keeps, just close the program.")
    time.sleep(1)
    exit()