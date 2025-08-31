def print_board(board):
    """Imprime o tabuleiro do jogo da velha."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    """Verifica se um jogador venceu."""
    # Verificar linhas
    for row in board:
        if all(s == player for s in row):
            return True
    # Verificar colunas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Verificar diagonais
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    """Verifica se o jogo empatou."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    """Função principal do jogo da velha."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Jogador '{current_player}', escolha a linha (0, 1, 2): "))
            col = int(input(f"Jogador '{current_player}', escolha a coluna (0, 1, 2): "))
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Posição fora do tabuleiro. Tente novamente.")
                continue

            if board[row][col] == " ":
                board[row][col] = current_player
            else:
                print("Essa posição já está ocupada. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"O jogador '{current_player}' venceu!")
            break
        
        if check_draw(board):
            print_board(board)
            print("O jogo empatou!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()