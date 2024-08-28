import time
import random
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def print_with_delay(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start_hacking():
    clear_line = '\r' + ' ' * 50 + '\r'
    print(Fore.GREEN + "Initializing...")
    time.sleep(2)
    print_with_delay(Fore.YELLOW + "Connecting to the target system...", 0.2)
    time.sleep(2)
    print_with_delay(Fore.CYAN + "Scanning network...", 0.2)
    time.sleep(2)

    for _ in range(5):
        print_with_delay(Fore.MAGENTA + "Accessing node: " + str(random.randint(1000, 9999)), 0.3)
        time.sleep(random.uniform(0.5, 1.5))
        print(clear_line, end='')

    print(Fore.GREEN + "Hacking attempt in progress...")
    time.sleep(3)
    print_with_delay(Fore.RED + "Error: Unauthorized access attempt detected!", 0.3)
    time.sleep(2)
    print_with_delay(Fore.RED + "Connection terminated.", 0.3)
    print(Fore.WHITE + "Operation complete.")

if __name__ == "__main__":
    start_hacking()
