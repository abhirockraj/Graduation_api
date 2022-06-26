from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class GradSchema(BaseModel):
    id: Optional[int] = None
    GRE_Score: Optional[int] = None
    TOEFL_Score: Optional[int] = None
    University_Rating: Optional[int] = None
    SOP: Optional[int] = None
    LOR: Optional[int] = None
    CGPA: Optional[int] = None
    Chance_of_Admit: Optional[float] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestGrad(BaseModel):
    parameter: GradSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]