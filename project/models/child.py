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

    @classmethod
    def add_child(cls, full_name, Certificate_No, Date_of_birth, parent_id):
        from models import Parent

        National_ID = session.query(Parent).filter_by(National_ID=parent_id).first()
        if National_ID:
            # Convert Date_of_birth string to Python date object
            calculated_date = datetime.strptime(Date_of_birth, "%Y-%m-%d").date()

            # Calculate age using Python date object
            years, months, weeks, days = cls.calculate_age(calculated_date)

            age = f"{years}y {months}m {weeks}w"
            child = cls(
                Fullname=full_name,
                Certificate_No=Certificate_No,
                Date_Of_Birth=calculated_date,  # Pass Python date object
                Age=age,
                parent_id=parent_id,
            )
            try:
                session.add(child)
                session.commit()
                print(child)
                return child
            except Exception as error:
                session.rollback()
                print(f"Error: {error}")
        else:
            print("The parent is not registered")

    @classmethod
    def find_child(cls, value):
        children = session.query(cls).filter(
            or_(cls.Fullname == value, cls.Certificate_No == value)
        ).all()
        if children:
            for child in children:
                print(f"{child.Fullname} Age {child.Age} Certificate no. {child.Certificate_No}")
        else:
            print(f"No Record of {value} in the system")

    @classmethod
    def update_child():
        pass

    @classmethod
    def get_all_children(cls):
        try:
            chlidren = session.query(cls).all()
            if chlidren:
                print("All Children")
                for child in chlidren:
                    print(child)
            else:
                print("No children found.")
        except Exception as error:
            print("Error: ",error)