# helpers.py
from models import Child
def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def register_child():
    name = input("Enter Child's Fullname: ")
    cert_no  = int(input("Enter Child's Certificate Number: "))
    d_o_b = input("Enter child's Date of Birth(YYYY-MM-DD): ")

    try:
        Child.add_child(name,cert_no,d_o_b)        
    except Exception as error:
        print("Error during registration: ",error)


    