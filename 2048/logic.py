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


