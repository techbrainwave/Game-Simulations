# Simulation

Simulation involves modeling and creating artificial representations of real-world systems to understand their behavior or make predictions. 

Simulation study has many applications. One such ap-
plication is in the area of game development. In this work a pro-
gram oriented simulation of a two player game is conducted with
the goal of finding out the duration to which it would last. While
a simulation provided empirical results on a fixed set of runs of the
game, an application of an analytical method derived the expected
value for the duration of each game. Distribution of frequencies for
the number of cycles of a game set in the simulations were com-
puted and visualized as histograms.

## Markov chain
Any stochastic process that possesses the Markov property is called a
Markov chain.

## The Game 

>There are two players, A and B. At the beginning
of the game, each starts with 4 coins, and there are 2 coins in the pot. A goes first,
then B, then A,. . . . During a particular player's turn, the player tosses a 6-sided
die. If the player rolls a:
_ 1, then the player does nothing.
_ 2: then the player takes all coins in the pot.
_ 3: then the player takes half of the coins in the pot (rounded down).
_ 4,5,6: then the player puts a coin in the pot.

>A player loses (and the game is over): if they are unable to perform the task (i.e.,
if they have 0 coins and need to place one in the pot).

## Cycle
We define a cycle as A and
then B completing their turns. The exception is if a player goes out; that is the
final cycle (but it still counts as the last cycle).


<img src="https://github.com/techbrainwave/Game-Simulation/blob/main/cycle-count.png" alt="cycle count" width="300"/>

## Simulation Run

1. Open a Python console (Python version 3.7 or later) and navigate to the directory containing the file `anothergame.py`.
2. Run the command `python anothergame.py`
3. Results will be displayed and the histogram will be downloaded as image in the same directory. 
