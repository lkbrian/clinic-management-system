# interface.py
import fire

from helpers import (
    exit_program,
    Registration
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            fire.Fire(exit_program)
        elif choice == "1":
            Registration()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Registrations")


if __name__ == "__main__":
    main()