# Snakes-n-Ladders

---

# 🐍🎲 Complex Snakes and Ladders Game — Python

This is a **fun and colorful multiplayer Snake and Ladders game** built entirely in Python. It runs in the terminal and includes a dynamic board, dice rolls, snakes, ladders, and multiplayer support (2 to 4 players).  

> **No external libraries** are required — just run and play!

---

## 🔧 Features

- 🎮 Supports 2 to 4 players  
- 🎲 Realistic dice roll simulation  
- 🐍 Snakes send you down  
- 🪜 Ladders take you up  
- 🌈 Colorful terminal output (for player turns, snakes, ladders, etc.)  
- 📊 Live game board with player positions  
- 🔁 Replay option after the game ends  
- 🚫 Exact roll required to win — just like the classic rules

---

## 📁 How to Set Up

### Step 1: Prerequisites

- Make sure **Python 3** is installed.
- To check, run this command in your terminal:
  ```bash
  python --version
  ```
  or
  ```bash
  python3 --version
  ```

> ✅ If you see Python version 3.x.x, you're good to go!

---

### Step 2: Download the Game

1. Create a new file called `snakes_and_ladders.py`
2. Copy the entire game code into that file.

Alternatively, download the file from your own repository if you host it.

---

### Step 3: Run the Game

Open your terminal in the folder where `snakes_and_ladders.py` is saved, then run:

```bash
python snakes_and_ladders.py
```
or
```bash
python3 snakes_and_ladders.py
```

> You’ll see a welcome message and be asked to enter player names!

---

## 🎮 How to Play

1. **Choose the number of players** (minimum 2, maximum 4).
2. **Enter player names** when prompted.
3. Each player takes turns rolling the dice by pressing **ENTER**.
4. The player's position updates on the board.
   - If you land on a **ladder**, you move up.
   - If you land on a **snake**, you go down.
5. To **win the game**, you must land **exactly** on square 100.
   - If your dice roll goes past 100, your turn is skipped.

After someone wins, you can choose to **play again** or **exit the game**.

---

## 🖥️ Example Gameplay

```text
Welcome to Complex Snakes and Ladders!
Enter number of players (2–4): 2
Enter name for Player 1: Alice
Enter name for Player 2: Bob

--- Alice's Turn ---
Press ENTER to roll the dice...
You rolled a 5!
Alice moves to 5

--- Bob's Turn ---
Press ENTER to roll the dice...
You rolled a 6!
Bob moves to 6
Yay! Climbed a ladder to 25
```

---

## 🐍 Snakes and 🪜 Ladders Positions

### Snakes:
| From | To  |
|------|-----|
| 99   | 54  |
| 95   | 72  |
| 87   | 57  |
| 70   | 55  |
| 62   | 19  |
| 52   | 42  |
| 25   | 2   |

### Ladders:
| From | To  |
|------|-----|
| 3    | 22  |
| 6    | 25  |
| 11   | 40  |
| 17   | 69  |
| 46   | 90  |
| 60   | 85  |
| 63   | 95  |

---

## 💡 Tips

- Use a **terminal with color support** (e.g., Command Prompt, Terminal, VS Code, etc.).
- Make your terminal **fullscreen** or large enough to view the board comfortably.
- Have fun competing with friends or family!

---

## 📌 Troubleshooting

| Problem                      | Solution                                                   |
|-----------------------------|------------------------------------------------------------|
| `python not found` error    | Try using `python3` instead of `python`                   |
| Board looks misaligned      | Use a monospace font or run in a wider terminal window    |
| No colors in terminal       | Use a terminal that supports ANSI escape codes (most do)  |

---

## 🧠 Future Ideas (Optional Upgrades)

- Save/load game progress  
- Add player icons or emojis  
- Include sound effects or background music  
- Turn this into a GUI-based game using `tkinter`  
- Online multiplayer with sockets

---

## 👨‍💻 Author

This game was written in Python as a fun terminal-based project.  
Feel free to expand, share, or fork it!

---

## 📜 License

This project is open-source and free to use or modify.

---
