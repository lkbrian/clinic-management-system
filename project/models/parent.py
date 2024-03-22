from sqlalchemy import Column, Integer, String, or_
from models import Base, session


class Parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, primary_key=True, nullable=False)
    Fathers_Name = Column(String, nullable=True)
    Mothers_Name = Column(String, nullable=True)
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
        if Fathersname or Mothersname:  # At least one parent name should be given
            parent = cls(
                Fathers_Name=Fathersname,
                Mothers_Name=Mothersname,
                National_ID=National_ID,
            )
            try:
                session.add(parent)
                session.commit()
                print(parent)
                return parent
            except Exception as e:
                session.rollback()
                print(f"\033[91m Error: {e} \033[0m")
        else:
            print("At least one parent name should be provided.")

    @classmethod
    def find_parent(cls, value):
        parents = (
            session.query(cls)
            .filter(
                or_(
                    cls.Fathers_Name == value,
                    cls.Mothers_Name == value,
                    cls.National_ID == value,
                )
            )
            .all()
        )
        if parents:
            for parent in parents:
                print(f"\n{parent.Fathers_Name} and {parent.Mothers_Name}")
        else:
            print("\033[91m No Parents were found!\033[0m")

    @classmethod
    def update_parent(
        cls, parent_id, Fathersname=None, Mothersname=None, National_ID=None
    ):
        parent = session.query(cls).get(parent_id)
        if parent:
            if Fathersname:
                parent.Fathers_Name = Fathersname
            if Mothersname:
                parent.Mothers_Name = Mothersname
            if National_ID:
                parent.National_ID = National_ID
            try:
                session.commit()
                print("Parent updated successfully.")
                print(parent)
            except Exception as e:
                session.rollback()
                print(f" \033[91m Error: {e} \033[0m")
        else:
            print("\033[91m Parent not found. \033[0m")

    @classmethod
    def get_all_parents(cls):
        try:
            parents = session.query(cls).all()
            if parents:
                print("All parents")
                for pair_parent in parents:
                    print(pair_parent)
            else:
                print ("No Parents found.")
        except Exception as error:
            print("Error: ",error)