import uuid
from enum import auto, Enum, IntEnum
from typing import List


class Student:
    name: str
    raw_reading_level: str
    reading_level_range_id: int
    group_id: int

    def __init__(self, name: str, reading_level: str, reading_level_range_id: int, group: uuid = None):
        self.name = name
        self.raw_reading_level = reading_level
        self.reading_level_range_id = reading_level_range_id
        self.group = group

    @property
    def reading_level(self):
        return ReadingLevel[self.raw_reading_level]


class StudentGroup:
    id: uuid
    students: List[Student]

    def __init__(self):
        self.id = uuid.uuid4()
        self.students = []


class ReadingLevel(IntEnum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()
    G = auto()
    H = auto()
    I = auto()
    J = auto()
    K = auto()
    L = auto()
    M = auto()
    N = auto()
    O = auto()
    P = auto()
    Q = auto()
    R = auto()
    S = auto()
    T = auto()
    U = auto()
    V = auto()
    W = auto()
    X = auto()
    Y = auto()
    Z = auto()


class ReadingLevelRange:
    start: ReadingLevel
    end: ReadingLevel
    students: List[Student]

    def __init__(self, start: ReadingLevel, end: ReadingLevel):
        self.start = start
        self.end = end
        self.students = []


class LevelType(Enum):
    READING = auto()
    MATH = auto()


class InvalidLevelTypeMode(Exception):
    pass
