
# define - What data your API accepts and returns. structure of our API 
# Defines request and response data models using Pydantic.

from pydantic import BaseModel, ConfigDict, HttpUrl, Field


# BaseModel comes from Pydantic.
# It gives your class: Validation , Type checking , Automatic JSON conversion
class URLBase(BaseModel):
    target_url: HttpUrl


# it contains Basemodel + target_rul: HttpUrl
class URLCreate(URLBase):
    custom_key: str = Field(default=None, min_length=3, max_length=20)


# This is what your API sends back.
class URLResponse(URLBase):
    id: int
    key: str
    secret_key: str
    is_active: bool
    clicks: int

    # It allows Pydantic to read SQLAlchemy models.
    model_config = ConfigDict(from_attributes=True)