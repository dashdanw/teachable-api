from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

from typing import List
from typing import Union
from typing import Optional


class Course(BaseModel):
    id:int = Field()
    name:str = Field()
    heading:str = Field()
    description:Union[str, None] = Field()
    is_published:bool = Field()
    image_url:str = Field()


class Enrollment(BaseModel):
    user_id:int = Field()
    enrolled_at:datetime = Field()
    completed_at:Union[datetime, None] = Field()
    percent_complete:int = Field()


class User(BaseModel):
    name:str = Field()
    email:str = Field()
    id:int = Field()


class Meta(BaseModel):
    total:int = Field()
    page:int = Field()
    from_item:int = Field(alias='from')
    to_item:int = Field(alias='to')
    per_page:int = Field()
    number_of_pages:int = Field()


class BaseResponseModel(BaseModel):
    pass


class CoursesResponse(BaseResponseModel):
    meta:Meta
    courses:List[Course]


class EnrollmentsResponse(BaseResponseModel):
    meta:Meta
    enrollments:List[Enrollment]


class UsersResponse(BaseResponseModel):
    meta:Meta
    users:List[User]