from enum import Enum
from pydantic import BaseModel


class PredictionEnum(str, Enum):
    Human = "Human"
    AI = "AI"


class TextToClassify(BaseModel):
    text: str


class ClassificationResult(BaseModel):
    prediction: PredictionEnum
