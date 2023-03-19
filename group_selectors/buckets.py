from helpers.models import StudentGroup, ReadingLevelRange, Student
from typing import List


class BucketGroupMaker:
    ###
    # group_maker(
    #   [Student('ALEX', 'E'), Student('ELI', 'B')], Student('MIRA', 'T'), Student('EMMA', 'M')],
    #   [LevelRange('A', 'I'), LevelRange('J', 'L'), LevelRange('M', 'O'), LevelRange('P', 'Z')],
    #   6
    # )
    ###
    students: List[Student]
    level_ranges: List[ReadingLevelRange]
    group_count: int

    def __init__(self, students: List[Student], level_ranges: List[ReadingLevelRange], group_count: int):
        self.students = students
        self.level_ranges = level_ranges
        self.group_count = group_count

    def group_maker(self):
        groups: List[StudentGroup] = []

        for group_counter in range(self.group_count):
            groups.append(StudentGroup())
        while self.students_need_assignment():
            self.round_robin_students(groups)
        return groups

    def students_need_assignment(self):
        for level_range in self.level_ranges:
            if level_range.students:
                return True
        return False

    def round_robin_students(self, groups):
        # Start by taking one student from each range into each group
        for range_counter in range(len(self.level_ranges)):
            for group_counter in range(self.group_count):
                range_students = self.level_ranges[range_counter].students
                if not range_students:
                    continue
                range_student = range_students.pop()
                groups[group_counter].students.append(range_student)
