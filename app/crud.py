from sqlalchemy.orm import Session
from models import Grad
from schemas import GradSchema


def get_grad(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Grad).offset(skip).limit(limit).all()


def create_grad(db: Session, grad: GradSchema):
    _grad = Grad(GRE_Score=grad.GRE_Score, TOEFL_Score=grad.TOEFL_Score,University_Rating=grad.University_Rating,SOP=grad.SOP,LOR=grad.LOR,CGPA=grad.CGPA,Chance_of_Admit=grad.Chance_of_Admit)
    db.add(_grad)
    db.commit()
    db.refresh(_grad)
    return _grad
