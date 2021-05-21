import sys
import requests
from colorama import Fore
import os

"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN


        creat by Amir Hossein Tadas & TAHA
"""


def __start__():
    try:
        print(Fore.RED+"\n [!] Plase Enter IP/Domain")
        print(Fore.RED+"\n [!] for exampel : test.com\n")

        inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"/"+Fore.WHITE+"Get-web-information"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Whois"+Fore.RED+"""]
 └─╼ """+Fore.WHITE+">> ")
        result = requests.get(
            'http://api.hackertarget.com/whois/?q=' + inp).text

        print(Fore.BLUE+result)
        try:
            input(Fore.RED+" [!] "+Fore.GREEN +
                  "Back To start again (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print("\nExit :)")


if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()
