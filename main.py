#ciphersec 

import ipinfo
from colorama import Fore, init

init(autoreset=True)

ip_address = input(Fore.YELLOW + "Enter the IP address: ")
access_token = "access_token_id"  #add token id from https://ipinfo.io/

handler = ipinfo.getHandler(access_token)
details = handler.getDetails(ip_address)

def banner():
    RED = "\33[91m"
    BLUE = "\33[94m"
    GREEN = "\033[32m"
    YELLOW = "\033[93m"
    PURPLE = '\033[0;35m' 
    CYAN = "\033[36m"
    END = "\033[0m"
    font = """
   _____ _____ _____  _    _ ______ _____   _____ ______ _____ 
  / ____|_   _|  __ \| |  | |  ____|  __ \ / ____|  ____/ ____|
 | |      | | | |__) | |__| | |__  | |__) | (___ | |__ | |     
 | |      | | |  ___/|  __  |  __| |  _  / \___ \|  __|| |     
 | |____ _| |_| |    | |  | | |____| | \ \ ____) | |___| |____ 
  \_____|_____|_|    |_|  |_|______|_|  \_\_____/|______\_____|
                                                               
                                                               
"""
    print(font)

if __name__ == "__main__":
    banner()
    print(Fore.RESET + " ")

    print(Fore.RESET + f"IP: {details.ip}")
    print(Fore.RESET + f"City: {details.city}")
    print(Fore.RESET + f"Region: {details.region}")
    print(Fore.RESET + f"Country: {details.country}")
    print(Fore.RESET + f"Coordinates: {details.loc}")

    while True:
        response = input(Fore.YELLOW + "Do you want to see more information? (y/n) ").lower()

        if response == "y":
            print(Fore.RESET + "")

            print(Fore.RESET + f"Postal Code: {details.postal}")
            print(Fore.RESET + f"Timezone: {details.timezone}")
            print(
                Fore.RESET + f"Google Maps: https://www.google.com/maps/@{details.loc}"
            )
            print(Fore.RESET + f"Detailed Information: https://ipinfo.io/{details.ip}")
            print(Fore.RESET + " ")
            break
        elif response == "n":
            print(Fore.RESET + " ")
            break
        else:
            print(Fore.RED + "Please enter y or n.")
