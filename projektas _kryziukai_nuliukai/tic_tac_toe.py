#zaidimas kryziukai nuliukai (tic tac toe)


# Sukuriama žaidimo klasė "Kryžiukai-nuliukai"
class TicTacToe:
    def __init__(self):
        self.__board = [[' ' for _ in range(3)] for _ in range(3)] #  3x3 dydžio žaidimas (pradžioje visi langeliai tušti)
    def get_board(self): # Grąžina žaidimo lentą
        return self.__board

    # Leidžia žaidėjui padaryti ėjimą, jei pasirinktas langelis yra laisvas
    def set_move(self, row, col, player):
        if self.__board[row][col] == ' ':
            self.__board[row][col] = player  # Įrašo žaidėjo simbolį (x arba o) į pasirinktą vietą
            return True # Ėjimas sėkmingas
        else:
            print("Klaida,langelis jau uzimtas") # Jei langelis užimtas – praneša apie klaidą
            return False # Ėjimas nesėkmingas

    # Patikrina, ar kas nors laimėjo (eilutės, stulpeliai, įstrižainės)
    def check_winner(self):
        board = self.__board
        for i in range(3):
            if board [i][0] == board[i][1] == board[i][2] !=' ': # Tikrina eilutes
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] !=' ': # Tikrina stulpelius
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] !=' ':  # Tikrina pagrindinę įstrižainę
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] !=' ':  # Tikrina antrinę įstrižainę
            return board[0][2]
        return None # Nėra laimėtojo

    # Atspausdina dabartinę žaidimo lentos būseną
    def print_board(self):
        print("\n 0 1 2")  # Stulpelių numeriai
        for i, row in enumerate(self.__board):
            print(i, "|".join(row))  # Atspausdina eilutę su tarpais tarp simbolių
            if i < 2:
                print(" -----") # Brūkšneliai tarp eilučių

# Pagrindinė funkcija, valdanti žaidimo eigą
def play_game():
    game = TicTacToe() # Sukuriamas žaidimo objektas
    game.print_board() # Pradiniame ekrane parodoma tuščia lenta
    player = "x"       # Pradeda žaidėjas "x"
    for turn in range(9): # Galimi 9 ėjimai (kai lenta pilna)
        while True:       # Kartojama, kol ėjimas bus teisingas
            try:
                row = int(input(f"Zaidejas {player}, pasirinkite eilute (0 - 2): "))
                col = int(input(f"Zaidejas {player}, pasirinkite stulpeli (0 - 2): "))
                if row not in [0, 1, 2] or col not in [0, 1, 2]:    # Tikrina ar įvesti skaičiai teisingi
                    print("Netinkamas skaicius, iveskite skaiciu tarp 0 - 2")
                    continue
                if game.set_move(row, col, player):   # Bando atlikti ėjimą, jei sėkmingai – išeina iš ciklo
                    break
            except ValueError:
                print("Klaida, iveskite skaiciu tarp 0 - 2")
        game.print_board()             # Parodo atnaujintą lentą
        winner = game.check_winner()   # Patikrina ar yra laimėtojas
        if winner:
            print(f"Zaidejas {winner} wins!")
            return     # Nutraukia žaidimą, jei kas nors laimėjo
        player = "o" if player == "x" else "x"   # Pakeičia žaidėją
    print("Lygiosios")  # Jei niekas nelaimėjo per 9 ėjimus

# Jei paleidžiama tiesiogiai – pradedamas žaidimas
if __name__ == "__main__":
    play_game()




