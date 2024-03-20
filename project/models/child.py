from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.orm import relationship
from models import Base,session
from datetime import datetime, date


class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True, nullable=False)
    Fullname = Column(String, nullable=False)
    Certificate_No = Column(Integer, unique=True, nullable=False)
    Date_Of_Birth = Column(Date, nullable=False)
    Age = Column(Integer)
    parents = relationship("Parent", secondary="appointments")

    def __init__(self, Fullname, Certificate_No, Date_Of_Birth, Age=None):
        self.Fullname = Fullname
        self.Certificate_No = Certificate_No
        self.Date_Of_Birth = Date_Of_Birth
        self.Age = Age

    def __repr__(self):
        return f"Child name: {self.Fullname}, {self.Age} years"
    
    @classmethod
    def add_child(cls, full_name, Certificate_No, Date_of_birth):
        Date_of_birth = datetime.strptime(Date_of_birth, "%Y-%m-%d").date()
        current_date = date.today()
        age = current_date.year - Date_of_birth.year
        child = cls(
            Fullname=full_name,
            Certificate_No=Certificate_No,
            Date_Of_Birth=Date_of_birth,
            Age=age,
        )
        try:
            session.add(child)
            session.commit()
            print("Child added succesfully")
            return child
        except Exception as e:
            session.rollback()
            print(f"Error:{e}")