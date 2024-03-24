#!/usr/bin/env python3

from models import Child, Parent,Appointment
from models import Base, engine


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# Database
def seed_database():

    # Parents
    parent_one = Parent.add_parent("Julius Lagat", "MaryAnn Cherotich", 426725)
    parent_two = Parent.add_parent("Benjamin Odhiambo", "Rachel Asus", 4747346)
    parent_three = Parent.add_parent("James Kimani", "Jeniffer Maina", 4126468)
    parent_four = Parent.add_parent("Dennis Wafula", "Whitney Hadassa", 3874728)
    parent_five = Parent.add_parent("Ali Noor", "Fatuma Aisha", 3216468)
    parent_six = Parent.add_parent("Abraham Karanja", "Anastasia Wanjiku", 5674728)


    # # Children
    child_one = Child.add_child("Alvan Kibet", 23769, "2022-10-3",parent_one.National_ID)
    child_two = Child.add_child("Kelvin Cheruiyot", 22469, "2022-10-3",parent_one.National_ID)
    child_three = Child.add_child("Anthony Otieno", 23464, "2022-09-26",parent_two.National_ID)
    child_four = Child.add_child("Elvis Orinda", 29045, "2022-09-26",parent_two.National_ID)
    child_five = Child.add_child("Abraham Macharia", 23749, "2022-10-3",parent_three.National_ID)
    child_six = Child.add_child("Simon Wanyonyi", 21387, "2022-10-3",parent_four.National_ID)
    child_seven = Child.add_child("Mohamed Abdikadir", 24575, "2022-09-26",parent_five.National_ID)
    child_eight = Child.add_child("Abraham Macharia", 287456, "2020-02-12",parent_six.National_ID)


    # # child_two = Child.add_child("Elvis Orinda", 23456, "2023-01-19")
    Appointment.set_appointment(child_one.Certificate_No,parent_one.National_ID,"Influenza (flu)","Unvaccinated","Dr.Clarence Opondo","2024-04-10")
    Appointment.set_appointment(child_two.Certificate_No,parent_one.National_ID,"Influenza (flu) ","Unvaccinated","Dr.james Gitau","2024-04-10")
    Appointment.set_appointment(child_three.Certificate_No,parent_two.National_ID,"Measles,polio","Unvaccinated","Dr.Philomena Siprosa ","2024-05-20")
    Appointment.set_appointment(child_four.Certificate_No,parent_two.National_ID,"Measles,polio","Unvaccinated","Dr.Ann Maina","2024-06-01")
    Appointment.set_appointment(child_five.Certificate_No,parent_three.National_ID,"polio","vaccinated","Dr.Beatrice Nabwire","2024-03-25")
    Appointment.set_appointment(child_six.Certificate_No,parent_four.National_ID,"Measles","Unvaccinated","Dr.Clarence Opondo","2024-05-20")

    # Appointment.vaccinate(child_eight.Certificate_No)
    # Appointment.vaccinate(21387)

    # Appointment.find_appointment("Dr.Clarence Opondo")
    # Appointment.find_appointment(1429)

    # Child.find_child("Abraham Macharia")
    # Child.find_child(22469)

    # Appointment.get_vaccinated()
    # Appointment.get_unvaccinated()

    Appointment.get_all_appointments()



seed_database()
print("Seeded database")
