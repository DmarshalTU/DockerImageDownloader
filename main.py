import os
from Docker.docker import docker
from welcome import welcome


def main():
    while True:
        os.system("clear")
        print(welcome("AXON"))
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
        os.system("clear")


if __name__ == "__main__":
    main()
