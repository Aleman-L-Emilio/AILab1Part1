# Name(s): Emilio L. Aleman and Vartan Yildiz

from search_heuristics import *
from spotlessroomba_problem import *

# TODO If applicable, argue for why this is admissible / consistent!
def spotlessroomba_first_heuristic(state : SpotlessRoombaState)  -> float:
    """
    Consistent, finds best path heuristic
    Method was created with help of peers in class, received a lot of help trying to make this method
    This heuristic returns distance to best start tile
    Roomba is able to phase through walls
    """
    if not state.dirty_locations:
        return 0
    
    best_start = 0
    best_cost = INF

    for i in range(len(state.dirty_locations)):
        estimate_cost = 0
        lowest_cost = INF
        closest_dirty = 0
        dirty_locations = list(state.dirty_locations)
        current_pos = dirty_locations.pop(i)

        while dirty_locations:
            for j in range(len(dirty_locations)):
                manhattan = abs(current_pos.row - dirty_locations[j].row) + abs(current_pos.col - dirty_locations[j].col)
                if manhattan < lowest_cost:
                    lowest_cost = manhattan
                    closest_dirty = j
            estimate_cost += lowest_cost
            current_pos = dirty_locations.pop(closest_dirty)
            lowest_cost = INF
        if estimate_cost < best_cost:
            best_cost = estimate_cost
            best_start = i
        if estimate_cost == best_cost:
            current_pos = state.position
            dist_to_prev_best = abs(current_pos.row - state.dirty_locations[best_start].row) + abs(current_pos.col - state.dirty_locations[best_start].col)
            dist_to_i = abs(current_pos.row - state.dirty_locations[i].row) + abs(current_pos.col - state.dirty_locations[i].col)
            if dist_to_i < dist_to_prev_best:
                best_start = i
    

    current_pos = state.position

    #Adapted from manhattan distance
    dist_to_start = abs(current_pos.row - state.dirty_locations[best_start].row) + abs(current_pos.col - state.dirty_locations[best_start].col)

    return dist_to_start + best_cost


def spotlessroomba_second_heuristic(state : SpotlessRoombaState)  -> float:
    """
    Admissible Hamming Heuristic
    Does not show too much of a performance boost in testing but it does not overestimate so it is admissible.
    """
    return len(state.dirty_locations)

# TODO if you wish, implement more heuristics!

# TODO Update heuristic names and functions below. If you make more than two, add them here.
SPOTLESSROOMBA_HEURISTICS = {"Zero" : zero_heuristic,
                        "Arbitrary": arbitrary_heuristic, 
                        "Custom Heur. 1": spotlessroomba_first_heuristic,
                        "Custom Heur. 2" : spotlessroomba_second_heuristic
                        }
