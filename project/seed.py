#!/usr/bin/env python3

from models import Child, Parent, Appointment, ClinicManagementSystem

#Database
happy_hearts = ClinicManagementSystem("afyabora.db")

#Parents
parent_one= happy_hearts.add_parent("Julius Lagat","MaryAnn Cherotich",254745665423,458885686)


#Children
child_one = happy_hearts.add_child("Alvan Kibet", 23769, "2022-10-3")
child_two = happy_hearts.add_child("Elvis Orinda", 23456, "2023-01-19")
child_three = happy_hearts.add_child("Patience Mutua", 28721, "2021-8-12")
child_four = happy_hearts.add_child("Kimberly Kemunto", 25896, "2022-01-31")
child_five = happy_hearts.add_child("Joy Maina", 29031, "2020-04-22")
child_six = happy_hearts.add_child("Andrew Karanja", 21189, "2022-11-05")
