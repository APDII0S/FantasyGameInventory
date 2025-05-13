# Coin Flip Streaks
# Ace ~ 2025-03-09

# This program will flip a coin 10000 times, and find the odds of
# finding a streak of 6 heads/tails.

import random
streaks = 0
comboHeads= 0
comboTails = 0
coinFlips = []

def flipCoins(coinFlips):
    """Simulates 10,000 coin flips and stores result in `coinFlips`"""
    for i in range(10000):              
        if random.randrange(0, 2) == 0:
            coinFlips.append('H')
        else:
            coinFlips.append('T')

    print(coinFlips)    # Optional: Prints the entire sequence of coinflips. May be large.


def probabilityCalculation(streaks, comboHeads, comboTails, coinFlips):
    """Counts streaks of 6 in `coinFlips`, to calculate probability of finding streaks of 6"""

    for i in coinFlips:       
        if i == 'H':
            comboHeads += 1
            comboTails = 0  # Resets combo of tails, since combo of tails is broken
        
        elif i == 'T':
            comboTails += 1
            comboHeads = 0  # Resets combo of heads, since combo of heads is broken


        # `comboHeads` and `comboTails` get reset once either of them equal `6`. Increment `streaks` by 1
        if comboHeads == 6 or comboTails == 6:
            streaks += 1
            comboHeads = 0
            comboTails = 0


    print(f'Chance of streak is: {streaks / 100:.2f}%')    # Calculate and print probability of finding streaks of 6 in `coinFlips`
    print(f"Here is streak count total: {streaks}")

flipCoins(coinFlips)
probabilityCalculation(streaks, comboHeads, comboTails, coinFlips)
