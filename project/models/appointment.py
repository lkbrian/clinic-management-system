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
            from models import Parent, Child

            child = session.query(Child).filter_by(Certificate_No=child_cert_no).first()
            parent = (
                session.query(Parent).filter_by(National_ID=parent_id_number).first()
            )

            # Check if child is registered
            if not child:
                print("Child is not registered")
                return

            # Check if parent exists and matches the parent associated with the child
            if not parent:
                print("Parent not found")
                return
            elif parent.National_ID != child.parent_id:
                print("Parent ID does not match the parent associated with the child")
                return

            # Check if child is vaccinated
            if cls.Status == "Unvaccinated":
                print("Child must clear vaccinations before setting an appointment")
                return

            # Set appointment
            appointment = cls(
                Appointment_No=random.randint(5864, 20000),
                Childname=child.Fullname,
                Parentname=(
                    parent.Mothers_Name if parent.Mothers_Name else parent.Fathers_Name
                ),
                Vaccine=Vaccine,
                Status=Status,
                Doctor_Incharge=Doctor_Incharge,
                Appointment_Date=appointment_date,
            )

            try:
                session.add(appointment)
                session.commit()
                print(appointment)
                print("\033[92m Appointment set successfully \033[0m")
            except Exception as error:
                print("Error: ", error)
        else:
            print("\033[91m Appointment date must be later than today \033[0m")

    @classmethod
    def vaccinate(cls, cert):
        from models import Child

        child = session.query(Child).filter_by(Certificate_No=cert).first()
        if child:
            appointments = session.query(cls).filter_by(Childname=child.id).all()
            for appointment in appointments:
                appointment.Status = "vaccinated"
                session.commit()
            print(f"\033[92m Child {child.Fullname} vaccinated successfully.\033[0m")
        else:
            print("\033[91m Child not found or certificate number incorrect.\033[0m")

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
                status = (
                    f"\033[92m {appointment.Status} \033[0m"
                    if appointment.Status == "vaccinated"
                    else f"\033[91m {appointment.Status} \033[0m"
                )
                print(
                    f"\nAppointment number: {appointment.Appointment_No}\nChild: {appointment.Childname}\nParent: {appointment.Parentname} \nDoctor Incharge: {appointment.Doctor_Incharge} \nStatus: {status}\nAppointment date: {appointment.Appointment_Date}"
                )
        else:
            print("No appointments found for", value)

    @classmethod
    def update_appointment(
        cls,
        Appointment_No,
        Vaccine=None,
        Status=None,
        Doctor_Incharge=None,
        Appointment_Date=None,
    ):

        try:
            appointment = (
                session.query(cls).filter_by(Appointment_No=Appointment_No).first()
            )
            if appointment:
                if Vaccine:
                    appointment.Vaccine = Vaccine
                if Status:
                    appointment.Status = Status
                if Doctor_Incharge:
                    appointment.Doctor_Incharge = Doctor_Incharge
                if Appointment_Date:
                    appointment_date = datetime.strptime(
                        Appointment_Date, "%Y-%m-%d"
                    ).date()
                    if appointment_date > date.today():
                        appointment.Appointment_Date = appointment_date
                    else:
                        print(
                            "\033[91mError: Appointment date must be later than today\033[0m"
                        )
                        return None

                session.commit()
                print("\033[92mAppointment updated successfully.\033[0m")
                return appointment
            else:
                print("\033[91mNo Such Appointment.\33[0m")
        except Exception as error:
            session.rollback()
            print(f"\033[91mError: {error}\033[0m")

    @classmethod
    def get_vaccinated(cls):
        appointments = session.query(cls).filter_by(Status="vaccinated")
        if appointments:
            print("Matching Appointments:")
            for appointment in appointments:
                print(
                    f"\nChild: {appointment.Childname}\nStatus: \033[92m {appointment.Status}\033[0m"
                )
        else:
            print("No appointments found")

    @classmethod
    def get_unvaccinated(cls):
        appointments = session.query(cls).filter_by(Status="Unvaccinated")
        if appointments:
            print("Matching Appointments:")
            for appointment in appointments:
                print(
                    f"\nChild: {appointment.Childname}\nStatus: \033[91m {appointment.Status}\033[0m"
                )
        else:
            print("No appointments found")

    @classmethod
    def get_all_appointments(cls):
        try:
            appointments = session.query(cls).all()
            if appointments:
                print("All Appointments")
                for appointment in appointments:
                    if appointment.Status == "vaccinated":
                        print(
                            f"\n--------Appointment for-------- \n{appointment.Childname} by {appointment.Doctor_Incharge} \nScheduled for {appointment.Appointment_Date} \nAccompanied by {appointment.Parentname} \nAppointment Number: {appointment.Appointment_No}\nStatus: \033[92m {appointment.Status}\033[0m \n --------------------------------"
                        )
                    else:
                        print(
                            f"\n--------Appointment for-------- \n{appointment.Childname} by {appointment.Doctor_Incharge} \nScheduled for {appointment.Appointment_Date} \nAccompanied by {appointment.Parentname} \nAppointment Number: {appointment.Appointment_No}\nStatus: \033[91m {appointment.Status} \033[0m \n --------------------------------"
                        )
            else:
                print("\033[91m No appointments found. \033[0m")
        except Exception as error:
            print(f"\033[91m Error:  {error}\033[0m")
