from enum import Enum
from pydantic import BaseModel, Field


class Grade(str, Enum):
    first = "1º ano"
    second = "2º ano"
    third = "3º ano"
    fourth = "4º ano"
    fifth = "5º ano"


class Topic(str, Enum):
    syllables = "sílabas"
    reading = "compreensão de leitura"
    separation = "separação de palavras"
    accentuation = "acentuação"


class Difficulty(str, Enum):
    easy = "fácil"
    medium = "médio"
    hard = "difícil"


class WorksheetRequest(BaseModel):
    grade: Grade
    topic: Topic
    difficulty: Difficulty
    seed: int | None = Field(default=None, ge=0)


class Worksheet(BaseModel):
    title: str
    instructions: str
    grade: Grade
    topic: Topic
    difficulty: Difficulty
    exercises: list[str]
    final_challenge: str
    illustrations: list[str]
    seed: int
