import random

# Team names
team_cubs = "Cubs"
team_sox = "Sox"

# Win probabilities (Cubs slightly stronger)
cubs_win_prob = 0.55
sox_win_prob = 0.45

# Simulate 1000 games
num_games = 1000
cubs_wins = 0
sox_wins = 0

for _ in range(num_games):
    if random.random() < cubs_win_prob:
        cubs_wins += 1
    else:
        sox_wins += 1

# Show results
print(f"Out of {num_games} games:")
print(f"{team_cubs} won {cubs_wins} games")
print(f"{team_sox} won {sox_wins} games")
