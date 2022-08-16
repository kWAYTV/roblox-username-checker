import requests, os, threading, random, time
from colorama import Fore, Back, Style

clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
usernames = open('check.txt', 'r').read().split('\n')
clear()
count = 0
proxyDebug = False

def check():
    global count
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
                if "User not found" in r:
                    count +=1
                    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Free: " + user)
                    with open('free.txt', 'a') as f:
                        f.write(user + '\n')
                else:
                    count +=1
                    print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Taken: " + user)
                    with open('taken.txt', 'a') as f:
                        f.write(user + '\n')
                os.system(f"title Roblox Username Checker ^- Checked: " + str(count) + " ^- Remaining: " + str(len(usernames) - count))
        except Exception as e:
            print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Error: " + e)

clear()
try:
    check()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting.")
    time.sleep(1)
    exit()