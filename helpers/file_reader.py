import csv
from typing import List
from helpers.models import InvalidLevelTypeMode, LevelType, ReadingLevel, ReadingLevelRange, Student


def load_levels_data_from_file(mode: LevelType, level_ranges: List[ReadingLevelRange]) -> List[Student]:
    if mode is LevelType.READING:
        file = 'data_fixtures/reading_levels_data.csv'
    elif mode is LevelType.MATH:
        file = 'data_fixtures/math_levels_data.csv'
    else:
        raise InvalidLevelTypeMode(f'Invalid level type mode. Valid selections are: {LevelType}')

    with open(file) as data_file:
        data_reader = csv.reader(data_file)
        return load_levels_from_data_reader(data_reader, level_ranges)


def load_levels_from_data_reader(data_reader, level_ranges: List[ReadingLevelRange]):
    student_levels_data = []
    is_first_row = True

    for entry in data_reader:
        # Skip blank first entry after getting names
        if is_first_row:
            is_first_row = False
            continue

        # Identify current student as basis
        name, reading_level = entry

        # We need to find which reading level range the reading level is in
        for levels_range_counter in range(len(level_ranges)):
            range_start = level_ranges[levels_range_counter].start
            range_end = level_ranges[levels_range_counter].end
            if range_start <= ReadingLevel[reading_level] <= range_end:
                # Create student entry with name, reading level, and which reading range they're in
                student_reading_range = levels_range_counter
                student = Student(
                    name=name,
                    reading_level=reading_level,
                    reading_level_range_id=student_reading_range
                )
                student_levels_data.append(student)
                level_ranges[levels_range_counter].students.append(student)
                break

    return student_levels_data
