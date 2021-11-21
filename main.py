import os
from Docker.docker import docker
from welcome import welcome
import subprocess
import platform


def clear_screen():
    os_name=platform.system().lower()
    if os_name=="linux":
        subprocess.run("clear",shell=True)
    elif os_name=="windows":
        subprocess.run("cls",shell=True)

def main():
    while True:
        clear_screen()
        print(welcome("Denni TU - CodeWizard"))
        print("\nChoose service you want to use : ")
        print("""
        1 : Docker
        0 : Exit
        """
              )
        choice = input("\nEnter your choice : ")

        if choice == '1':
            docker()
        elif choice == '0':
            exit()
        clear_screen()


if __name__ == "__main__":
    main()
