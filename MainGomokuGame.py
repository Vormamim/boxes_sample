import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os

class TitleScreen:
    def __init__(self, on_start_game):
        self.root = tk.Tk()
        self.root.title("Gomoku - Title Screen")
        self.on_start_game = on_start_game
        self.create_title_widgets()

    def create_title_widgets(self):
        title_label = tk.Label(self.root, text="Welcome to Gomoku", font=("Helvetica", 24))
        title_label.pack(pady=20)

        start_button = tk.Button(self.root, text="Start Game", command=self.on_start_game)
        start_button.pack(pady=10)

    def run(self):
        self.root.mainloop()

class Game:
    def __init__(self):
        self.title_screen = TitleScreen(self.start_game)
        self.root = None
        self.board = None
        self.current_player = "X"
        self.ai_mode = False
        self.ai_difficulty = "easy"
        self.sound_on = True  # Add a flag for sound on/off

    def start_game(self):
        self.title_screen.root.destroy()
        self.root = tk.Tk()
        self.root.title("Gomoku")
        self.create_menu()
        self.create_board()
        self.play_background_music()  # Play background music
        self.root.mainloop()

    def create_menu(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.game_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gamemode selection", menu=self.game_menu)
        self.game_menu.add_command(label="Human vs Human", command=self.set_hvh)
        self.game_menu.add_command(label="Human vs Computer (Easy)", command=self.set_hvc_easy)
        self.game_menu.add_command(label="Human vs Computer (Hard)", command=self.set_hvc_hard)

        self.sound_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Sound", menu=self.sound_menu)
        self.sound_on_var = tk.BooleanVar()
        self.sound_on_var.set(True) 
        self.sound_menu.add_checkbutton(label="Sound On/Off", variable=self.sound_on_var, command=self.toggle_sound)

    def toggle_sound(self):
        self.sound_on = self.sound_on_var.get()

    def set_hvh(self):
        self.ai_mode = False
        self.restart_game()

    def set_hvc_easy(self):
        self.ai_mode = True
        self.ai_difficulty = "easy"
        self.restart_game()

    def set_hvc_hard(self):
        self.ai_mode = True
        self.ai_difficulty = "hard"
        self.restart_game()

    def create_board(self):
        self.board = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                button = tk.Button(self.root, text=" ", command=lambda i=i, j=j: self.make_move(i, j), height=2, width=5)
                button.grid(row=i, column=j)
                self.board[i][j] = button

    def make_move(self, i, j):
        if self.board[i][j]['text'] == " ":
            self.play_sound("click")  
            self.board[i][j]['text'] = self.current_player
            if self.check_win(i, j):
                self.play_sound("win") 
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.restart_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O" and self.ai_mode:
                    self.ai_move()

    def ai_move(self):
        if self.ai_difficulty == "easy":
            self.ai_move_easy()
        else:
            self.ai_move_hard()

    def ai_move_easy(self):
        while True:
            i, j = random.randint(0, 8), random.randint(0, 8)
            if self.board[i][j]['text'] == " ":
                self.board[i][j].invoke()
                break

    def ai_move_hard(self):
        best_score = -1
        best_move = None

        for i in range(9):
            for j in range(9):
                if self.board[i][j]['text'] == " ":
                    score = self.evaluate_move(i, j)
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move is not None:
            i, j = best_move
            self.board[i][j].invoke()

    def evaluate_move(self, i, j):
        # Check the score for each possible direction
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        total_score = 0
        for dx, dy in directions:
            count = self.count_continuous(i, j, dx, dy) + self.count_continuous(i, j, -dx, -dy) - 1
            if self.current_player == "X":
                # Positive score for player X
                total_score += count
            else:
                # Negative score for player O
                total_score -= count
        return total_score

       

    def play_sound(self, sound_type):
        if not self.sound_on:
            return

        if sound_type == "win":
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join("WinSound.mp3"))
            pygame.mixer.music.play()
        elif sound_type == "click":
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join("ClickSound.mp3"))
            pygame.mixer.music.play()

    def play_background_music(self):
        if not self.sound_on:
            return

        #pygame.mixer.init()
        #pygame.mixer.music.load(os.path.join("background_music.mp3"))
        #pygame.mixer.music.play(-1)  
    def check_win(self, i, j):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            if self.count_continuous(i, j, dx, dy) + self.count_continuous(i, j, -dx, -dy) - 1 >= 5:
                return True
        return False

    def count_continuous(self, i, j, dx, dy):
        count = 0
        while 0 <= i < 9 and 0 <= j < 9 and self.board[i][j]['text'] == self.current_player:
            i += dx
            j += dy
            count += 1
        return count

    def restart_game(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j].destroy()
        self.create_board()
        self.current_player = "X"

    def start(self):
        self.title_screen.run()

if __name__ == "__main__":
    game = Game()
    game.start()
