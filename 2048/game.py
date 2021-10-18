import logic


def print_mat(mat):
    for i in range(logic.dimension):
        for j in range(logic.dimension):
            print(mat[i][j], end='\t')
        print()


def runner():
    mat = logic.start_game()
    print_mat(mat)
    while True:
        cmd = input("Press the command : ")
        if cmd == 'w':
            mat = logic.move_up(mat)
            status = logic.game_state(mat)
            if status == 'Continue':
                print(status)
                logic.add_random_element(mat)
            else:
                break
        elif cmd == "q":
            return
        elif cmd == 's':
            mat = logic.move_down(mat)
            status = logic.game_state(mat)
            if status == 'Continue':
                print(status)
                logic.add_random_element(mat)
            else:
                break

        elif cmd == 'a':
            mat = logic.move_left(mat)
            status = logic.game_state(mat)
            if status == 'Continue':
                logic.add_random_element(mat)
            else:
                print(status)
                break

        elif cmd == 'd':
            mat = logic.move_right(mat)
            status = logic.game_state(mat)
            if status == 'Continue':
                logic.add_random_element(mat)
            else:
                print(status)
                break
        else:
            print("Invalid Key Pressed")

        print_mat(mat)


if __name__ == "__main__":
    runner()

