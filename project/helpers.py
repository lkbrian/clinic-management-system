# helpers.py
from models import Child, Parent, Appointment


def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()


def Registration():

    Father = input("Enter Child's Fullname: ")
    Mother = input("Enter Mothers's Fullname: ")
    Nationalid = int(input("Enter the point parent's National ID Number: "))
    try:
        Parent.add_parent(Father, Mother, Nationalid)
    except Exception as error:
        print("Error during registration: ", error)

    name = input("Enter Child's Fullname: ")
    cert_no = int(input("Enter Child's Certificate/Notification Number: "))
    d_o_b = input("Enter child's Date of Birth(YYYY-MM-DD): ")
    parent_id = input("Enter the Parents's National ID Number: ")

    try:
        Child.add_child(name, cert_no, d_o_b, parent_id)
    except Exception as error:
        print("Error during registration: ", error)

    child_cert_no = int(input("Enter Child's Certificate/Notification Number: "))
    parent_id_number = int(input("Enter Parent's National ID Number: "))
    Vaccine = input("Enter Vaccine To Administer: ")
    Status = input("Enter Vaccination Status: ")
    Doctor_Incharge = input("Enter Doctor Incharge: ")
    Appointment_Date = input("Enter Appointment Date: ")

    try:
        Appointment.set_appointment(child_cert_no,parent_id_number,Vaccine,Status,Doctor_Incharge,Appointment_Date)
    except Exception as error:
        print("Error during registration: ", error)
