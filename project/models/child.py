from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.orm import relationship
from models import Base


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