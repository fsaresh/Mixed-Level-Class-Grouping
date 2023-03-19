from helpers.models import StudentGroup, ReadingLevelRange, Student
from typing import List


class BucketGroupMaker:
    students: List[Student]
    level_ranges: List[ReadingLevelRange]
    group_count: int

    def __init__(self, student_levels_data: List[Student], level_ranges: List[ReadingLevelRange], group_count: int):
        self.students = sorted(student_levels_data, key=lambda student: student.reading_level)
        self.level_ranges = level_ranges
        self.group_count = group_count

    def group_maker(self):
        groups: List[StudentGroup] = []

        for group_counter in range(self.group_count):
            groups.append(StudentGroup())
        while self.students:
            self.round_robin_students(groups)
        return groups


    def round_robin_students(self, groups):
        # Start by taking one student from each range into each group
        for group_counter in range(self.group_count):
            if not self.students:
                return

            student = self.students.pop()
            groups[group_counter].students.append(student)
