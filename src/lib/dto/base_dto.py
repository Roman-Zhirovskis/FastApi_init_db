from pydantic import BaseModel


class Base(BaseModel):
    """Базовая DTO Pydantic.
    С поддержкой ORM
    """

    class Config:
        from_attributes = True
