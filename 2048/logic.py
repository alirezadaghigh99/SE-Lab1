import random

dimension = 4
goal_score = 2048



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
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if new_mat[i][j] != mat[i][j]:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                    pos += 1
    return new_mat, changed



def add_random_element(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    mat[r][c] = 2

