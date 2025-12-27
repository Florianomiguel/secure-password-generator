import os
import random_password
from colorama import Fore, Style, init

init(autoreset=True)

def cleam_scream():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    cleam_scream()
    print(f"{'-'*30}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}PASSWORD MANAGER MENU")
    print(f"{'-'*30}")
    
    try:
        prompt = (f"Do you want to:\n"
                  f"{Fore.YELLOW}[1]{Fore.RESET} Create a new password\n"
                  f"{Fore.YELLOW}[2]{Fore.RESET} Check current password\n"
                  f"{Fore.RED}[0]{Fore.RESET} Exit\n"
                  f"{Fore.CYAN}Choose an option: ")     
        option = int(input(prompt))

        if option == 1:
            print(f"\n{Fore.YELLOW}Reminder: Passwords with fewer than 8 characters are rarely considered strong.")
            length_prompt = f"{Fore.GREEN}Enter the length you want: "
            length = int(input(length_prompt))
            random_password.generate_password(length)
            
            input(f"\n{Fore.CYAN}Press Enter to return to menu...")
            
        elif option == 2:
            pass_prompt = f"{Fore.GREEN}Enter your password to check: "
            user_password = input(pass_prompt).strip()
            random_password.try_level(user_password)
            
            input(f"\n{Fore.CYAN}Press Enter to return to menu...")
            
        elif option == 0:
            print(f"\n{Fore.LIGHTBLACK_EX}Exiting... Goodbye!")
            break  
            
        else:
            print(f"{Fore.RED}Invalid choice! Please enter 0, 1, or 2.")
            input(f"\n{Fore.CYAN}Press Enter to try again...")
            
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}ERROR! Please enter numbers only.")
        input(f"\n{Fore.CYAN}Press Enter to try again...")
