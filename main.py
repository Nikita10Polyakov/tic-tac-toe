import random


def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)


def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]


def player_move(board):
    while True:
        try:
            row = int(input("Введите номер строки (1-3): ")) - 1
            col = int(input("Введите номер столбца (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Эта клетка уже занята, попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")


def computer_move(board):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"


def choose_difficulty():
    while True:
        try:
            difficulty = input("Выберите уровень сложности (1 - простой, 2 - сложный): ")
            if difficulty in ["1", "2"]:
                return difficulty
            else:
                print("Введите 1 или 2 для выбора уровня сложности.")
        except ValueError:
            print("Введите 1 или 2 для выбора уровня сложности.")


def tic_tac_toe_game():
    board = initialize_board()
    difficulty = choose_difficulty()

    if difficulty == "2":
        computer_move(board)

    while True:
        print_board(board)

        player_move(board)
        if check_winner(board):
            print_board(board)
            print("Поздравляем! Вы выиграли!")
            break
        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break

        computer_move(board)
        if check_winner(board):
            print_board(board)
            print("Компьютер выиграл!")
            break
        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break

# Запуск игры
tic_tac_toe_game()