from sqlalchemy import Column,Integer,String,Date,ForeignKey
from models import Base


class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, nullable=False)
    Vaccine = Column(String, nullable=False)
    Appointment_Date = Column(Date, nullable=False)
    Doctor_Incharge = Column(String, nullable=False)
    Appointment_No = Column(Integer, unique=True, nullable=False)
    Child_ID = Column(Integer, ForeignKey("children.id"))
    Paren_ID = Column(Integer, ForeignKey("parents.id"))