from sqlalchemy import Column,Integer,String
from models import Base

class Parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, primary_key=True, nullable=False)
    Fathers_Name = Column(String, nullable=False)
    Mothers_Name = Column(String, nullable=False)
    Mobile_No = Column(Integer, nullable=False)
    # national id for the point parent
    National_ID = Column(Integer, unique=True, nullable=False)

    def __init__(self, Fathers_Name, Mothers_Name, Mobile_No, National_ID):
        self.Fathers_Name = Fathers_Name
        self.Mothers_Name = Mothers_Name
        self.Mobile_No = Mobile_No
        self.National_ID = National_ID

    def __repr__(self):
        return f"Father's name: {self.Fathers_Name}, Mother's name: {self.Mothers_Name}"