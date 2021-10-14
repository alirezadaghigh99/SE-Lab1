import random

dimension = 4
goal_score = 2048


def start_game():
    mat = [[0 for _ in range(dimension)] for _ in range(dimension)]

    # printing controls for user
    print("enter one of these commands : ")
    print("'w' : Move Up")
    print("'s' : Move Down")
    print("'a' : Move Left")
    print("'d' : Move Right")

    add_random_element(mat)
    return mat


def game_state(mat):
    for i in range(dimension):
        for j in range(dimension):
            if mat[i][j] == goal_score:
                return 'Win'

    for i in range(dimension):
        for j in range(dimension):
            if mat[i][j] == 0:
                return 'Continue'

    for i in range(dimension - 1):
        for j in range(dimension - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'Continue'

    for j in range(dimension - 1):
        if mat[dimension - 1][j] == mat[dimension - 1][j + 1]:
            return 'Continue'

    for i in range(dimension - 1):
        if mat[i][dimension - 1] == mat[i + 1][dimension - 1]:
            return 'Continue'

    # else we have lost the game
    return 'Lose'


def compress(mat):
    new_mat = []
    for i in range(dimension):
        new_mat.append([0] * dimension)
    for i in range(dimension):
        pos = 0
        for j in range(4):
            if new_mat[i][j] != mat[i][j]:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    pos += 1
    return new_mat


def add_random_element(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    mat[r][c] = 2


def merge(mat):
    # this function handles left movement. other moves can be done vis matrix transformations.
    for i in range(dimension):
        for j in range(dimension - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
    return mat


def reverse_cols(mat):
    new_mat = []
    for i in range(dimension):
        new_mat += [[]]
        for j in range(dimension):
            new_mat[i].append(mat[i][dimension - j - 1])
    return new_mat


def transpose(mat):
    new_mat = []
    for i in range(dimension):
        new_mat.append += [[]]
        for j in range(dimension):
            new_mat[i].append(mat[j][i])
    return new_mat


def move_left(mat):
    new_mat = compress(mat)
    new_mat = merge(new_mat)
    new_mat = compress(new_mat)
    return new_mat


def move_right(mat):
    new_mat = reverse_cols(mat)
    new_mat = move_left(new_mat)
    new_mat = reverse_cols(new_mat)
    return new_mat


def move_up(mat):
    new_mat = transpose(mat)
    new_mat = move_left(new_mat)
    new_mat = transpose(new_mat)
    return new_mat


def move_down(mat):
    new_mat = transpose(mat)
    new_mat = move_right(new_mat)
    new_mat = transpose(new_mat)
    return new_mat
