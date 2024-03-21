# interface.py
from interface_funcs import register_child, register_appointment, register_parent
import click
import sys


@click.group()
def userinterface():
    pass


userinterface.add_command(register_parent)
userinterface.add_command(register_child)
userinterface.add_command(register_appointment)


def Registration():
    while True:
        registration_menu()
        choice = click.prompt("Select a choice", type=int)
        if choice == 1:
            register_parent()
        elif choice == 2:
            register_child()
        elif choice == 3:
            register_appointment()
        elif choice == 4:
            sys.exit()
        else:
            click.echo("Invalid choice")


def Updates():
    while True:
        Updates_menu()
        choice = click.prompt("Please enter your choice", type=int)
        if choice == 1:
            register_parent()
        elif choice == 2:
            register_child()
        elif choice == 3:
            register_appointment()
        elif choice == 4:
            sys.exit()
        else:
            click.echo("Invalid choice")


def Find_Data():
    while True:
        registration_menu()
        choice = click.prompt("Please enter your choice", type=int)
        if choice == 1:
            register_parent()
        elif choice == 2:
            register_child()
        elif choice == 3:
            register_appointment()
        elif choice == 4:
            sys.exit()
        else:
            click.echo("Invalid choice")


def List_Data():
    while True:
        registration_menu()
        choice = click.prompt("Please enter your choice", type=int)
        if choice == 1:
            register_parent()
        elif choice == 2:
            register_child()
        elif choice == 3:
            register_appointment()
        elif choice == 4:
            sys.exit()
        else:
            click.echo("Invalid choice")


def consecutive_registration_action():
    click.echo("\nProceed to: ")
    click.echo("1. Registration menu")
    click.echo("2. Main menu")
    choice = click.prompt("Select a choice", type=int)

    if choice == 1:
        Registration()
    else:
        main()


def List_data_menu():
    click.echo("\nList Data Menu:")
    click.echo("1. Get All Parents")
    click.echo("2. Get All Children")
    click.echo("3. Get All Appointments")
    click.echo("4. Get All Unvaccinated")
    click.echo("5. Get All Vaccinated")
    click.echo("6. Return to Main Menu")


def Find_data_menu():
    click.echo("\nFind Data Menu:")
    click.echo("1. Find Parent")
    click.echo("2. Find Child")
    click.echo("3. Find Appointment")
    click.echo("4. Return to Main Menu")


def Updates_menu():
    click.echo("\nUpdates Menu:")
    click.echo("1. Update Parent")
    click.echo("2. Update Child")
    click.echo("3. Update Appointment")
    click.echo("4. Return to Main Menu")


def registration_menu():
    click.echo("\nRegistration Menu:")
    click.echo("1. Register Parent")
    click.echo("2. Register Child")
    click.echo("3. Register Appointment")
    click.echo("4. Return to Main Menu")


def main():
    while True:
        menu()
        choice = click.prompt("Please enter your choice", type=int)
        if choice == 1:
            Registration()
        elif choice == 5:
            click.echo("Get Better")
            sys.exit()
        else:
            print("Invalid choice")


def menu():
    click.echo("\nHappy Hearts Pediatric Center:")
    click.echo("1. Registrations")
    click.echo("2. Register Parent")
    click.echo("3. Register Child")
    click.echo("4. Register Appointment")
    click.echo("5. End Session")


if __name__ == "__main__":
    main()
