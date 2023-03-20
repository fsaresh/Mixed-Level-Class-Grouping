import uuid
from enum import Enum
from typing import List
from helpers.level_models import StudentLevel


class Gender(Enum):
    F = 'F'
    M = 'M'
    N = 'N'


class Student:
    name: str
    raw_reading_level: str
    level_range_id: int
    group_id: int
    raw_gender: str

    def __init__(self, name: str, reading_level: str, reading_level_range_id: int, gender: str, group: uuid = None):
        self.name = name
        self.raw_reading_level = reading_level
        self.level_range_id = reading_level_range_id
        self.group = group
        self.raw_gender = gender

    @property
    def level(self):
        return StudentLevel[self.raw_reading_level]

    @property
    def gender(self):
        return Gender[self.raw_gender]


class StudentGroup:
    id: uuid
    students: List[Student]
    _boy_count: int
    _girl_count: int
    _nb_count: int

    def __init__(self):
        self.id = uuid.uuid4()
        self.students = []
        _boy_count = 0
        _girl_count = 0
        _nb_count = 0

    def students_at_level(self, student_level: StudentLevel):
        return len([student for student in self.students if student.level is student_level])

    def students_at_level_range(self, range_id: int):
        return len([student for student in self.students if student.level_range_id is range_id])

    def gender_counter(self, gender: Gender):
        return len([student for student in self.students if student.gender is gender])

    def other_gender_counter(self, gender):
        return len(self.students) - self.gender_counter(gender)

    @property
    def boy_count(self):
        return self.gender_counter(Gender.M)

    @property
    def girl_count(self):
        return self.gender_counter(Gender.F)

    @property
    def nb_count(self):
        return self.gender_counter(Gender.N)
