import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 600
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE
LINE_WIDTH = 8

# Colors
BG_COLOR = "#FFFFFF"
GRID_COLOR = "#000000"
PLAYER_COLOR = "#0000FF"
COMPUTER_COLOR = "#FF0000"

# Game variables
player_score = 0
computer_score = 0
player_turn = True
game_over = False
board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initialize the game board
def init_board():
    global board
    board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Check if a move is valid
def is_valid_move(row, col):
    return board[row][col] is None

# Make a move
def make_move(row, col):
    global player_turn, game_over, player_score, computer_score
    if is_valid_move(row, col):
        board[row][col] = PLAYER_COLOR if player_turn else COMPUTER_COLOR
        player_turn = not player_turn
        if not game_over and not player_turn:
            computer_move()
        update_board()
        
# Make a move for the computer
def computer_move():
    global player_turn
    valid_moves = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if is_valid_move(r, c)]
    if valid_moves:
        row, col = random.choice(valid_moves)
        board[row][col] = COMPUTER_COLOR
        player_turn = True
        update_board()

## Draw grid lines
def draw_grid_lines():
    for i in range(GRID_SIZE):
        x0 = i * CELL_SIZE
        y0 = 0
        x1 = x0
        y1 = HEIGHT
        canvas.create_line(x0, y0, x1, y1, fill=GRID_COLOR, width=LINE_WIDTH)
    for i in range(GRID_SIZE):
        x0 = 0
        y0 = i * CELL_SIZE
        x1 = WIDTH
        y1 = y0
        canvas.create_line(x0, y0, x1, y1, fill=GRID_COLOR, width=LINE_WIDTH)

# Update the game board
def update_board():
    canvas.delete("tiles")  # Delete only the tiles, not the grid lines
    # Draw board tiles
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            x0 = c * CELL_SIZE
            y0 = r * CELL_SIZE
            x1 = x0 + CELL_SIZE
            y1 = y0 + CELL_SIZE
            canvas.create_rectangle(x0, y0, x1, y1, fill=BG_COLOR, outline="", tags="tiles")
            if board[r][c] is not None:
                canvas.create_rectangle(x0, y0, x1, y1, fill=board[r][c], outline="", tags="tiles")

    if game_over:
        show_win_screen()
        
    # Draw board tiles
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            x0 = c * CELL_SIZE
            y0 = r * CELL_SIZE
            x1 = x0 + CELL_SIZE
            y1 = y0 + CELL_SIZE
            canvas.create_rectangle(x0, y0, x1, y1, fill=BG_COLOR, outline="Black")
            if board[r][c] is not None:
                canvas.create_rectangle(x0, y0, x1, y1, fill=board[r][c], outline="Black")
    if game_over:
        show_win_screen()

# Show the win screen
def show_win_screen():
    global player_score, computer_score
    if player_score >= 5:
        text = "You win!"
    else:
        text = "Computer wins!"
    canvas.create_text(WIDTH//2, HEIGHT//2, text=text, font=("Arial", 32))
    canvas.create_text(WIDTH//2, HEIGHT//2+50, text="Player score: {}".format(player_score), font=("Arial", 16))
    canvas.create_text(WIDTH//2, HEIGHT//2+75, text="Computer score: {}".format(computer_score), font=("Arial", 16))
    canvas.create_rectangle(WIDTH//2-50, HEIGHT//2+100, WIDTH//2+50, HEIGHT//2+130, fill=BG_COLOR, outline="")
    canvas.create_text(WIDTH//2, HEIGHT//2+115, text="Retry", font=("Arial", 16), fill=PLAYER_COLOR)

# Handle mouse clicks
def handle_click(event):
    if not game_over and player_turn:
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        make_move(row, col)

# Initialize the game
def init_game():
    global player_score, computer_score, player_turn, game_over
    player_score = 0
    computer_score = 0
    player_turn = True
    game_over = False
    init_board()
    draw_grid_lines()  # Call the draw_grid_lines function here
    update_board()

# Create the GUI
root = tk.Tk()
root.title("Longest Line Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()

canvas.bind("<Button-1>", handle_click)

init_game()

root.mainloop()
