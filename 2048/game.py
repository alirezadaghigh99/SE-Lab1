import logic
import User
import pickle

PIK = "users.pickle"

def print_end_game(status):
    print(status)
def load_users(username):
    with open(PIK, "rb") as f:
        users = pickle.load(f)
        for user in users:
            if user.name == username:
                return user
    return None


def save_user(user, new_user=True):
    users = pickle.load(open(PIK, "rb"))
    if new_user:
        users.append(user)
    else:
        for i in range(len(users)):
            if users[i].name == user.name:
                users[i] = user
    pickle.dump(users, open(PIK, "wb"))


def initial_save():
    data = []
    pickle.dump(data, open(PIK, "wb"))

def print_mat(mat):
    for i in range(logic.dimension):
        for j in range(logic.dimension):
            print(mat[i][j], end='\t')
        print()


def runner():
    new_user = False
    name = input("please enter your name: ")
    user = load_users(name)
    if user is None:
        user = User.User(name)
        new_user = True
    mat = logic.start_game()
    print_mat(mat)

    while True:
        cmd = input("Press the command : ")
        if cmd == 'w':
            mat = logic.move_up(mat)
            status = logic.game_state(mat)
            print("score : ", logic.score)
            print("high score : ", user.best_score)
            if status == 'Continue':
                logic.add_random_element(mat)
            else:
                if user.best_score < logic.score:
                    user.best_score = logic.score
                save_user(user, new_user)
                print(status)
                break

        elif cmd == 's':
            mat = logic.move_down(mat)
            status = logic.game_state(mat)
            print("score : ", logic.score)
            print("high score : ", user.best_score)
            if status == 'Continue':
                logic.add_random_element(mat)
            else:
                if user.best_score < logic.score:
                    user.best_score = logic.score
                save_user(user, new_user)
                print(status)

                break

        elif cmd == 'a':
            mat = logic.move_left(mat)
            status = logic.game_state(mat)
            print("score : ", logic.score)
            print("high score : ", user.best_score)

            if status == 'Continue':
                logic.add_random_element(mat)
            else:
                if user.best_score < logic.score:
                    user.best_score = logic.score
                save_user(user, new_user)
                print(status)
                break

        elif cmd == 'd':
            mat = logic.move_right(mat)
            status = logic.game_state(mat)
            print("score : ", logic.score)
            print("high score : ", user.best_score)

            if status == 'Continue':
                logic.add_random_element(mat)
            else:
                print(status)
                if user.best_score < logic.score:
                    user.best_score = logic.score
                save_user(user, new_user)
                break
        else:
            print("Invalid Key Pressed")

        print_mat(mat)


if __name__ == "__main__":
    runner()
