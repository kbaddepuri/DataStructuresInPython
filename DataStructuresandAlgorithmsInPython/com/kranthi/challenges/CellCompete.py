"""
There is a colony of 8 cells arranged in a straight line where each day every cell competes with its adjacent
cells(neighbour). Each day, for each cell, if its neighbours are both active or both inactive, the cell becomes
inactive the next day,. otherwise it becomes active the next day.

Assumptions: The two cells on the ends have single adjacent cell, so the other adjacent cell can be assumed
to be always inactive. Even after updating the cell state. consider its previous state for updating the state of other
cells. Update the cell information of all cells simultaneously.

Write a function cellCompete which takes takes one 8 element array of integers cells representing the current state of 8
cells and one integer days representing te number of days to simulate. An integer value of 1 represents an active cell
and value of 0 represents an inactive cell.
"""


def cellCompete(states, elem_days):
    new = states[:]  # get a copy of the array
    n = len(states)

    for _ in range(elem_days):
        new[0] = states[1]  # determine the edge nodes first
        new[n - 1] = states[n - 2]

        for i in range(1, n - 1):
            new[i] = 1 - (states[i - 1] == states[i + 1])  # logic for the rest nodes
        states = new[:]  # update the list for the next day

    return new


arr = [1, 1, 1, 0, 1, 1, 1, 1]
days = 2
print(cellCompete(arr, days))
