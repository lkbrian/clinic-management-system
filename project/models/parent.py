from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models import Base, session,Child
from datetime import datetime, date

class Parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, primary_key=True, nullable=False)
    Fathers_Name = Column(String, nullable=False)
    Mothers_Name = Column(String, nullable=False)
    National_ID = Column(Integer, unique=True, nullable=False)

    # children = relationship("Child", back_populates="parent")

    def __init__(self, Fathers_Name, Mothers_Name, National_ID):
        self.Fathers_Name = Fathers_Name
        self.Mothers_Name = Mothers_Name
        self.National_ID = National_ID

    def __repr__(self):
            return f"\nRegistered parents: {self.Fathers_Name} and {self.Mothers_Name} \nIdentification: {self.National_ID}"
        
    @classmethod
    def add_parent(cls, Fathersname, Mothersname, National_ID):
        parent = cls(
            Fathers_Name=Fathersname,
            Mothers_Name=Mothersname,
            National_ID=National_ID
        )
        try:
            session.add(parent)
            session.commit()
            print(parent)
            return parent
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")