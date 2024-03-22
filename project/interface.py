# interface.py
from models import Parent, Child, Appointment
import click
import sys


@click.group()
def userinterface():
    pass


# Registration Commands
@click.command()
@click.option("--name", prompt="Enter Child's Fullname: ")
@click.option(
    "--cert_no", prompt="Enter Child's Certificate/Notification Number: ", type=int
)
@click.option("--d_o_b", prompt="Enter child's Date of Birth (YYYY-MM-DD): ")
@click.option("--parent_id", prompt="Enter the Parent's National ID Number: ", type=int)
def register_child(name, cert_no, d_o_b, parent_id):
    try:
        Child.add_child(name, cert_no, d_o_b, parent_id)
        click.echo("Child registered successfully.")

    except Exception as error:
        click.echo("Error during child registration: ", error)
    consecutive_registration_action()


@click.command()
@click.option("--father", prompt="Enter Father's Fullname: ")
@click.option("--mother", prompt="Enter Mother's Fullname: ")
@click.option(
    "--national_id", prompt="Enter the point parent's National ID Number: ", type=int
)
def register_parent(father, mother, national_id):
    try:
        Parent.add_parent(father, mother, national_id)
        click.echo("Parent registered successfully.")

    except Exception as error:
        click.echo("Error during parent registration: ", error)
    consecutive_registration_action()


@click.command()
@click.option("--child_name", prompt="Enter Child's Fullname: ")
@click.option("--parent_name", prompt="Enter Parent's Fullname: ")
@click.option("--vaccine", prompt="Enter Vaccine: ")
@click.option("--status", prompt="Enter Status: ")
@click.option("--doctor", prompt="Enter Doctor in Charge: ")
@click.option("--appointment_date", prompt="Enter Appointment Date (YYYY-MM-DD): ")
def register_appointment(
    child_name, parent_name, vaccine, status, doctor, appointment_date
):
    try:
        Appointment.set_appointment(
            child_name, parent_name, vaccine, status, doctor, appointment_date
        )
        click.echo("Appointment set successfully.")
    except Exception as error:
        click.echo("Error during appointment setting: ", error)


@click.command()
@click.option("--value", prompt="Enter Name of either Parents/National ID")
def find_parent(value):
    prompt = int(value) if value.isdigit() else str(value)
    try:
        Parent.find_parent(prompt)
    except Exception as e:
        print("Error: ", e)
    consecutive_find_data_action()

@click.command()
@click.option("--value", prompt="Enter The Childs Name/Certficate Number")
def find_child(value):
    prompt = int(value) if value.isdigit() else str(value)
    try:
        Child.find_child(prompt)
    except Exception as e:
        print("Errors: ", e)
    consecutive_find_data_action()

@click.command()
@click.option("--value", prompt = "Enter Appointment No/Child's Name/Parent Name/Doctor In Charge:" )
def find_appointment(value):
    prompt = int(value) if value.isdigit() else str(value)
    try:
        Appointment.find_appointment(prompt)
    except Exception as e:
        print("Error: ",e)
    consecutive_find_data_action()


userinterface.add_command(register_parent)
userinterface.add_command(register_child)
userinterface.add_command(register_appointment)
userinterface.add_command(find_parent)
userinterface.add_command(find_child)
userinterface.add_command(find_appointment)

def Registration():
    while True:
        registration_menu()
        choice = click.prompt("Select a choice: ", type=int)
        if choice == 1:
            register_parent()
        elif choice == 2:
            register_child()
        elif choice == 3:
            register_appointment()
        elif choice == 4:
            main()
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
        Find_data_menu()
        choice = click.prompt("Please enter your choice", type=int)
        if choice == 1:
            find_parent()
        elif choice == 2:
            register_child()
        elif choice == 3:
            register_appointment()
        elif choice == 4:
            main()
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


def consecutive_list_data_action():
    click.echo("\nProceed to: ")
    click.echo("1. List Data menu")
    click.echo("2. Main menu")
    choice = click.prompt("Select a choice", type=int)

    if choice == 1:
        Registration()
    elif choice == 2:
        main()
    else:
        click.echo("Invalid choice")


def consecutive_find_data_action():
    click.echo("\nProceed to: ")
    click.echo("1. Find Data menu")
    click.echo("2. Main menu")
    choice = click.prompt("Select a choice", type=int)

    if choice == 1:
        Find_Data()
    elif choice == 2:
        main()
    else:
        click.echo("Invalid choice")


def consecutive_updates_action():
    click.echo("\nProceed to: ")
    click.echo("\n1. Updates menu")
    click.echo("2. Main menu")
    choice = click.prompt("Select a choice", type=int)

    if choice == 1:
        Updates()
    elif choice == 2:
        main()
    else:
        click.echo("Invalid choice")


def consecutive_registration_action():
    click.echo("\nProceed to: ")
    click.echo("\n1. Registration menu")
    click.echo("2. Main menu")
    choice = click.prompt("Select a choice", type=int)

    if choice == 1:
        Registration()
    elif choice == 2:
        main()
    else:
        click.echo("Invalid choice")


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
        elif choice == 2:
            Updates()
        elif choice == 3:
            Find_Data()
        elif choice == 4:
            List_Data()
        elif choice == 5:
            click.echo("\033[92m Get Better Soon,We Are Happy To See You Leave\033[0m ")
            sys.exit()
        else:
            print("Invalid choice")


def menu():
    click.echo("\nHappy Hearts Pediatric Center:")
    click.echo("1. Registrations")
    click.echo("2. Updates")
    click.echo("3. Find Data")
    click.echo("4. List Data")
    click.echo("5. End Session")


if __name__ == "__main__":
    main()
