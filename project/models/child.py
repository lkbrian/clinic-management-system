from sqlalchemy import Column, Integer, String, Date, ForeignKey, or_
from sqlalchemy.orm import relationship
from models import Base, session
from datetime import datetime, date


class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True, nullable=False)
    Fullname = Column(String, nullable=False)
    Certificate_No = Column(Integer, unique=True, nullable=False)
    Date_Of_Birth = Column(Date, nullable=False)
    Age = Column(String)
    parent_id = Column(Integer, ForeignKey("parents.National_ID"))
    parent = relationship("Parent", backref="children")

    def __init__(self, Fullname, Certificate_No, Date_Of_Birth, parent_id, Age=None):
        self.Fullname = Fullname
        self.Certificate_No = Certificate_No
        self.Date_Of_Birth = Date_Of_Birth
        self.Age = Age
        self.parent_id = parent_id

    def __repr__(self):
        return f"\nRegistered: {self.Fullname} of Age {self.Age} "

    @classmethod
    def calculate_age(cls, Date_Of_birth):
        if Date_Of_birth < date.today():
            birth_date = Date_Of_birth
            current_date = date.today()
            years = current_date.year - birth_date.year
            months = current_date.month - birth_date.month
            days = current_date.day - birth_date.day

            if months < 0 or (months == 0 and days < 0):
                years -= 1
                if months < 0:
                    months += 12
                else:
                    months = 11
                if days < 0:
                    days += 30

            weeks = days // 7
            days %= 7

            return years, months, weeks, days
        else:
            print("\033[91m Enter a past date \033[0m")

    @classmethod
    def add_child(cls, full_name, Certificate_No, Date_of_birth, parent_id):
        from models import Parent

        try:
            parent = session.query(Parent).filter_by(National_ID=parent_id).first()
            if parent:
                calculated_date = datetime.strptime(Date_of_birth, "%Y-%m-%d").date()

                years, months, weeks, days = cls.calculate_age(calculated_date)

                age = f"{years}y {months}m {weeks}w"
                child = cls(
                    Fullname=full_name,
                    Certificate_No=Certificate_No,
                    Date_Of_Birth=calculated_date,
                    Age=age,
                    parent_id=parent.National_ID,
                )
                session.add(child)
                session.commit()
                print(child)
                print("\033[92m Child registered successfully.\033[0m")
                return child
            else:
                print("\033[91m No Parernt with such Identification \33[0m")
        except Exception as error:
            session.rollback()
            print(f"\033[91m Error: {error} \033[0m")

    @classmethod
    def update_child(
        cls,
        Certificate=None,
        full_name=None,
        Date_of_birth=None,
        Changed_cert=None,
        parent_id=None,
        new_parent_id=None,
    ):
        from models import Parent

        try:
            # Check if the parent exists
            parent = session.query(Parent).filter_by(National_ID=new_parent_id).first()
            if not parent:
                print(
                    "\033[91mNew Parent not found. Please enter a valid Parent's National ID Number.\033[0m"
                )
                return

            # Update the child if it exists
            child = session.query(cls).filter_by(Certificate_No=Certificate).first()
            if child:
                if full_name:
                    child.Fullname = full_name
                if Date_of_birth:
                    calculated_date = datetime.strptime(
                        Date_of_birth, "%Y-%m-%d"
                    ).date()
                    years, months, weeks, days = cls.calculate_age(calculated_date)
                    age = f"{years}y {months}m {weeks}w"
                    child.Date_Of_Birth = calculated_date
                    child.Age = age
                if Changed_cert:
                    child.Certificate_No = Changed_cert
                if parent_id and parent_id != new_parent_id:
                    # Update the parent ID of the child
                    child.parent_id = new_parent_id

                session.commit()
                print("\033[92m Child updated successfully.\033[0m")
                print(
                    f"Updated:\nName to:{child.Fullname}\nDate of birth to: {child.Date_Of_Birth}\nCertificate No to: {child.Certificate_No}\nParent's ID to: {child.parent_id} \nNew Age: {child.Age} \033"
                )
                return child
            else:
                print(
                    "\033[91mNo child with such Certificate/Notification Number.\033[0m"
                )
        except Exception as error:
            session.rollback()
            print(f"\033[91mError: {error}\033[0m")

    @classmethod
    def find_child(cls, value):
        children = (
            session.query(cls)
            .filter(
                or_(
                    cls.Fullname == value,
                    cls.Certificate_No == value,
                    cls.parent_id == value,
                )
            )
            .all()
        )
        if children:
            [
                print(
                    f"{child.Fullname} Age {child.Age} Certificate no. {child.Certificate_No}"
                )
                for child in children
            ]
        else:
            print(f"No Record of {value} in the system")

    @classmethod
    def get_all_children(cls):
        try:
            chlidren = session.query(cls).all()
            if chlidren:
                print("All Children")
                # use of list expression
                [
                    print(f"\n Name {child.Fullname} of Age {child.Age} ")
                    for child in chlidren
                ]
            else:
                print("No children found.")
        except Exception as error:
            print("Error: ", error)
