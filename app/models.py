from sqlalchemy import  Column, Float, Integer
from config import Base

class Grad(Base):
    __tablename__ ="Grad_parameters"

    id = Column(Integer, primary_key=True, index=True)
    GRE_Score = Column(Integer)
    TOEFL_Score = Column(Integer)
    University_Rating = Column(Integer)
    SOP = Column(Integer)
    LOR = Column(Integer)
    CGPA = Column(Integer)
    Chance_of_Admit = Column(Float)

