#!/usr/bin/env python3

from models import Child, Parent
from models import Base, engine


Base.metadata.create_all(engine)


# Database
def seed_database():
    # Parents
    parent_one = Parent.add_parent(
        "Julius Lagat", "MaryAnn Cherotich", 254745665423, 458885686
    )

    # Children
    child_one = Child.add_child("Alvan Kibet", 23769, "2022-10-3")
    child_two = Child.add_child("Elvis Orinda", 23456, "2023-01-19")
    child_three = Child.add_child("Patience Mutua", 28721, "2021-8-12")
    child_four = Child.add_child("Kimberly Kemunto", 25896, "2022-01-31")
    child_five = Child.add_child("Joy Maina", 29031, "2020-04-22")
    child_six = Child.add_child("Andrew Karanja", 21189, "2022-11-05")


seed_database()
print("Seeded database")
