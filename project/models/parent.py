from sqlalchemy import Column,Integer,String
from models import Base,session

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
    
    @classmethod
    def add_parent(cls, Fathersname, Mothersname, Mobile_No, National_ID):
        parent = Parent(
            Fathers_Name=Fathersname,
            Mothers_Name=Mothersname,
            Mobile_No=Mobile_No,
            National_ID=National_ID,
        )
        try:
            session.add(parent)
            session.commit()
            print("Added Parent succesfuly")
            return parent
        except Exception as e:
            session.rollback()
            print(f"Error:{e}")