from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from models.child import Child
from models.parent import Parent

from datetime import datetime, date


Base = declarative_base()





class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, nullable=False)
    Vaccine = Column(String, nullable=False)
    Appointment_Date = Column(Date, nullable=False)
    Doctor_Incharge = Column(String, nullable=False)
    Appointment_No = Column(Integer, unique=True, nullable=False)
    Child_ID = Column(Integer, ForeignKey("children.id"))
    Paren_ID = Column(Integer, ForeignKey("parents.id"))


class ClinicManagementSystem:
    def __init__(self, database):
        self.engine = create_engine(f"sqlite:///{database}")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_child(self, full_name, Certificate_No, Date_of_birth):
        Date_of_birth = datetime.strptime(Date_of_birth, "%Y-%m-%d").date()
        current_date = date.today()
        age = current_date.year - Date_of_birth.year
        child = Child(
            Fullname=full_name,
            Certificate_No=Certificate_No,
            Date_Of_Birth=Date_of_birth,
            Age=age,
        )
        try:
            self.session.add(child)
            self.session.commit()
            print("Child added succesfully")
            return child
        except Exception as e:
            self.session.rollback()
            print(f"Error:{e}")

    def add_parent(self, Fathersname, Mothersname, Mobile_No, National_ID):
        parent = Parent(
            Fathers_Name=Fathersname,
            Mothers_Name=Mothersname,
            Mobile_No=Mobile_No,
            National_ID=National_ID,
        )
        try:
            self.session.add(parent)
            self.session.commit()
            print("Added Parent succesfuly")
            return parent
        except Exception as e:
            self.session.rollback()
            print(f"Error:{e}")
