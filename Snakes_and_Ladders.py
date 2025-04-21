import random
import os
import time

# ANSI colors for terminal
def colored(text, color):
    colors = {
        'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
        'blue': '\033[94m', 'magenta': '\033[95m', 'cyan': '\033[96m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

# Game board setup
BOARD_SIZE = 100
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72,
    87: 57,
    62: 19
}
ladders = {
    6: 25,
    11: 40,
    17: 69,
    46: 90,
    60: 85,
    63: 95,
    3: 22
}

# Clear terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Draw a compact board with positions
def draw_board(player_positions):
    board = ""
    for row in range(10, 0, -1):
        line = ""
        for col in range(1, 11):
            pos = (row - 1) * 10 + col
            if row % 2 == 0:
                pos = (row * 10 + 1) - col
            marker = ""
            for player, position in player_positions.items():
                if position == pos:
                    marker += colored(player[0], 'cyan')
            if pos in snakes:
                marker += colored("S", "red")
            elif pos in ladders:
                marker += colored("L", "green")
            cell = f"{pos:>3}{marker or '  '}"
            line += cell + " "
        board += line + "\n"
    print(board)

# Simulate dice roll
def roll_dice():
    input(colored("Press ENTER to roll the dice...", "yellow"))
    roll = random.randint(1, 6)
    print(colored(f"You rolled a {roll}!", "green"))
    return roll

# Game logic
def play_game():
    clear()
    print(colored("Welcome to Complex Snakes and Ladders!", "magenta"))
    num_players = int(input("Enter number of players (2–4): "))
    while num_players < 2 or num_players > 4:
        num_players = int(input("Invalid. Please enter between 2–4 players: "))
    
    players = []
    positions = {}

    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        players.append(name)
        positions[name] = 0

    game_over = False
    while not game_over:
        for player in players:
            clear()
            print(colored(f"\n--- {player}'s Turn ---", "blue"))
            draw_board(positions)
            dice = roll_dice()

            new_position = positions[player] + dice
            if new_position > BOARD_SIZE:
                print(colored("Too far! Wait for exact roll to win.", "yellow"))
            else:
                positions[player] = new_position
                print(f"{player} moves to {new_position}")
                # Check for snakes or ladders
                if new_position in snakes:
                    final = snakes[new_position]
                    print(colored(f"Oh no! Bitten by a snake, down to {final}", "red"))
                    positions[player] = final
                elif new_position in ladders:
                    final = ladders[new_position]
                    print(colored(f"Yay! Climbed a ladder to {final}", "green"))
                    positions[player] = final

            time.sleep(1.5)

            # Check win
            if positions[player] == BOARD_SIZE:
                print(colored(f"\n🎉 {player} wins the game! 🎉", "cyan"))
                game_over = True
                break

    replay = input(colored("\nDo you want to play again? (y/n): ", "yellow"))
    if replay.lower() == 'y':
        play_game()
    else:
        print(colored("Thanks for playing! Goodbye! 👋", "magenta"))

# Start the game
if __name__ == "__main__":
    play_game()
