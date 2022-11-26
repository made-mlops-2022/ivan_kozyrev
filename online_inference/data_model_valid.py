from typing import Literal

from fastapi import HTTPException
from pydantic import BaseModel, validator


class Patient(BaseModel):
    age: float
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: float
    chol: float
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: float
    exang: Literal[0, 1]
    oldpeak: float
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3]
    thal: Literal[0, 1, 2]

    @classmethod
    def check_valid_value(cls, value, min_val, max_val, name):
        if value < min_val or value > max_val:
            raise HTTPException(status_code=400, detail=f'{name} must be in range [{min_val}-{max_val}]')
        return value

    @validator('age')
    def age_valid(cls, value):
        return cls.check_valid_value(value, 0, 100, 'age')

    @validator('trestbps')
    def trestbps_valid(cls, value):
        return cls.check_valid_value(value, 30, 280, 'trestbps')

    @validator('chol')
    def chol_valid(cls, value):
        return cls.check_valid_value(value, 100, 600, 'chol')

    @validator('thalach')
    def thalach_valid(cls, value):
        return cls.check_valid_value(value, 20, 250, 'thalach')

    @validator('oldpeak')
    def oldpeak_valid(cls, value):
        return cls.check_valid_value(value, 0, 9, 'oldpeak')
