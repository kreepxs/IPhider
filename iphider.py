import os
import time
import random
import socket

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_console()
    print("*************************************")
    print("            IPhider                  ")
    print("        made by kreepxs              ")
    print("*************************************")

def change_ip():
    
    new_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    print(f"Seu novo IP é: {new_ip}")

def main():
    print_banner()
    try:
        interval = int(input("Escolha o tempo de mudança (em segundos): "))
        while True:
            change_ip()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
