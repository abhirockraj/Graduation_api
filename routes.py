from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import GradSchema, Request, Response, RequestGrad

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_grad_data(request: RequestGrad, db: Session = Depends(get_db)):
    crud.create_grad(db, grad=request.parameter)
    return Response(status="Ok",
                    code="201",
                    message="Grad created successfully").dict(exclude_none=True)


@router.get("/")
async def get_grad(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _grad = crud.get_grad(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_grad)


