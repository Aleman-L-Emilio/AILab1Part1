# Lab 1, Part 2a: Heuristics.
# Name(s): 
from search_heuristics import *
from slidepuzzle_problem import *

INF = float('inf')

#### Lab 1, Part 2a: Heuristics #################################################

# Implement these two heuristic functions for SlidePuzzleState.

""" Return the Hamming distance (number of tiles out of place) of the SlidePuzzleState """
def slidepuzzle_hamming(state : SlidePuzzleState)  -> float:
    distance = 0
    state_size = state.get_size()

    for row in range(state_size):
        for col in range(state_size):
            if state.tiles[row][col] != 0 and state.tiles[row][col] != row*state_size + col:
                    distance += 1

    return distance

""" Return the sum of Manhattan distances between tiles and goal of the SlidePuzzleState """
def slidepuzzle_manhattan(state : SlidePuzzleState)  -> float:
    distance = 0
    state_size = state.get_size()

    for row in range(state_size):
        for col in range(state_size):
            if state.tiles[row][col] != 0 and state.tiles[row][col] != row*state_size  + col:
                #Asked peer in class about this formula
                distance = distance + abs(row - (state.tiles[row][col] // state_size)) + abs(col - (state.tiles[row][col] % state_size))

    return distance

SLIDEPUZZLE_HEURISTICS = {
    "Zero" : zero_heuristic, 
    "Arbitrary": arbitrary_heuristic, 
    "Hamming" : slidepuzzle_hamming,
    "Manhattan" : slidepuzzle_manhattan
    }

