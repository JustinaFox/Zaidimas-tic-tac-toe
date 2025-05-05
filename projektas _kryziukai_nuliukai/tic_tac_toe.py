#zaidimas kryziukai nuliukai (tic tac toe)

class TicTacToe:
    def __init__(self):
        self.__board = [[' ' for _ in range(3)] for _ in range(3)]
    def get_board(self):
        return self.__board

    def set_move(self, row, col, player):
        if self.__board[row][col] == ' ':
            self.__board[row][col] = player
            return True
        else:
            print("Klaida,langelis jau uzimtas")
            return False

    def check_winner(self):
        board = self.__board
        for i in range(3):
            if board [i][0] == board[i][1] == board[i][2] !=' ':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] !=' ':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] !=' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] !=' ':
            return board[0][2]
        return None

    def print_board(self):
        print("\n 0 1 2")
        for i, row in enumerate(self.__board):
            print(i, "|".join(row))
            if i < 2:
                print(" -----")

def play_game():
    game = TicTacToe()
    game.print_board()
    player = "x"
    for turn in range(9):
        while True:
            try:
                row = int(input(f"Zaidejas {player}, pasirinkite eilute (0 - 2): "))
                col = int(input(f"Zaidejas {player}, pasirinkite stulpeli (0 - 2): "))
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Netinkamas skaicius, iveskite skaiciu tarp 0 - 2")
                    continue
                if game.set_move(row, col, player):
                    break
            except ValueError:
                print("Klaida, iveskite skaiciu tarp 0 - 2")
        game.print_board()
        winner = game.check_winner()
        if winner:
            print(f"Zaidejas {winner} wins!")
            return
        player = "o" if player == "x" else "x"
    print("Lygiosios")

if __name__ == "__main__":
    play_game()




