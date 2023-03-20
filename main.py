from group_selectors.buckets import BucketGroupMaker
from helpers.file_reader import load_levels_data_from_file
from helpers.level_models import StudentLevel, LevelRange, LevelType


def main():
    group_count = 6
    level_ranges = [
        LevelRange(start=StudentLevel.A, end=StudentLevel.I),
        LevelRange(start=StudentLevel.J, end=StudentLevel.L),
        LevelRange(start=StudentLevel.M, end=StudentLevel.O),
        LevelRange(start=StudentLevel.P, end=StudentLevel.Z),
    ]

    student_levels_data = load_levels_data_from_file(mode=LevelType.READING, level_ranges=level_ranges)
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
