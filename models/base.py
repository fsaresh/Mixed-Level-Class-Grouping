from enum import auto, IntEnum


class InvalidLevelTypeMode(Exception):
    pass


class GroupMismatchCountError(Exception):
    pass


class GroupMismatchGenderError(Exception):
    pass


class GroupMismatchLevelsError(Exception):
    pass


class StudentLevel(IntEnum):
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
