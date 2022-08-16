import requests, os, threading, random, time
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Center

clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
usernames = open('check.txt', 'r').read().split('\n')
clear()
count = 0
free = 0
taken = 0
error = 0
proxyDebug = False

# Vanity Generator Logo
logo = """
██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝"""

def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

def check():
    global count, free, taken, error
    while True:
        try:
            for user in usernames:
                proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
                if proxyDebug == True:
                    print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.GREEN}{proxyDict}{Fore.RESET}")
                else:
                    pass
                r = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}", proxies=proxyDict).text
                r = str(r)
                count += 1
                if "User not found" in r:
                    free += 1
                    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Free: " + user)
                    with open('free.txt', 'a') as f:
                        f.write(user + '\n')
                else:
                    taken += 1
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Taken: " + user)
                    with open('taken.txt', 'a') as f:
                        f.write(user + '\n')
                os.system(f"title Roblox Username Checker - Status: {count}/{len(usernames)} - Free: {free} - Taken: {taken} - Error: {error}")
        except Exception as e:
            print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Error: " + str(e))
            error += 1
            continue

clear()
printLogo()
try:
    check()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting.")
    time.sleep(1)
    exit()