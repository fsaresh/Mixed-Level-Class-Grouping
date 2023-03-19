from group_selectors.buckets import BucketGroupMaker
from helpers.file_reader import load_levels_data_from_file
from helpers.models import LevelType, ReadingLevel, ReadingLevelRange


def main():
    group_count = 6
    level_ranges = [
        ReadingLevelRange(start=ReadingLevel.A, end=ReadingLevel.I),
        ReadingLevelRange(start=ReadingLevel.J, end=ReadingLevel.L),
        ReadingLevelRange(start=ReadingLevel.M, end=ReadingLevel.O),
        ReadingLevelRange(start=ReadingLevel.P, end=ReadingLevel.Z),
    ]

    student_levels_data = load_levels_data_from_file(mode=LevelType.READING, level_ranges=ranges)
    bucket_group_maker = BucketGroupMaker(
        student_levels_data=student_levels_data,
        level_ranges=level_ranges,
        group_count=group_count
    )
    groups = bucket_group_maker.group_maker()
    print_groups(groups)


def print_groups(groups):
    group_counter = 0
    for group in groups:
        group_counter += 1
        print(f'Group #{group_counter}: ')
        for student in group.students:
            print(f'- {student.raw_reading_level}, {student.name}')


if __name__ == '__main__':
    main()
