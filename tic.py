import numpy as np

def initialize_board():
    """Initialize  """
    return np.full((3, 3), ' ')
 
def display_board(board):
    """Display the Tic-Tac-Toe board."""
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_win(board, player):
    """Check if the specified player has won."""
    # Check rows and columns
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def check_draw(board):
    """Check if the board is full and there's no winner."""
    return not np.any(board == ' ')

def tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    board = initialize_board() 
    players = ['X', 'O']
    turn = 0
    
    
    while True:
        display_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        
        # Get player input
        row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
        
        # Make the move
        if board[row, col] == ' ':
            board[row, col] = player
        else:
            print("Invalid move. Try again.")
            continue
        
        # Check win condition
        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check draw condition
        if check_draw(board):
            display_board(board)
            print("The game is a draw!")
            break
        
        # Switch turns
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()


 