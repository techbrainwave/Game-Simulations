# Game Simulation using Python - Project 29
"""
To determine the expected number (and maybe even the distribution) of cycles the game will last
for. Use "first-step" analysis to get the expected value. Use simulation to get the entire distribution.
"""

import numpy as np
from matplotlib import pyplot as plt


def play_game():
    """
    Returns: cycle_count

    Play Game Once
    There are two players, A and B. At the beginning
    of the game, each starts with 4 coins, and there are 2 coins in the pot. A goes first,
    then B, then A,. . . . During a particular player's turn, the player tosses a 6-sided
    die. If the player rolls a:
    _ 1, then the player does nothing.
    _ 2: then the player takes all coins in the pot.
    _ 3: then the player takes half of the coins in the pot (rounded down).
    _ 4,5,6: then the player puts a coin in the pot.

    A player loses (and the game is over): if they are unable to perform the task (i.e.,
    if they have 0 coins and need to place one in the pot).

    Cycle: We define a cycle as A and
    then B completing their turns. The exception is if a player goes out; that is the
    final cycle (but it still counts as the last cycle).
    """
    cycle_count = 0
    a_coins = 4
    b_coins = 4
    pot_coins = 2
    # print(a_coins, b_coins, pot_coins)

    while True:

        # Player A
        throw = np.random.randint(1,7,1)
        # print("Throw-001:",throw)
        if throw!= 1:

            if throw == 2:
                a_coins = a_coins + pot_coins
                pot_coins = 0

            elif throw == 3:
                extra = np.floor_divide(pot_coins,2)

                a_coins = a_coins + extra
                pot_coins = pot_coins - extra

            else: # 4,5,6
                if a_coins == 0:
                    cycle_count += 1
                    break
                else:
                    a_coins -= 1
                    pot_coins += 1

        else: # if 1, do nothing
            pass

        # print(a_coins,b_coins,pot_coins)
        # Player B
        throw = np.random.randint(1,7,1)
        # print("Throw2:",throw)
        if throw!= 1:

            if throw == 2:
                b_coins = b_coins + pot_coins
                pot_coins = 0

            elif throw == 3:
                extra = np.floor_divide(pot_coins,2)

                b_coins = b_coins + extra
                pot_coins = pot_coins - extra

            else: # 4,5,6
                if b_coins == 0:
                    cycle_count += 1
                    break
                else:
                    b_coins -= 1
                    pot_coins += 1

        else: # if 1, do nothing
            pass

        # print(a_coins,b_coins,pot_coins)
        cycle_count += 1


    return cycle_count



def run_simulations(game_count):
    """

    Args:
        game_count:

    Returns:
        cycle_counts[]

    Run the play_game() as many as game_count times and return the average of cycle counts
    """
    total_count = 0
    all_cycles = np.array([], dtype=np.int64)

    for id in range(0, game_count):
        count = play_game()
        # print("Cycles:",count)
        total_count += count
        all_cycles = np.append(all_cycles,count)

    cycle_counts = total_count / game_count



    # Display Histogram
    print(np.bincount(all_cycles))

    plt.hist(all_cycles, bins='auto')
    plt.ylabel("Frequency")
    plt.xlabel("Cycle Count")
    plt.title("Cycle Count Distribution")
    plt.axhline(cycle_counts,color='orange')
    # plt.show()
    plt.savefig("Graph.png")


    return cycle_counts




if __name__ == "__main__":


    cycle_100 = run_simulations(100)
    cycle_2500 = run_simulations(2500)

    print("100 Simulations:",cycle_100)
    print("2500 Simulations:",cycle_2500)
    # print(cycle_400)