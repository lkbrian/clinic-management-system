from sqlalchemy import Column, Integer, String, Date, ForeignKey, or_
from sqlalchemy.orm import relationship
from models import Base, session
from datetime import datetime, date
import random

# import uuid


class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, nullable=False)
    Appointment_No = Column(Integer, unique=True, nullable=False)
    Childname = Column(Integer, ForeignKey("children.id"))
    Parentname = Column(Integer, ForeignKey("parents.id"))
    Vaccine = Column(String, nullable=False)
    Status = Column(String, nullable=False)
    Doctor_Incharge = Column(String, nullable=False)
    Appointment_Date = Column(Date, nullable=False)

    children = relationship("Child", backref="appointments")
    parents = relationship("Parent", backref="appointments")

    def __init__(
        self,
        Appointment_No,
        Childname,
        Parentname,
        Vaccine,
        Status,
        Doctor_Incharge,
        Appointment_Date,
    ):
        self.Appointment_No = Appointment_No
        self.Childname = Childname
        self.Parentname = Parentname
        self.Vaccine = Vaccine
        self.Status = Status
        self.Doctor_Incharge = Doctor_Incharge
        self.Appointment_Date = Appointment_Date

    def __repr__(self):
        return f"\n-----Appointment set for----- \n{self.Childname} by {self.Doctor_Incharge} \nScheduled for {self.Appointment_Date} \nAccompanied by {self.Parentname} \nAppointment Number: {self.Appointment_No}\n **************************"

    @classmethod
    def set_appointment(
        cls,
        child_cert_no,
        parent_id_number,
        Vaccine,
        Status,
        Doctor_Incharge,
        Appointment_Date,
    ):

        appointment_date = datetime.strptime(Appointment_Date, "%Y-%m-%d").date()
        if appointment_date > date.today():
            from models import Parent,Child
            # Query child and parent names by certificate number and ID number
            child = session.query(Child).filter_by(Certificate_No=child_cert_no).first()
            parent = (
                session.query(Parent).filter_by(National_ID=parent_id_number).first()
            )

            appointment = cls(
                # Appointment_No=str(uuid.uuid4()),
                Appointment_No=random.randint(5864, 20000),
                Childname=child.Fullname,
                Parentname = parent.Mothers_Name if parent.Mothers_Name else parent.Fathers_Name
,
                Vaccine=Vaccine,
                Status=Status,
                Doctor_Incharge=Doctor_Incharge,
                Appointment_Date=appointment_date,
            )
            try:
                session.add(appointment)
                session.commit()
                print(appointment)
            except Exception as error:
                print("Error: ", error)
        else:
            print("Appointment date must be later than today")

    @classmethod
    def vaccinate(cls, cert):
        from models import Child

        child = session.query(Child).filter_by(Certificate_No=cert).first()
        if child:
            appointments = session.query(cls).filter_by(Childname=child.id).all()
            for appointment in appointments:
                appointment.Status = "vaccinated"
                session.commit()
            print(f"Child {child.Fullname} vaccinated successfully.")
        else:
            print("Child not found or certificate number incorrect.")

    @classmethod
    def find_appointment(cls, value):
        appointments = (
            session.query(cls)
            .filter(
                or_(
                    cls.Childname == value,
                    cls.Parentname == value,
                    cls.Doctor_Incharge == value,
                    cls.Appointment_No == value,
                )
            )
            .all()
        )
        if appointments:
            print("Matching Appointments:")
            for appointment in appointments:
                print(
                    f"\nAppointment number: {appointment.Appointment_No}\nChild: {appointment.Childname}\nParent: {appointment.Parentname} \nDoctor Incharge: {appointment.Doctor_Incharge} \nStatus: {appointment.Status}\nAppointment date: {appointment.Appointment_Date}"
                )  # Use __repr__ for detailed output
        else:
            print("No appointments found for", value)
