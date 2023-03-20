from enum import auto, Enum
from typing import List

from models.base import StudentLevel


class LevelType(Enum):
    READING = auto()
    MATH = auto()


class LevelRange:
    start: StudentLevel
    end: StudentLevel
    students: List

    def __init__(self, start: StudentLevel, end: StudentLevel):
        self.start = start
        self.end = end
        self.students = []
