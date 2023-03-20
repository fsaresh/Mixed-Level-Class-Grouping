from models.base import GroupMismatchCountError, GroupMismatchGenderError, GroupMismatchLevelsError
from models.student import StudentGroup, Student
from models.level import LevelRange
from typing import List


class BucketGroupMaker:
    students: List[Student]
    level_ranges: List[LevelRange]
    group_count: int

    def __init__(self, student_levels_data: List[Student], level_ranges: List[LevelRange], group_count: int):
        self.students = sorted(student_levels_data, key=lambda student: student.level)
        self.level_ranges = level_ranges
        self.group_count = group_count

    def group_maker(self):
        groups: List[StudentGroup] = []

        for group_counter in range(self.group_count):
            groups.append(StudentGroup())
        self.assign_students_by_level_and_gender(groups)
        self.all_groups_are_valid(groups)
        return groups

    def _round_robin_students(self, groups: List[StudentGroup]):
        # Unused, basic greedy algorithm blindly popping students into groups
        # Start by taking one student from each range into each group
        while self.students:
            for group in groups:
                if not self.students:
                    return

                student = self.students.pop()
                group.students.append(student)

    def assign_students_by_level_and_gender(self, groups: List[StudentGroup]):
        while self.students:
            student = self.students.pop()
            best_group = groups[0]
            for group in groups:
                if group.students_at_level(student.level) > best_group.students_at_level(student.level):
                    continue
                if group.gender_counter(student.gender) > best_group.gender_counter(student.gender):
                    continue
                best_group = group
            best_group.students.append(student)

    def all_groups_are_valid(self, groups):
        for group in groups:
            self.group_is_valid(group, groups)

    def group_is_valid(self, group: StudentGroup, other_groups: List[StudentGroup]):
        for other_group in other_groups:
            if group.id == other_group.id:
                return True
            if abs(len(group.students) - len(other_group.students)) > 1:
                raise GroupMismatchCountError('Significant size mismatch')
            if abs(group.boy_count - other_group.boy_count) > 1:
                raise GroupMismatchGenderError('Significant boy bias')
            if abs(group.girl_count - other_group.girl_count) > 1:
                raise GroupMismatchGenderError('Significant girl bias')
            if abs(group.nb_count - other_group.nb_count) > 1:
                raise GroupMismatchGenderError('Significant nonbinary bias')

            for range_counter in range(len(self.level_ranges)):
                if abs(group.students_at_level_range(range_counter) - other_group.students_at_level_range(range_counter)) > 2:
                    raise GroupMismatchLevelsError('Significant levels mismatch')

