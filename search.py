# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    openSpace:
    Path found with total cost of 298 in 0.0 seconds
    Search nodes expanded: 576
    Pacman emerges victorious! Score: 212
    Average Score: 212.0
    Scores:        212.0
    Win Rate:      1/1 (1.00)
    Record:        Win
    """

    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Because of DFS, we need a stack as fringe. stack = LIFO queue
    fringe = util.Stack()
    # tinyMaze: (5,5) is the start state
    startState = problem.getStartState()
    fringe.push((startState, []))

    # to implement DFS as graph search, we need a list to store the already explored states
    visited = []

    while not fringe.isEmpty():
        item = fringe.pop()
        node = item[0]
        path = item[1]
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return path
            for s in problem.getSuccessors(node):
                newPath = path + [s[1]]
                fringe.push((s[0], newPath))


def breadthFirstSearch(problem):
    """
    openSpace:
    Path found with total cost of 54 in 0.0 seconds
    Search nodes expanded: 682
    Pacman emerges victorious! Score: 456
    Average Score: 456.0
    Scores:        456.0
    Win Rate:      1/1 (1.00)
    Record:        Win
    """

    # Because of BFS, we need a queue as fringe
    fringe = util.Queue()
    # (5,5)
    startState = problem.getStartState()
    fringe.push((startState, []))

    # to implement BFS as graph search, we need a list to store the already explored states
    visited = []

    while not fringe.isEmpty():
        item = fringe.pop()
        node = item[0]
        path = item[1]
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return path
            for s in problem.getSuccessors(node):
                newPath = path + [s[1]]
                fringe.push((s[0], newPath))

def uniformCostSearch(problem):
    """
    openMaze
    Path found with total cost of 54 in 0.1 seconds
    Search nodes expanded: 682
    Pacman emerges victorious! Score: 456
    Average Score: 456.0
    Scores:        456.0
    Win Rate:      1/1 (1.00)
    Record:        Win
    """


    # Because of UCS, we need a priority queue as fringe
    fringe = util.PriorityQueue()
    # (5,5)
    startState = problem.getStartState()
    fringe.push((startState, []), 0)

    # to implement UCS as graph search, we need a list to store the already explored states
    visited = []

    # UCS is quite simular to BFS, so we can reuse the algorithm beside we have to use the update method from
    # util.PriorityQueue(). Furthermore, we have to calculate the costs of a path
    while not fringe.isEmpty():
        item = fringe.pop()
        node = item[0]
        path = item[1]
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return path
            for s in problem.getSuccessors(node):
                newPath = path + [s[1]]
                cost = problem.getCostOfActions(newPath)
                fringe.update((s[0], newPath), cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    bigMaze:
    Path found with total cost of 210 in 0.1 seconds
    Search nodes expanded: 549
    Pacman emerges victorious! Score: 300
    Average Score: 300.0
    Scores:        300.0
    Win Rate:      1/1 (1.00)
    Record:        Win

    openMaze:
    Path found with total cost of 54 in 0.2 seconds
    Search nodes expanded: 535
    Pacman emerges victorious! Score: 456
    Average Score: 456.0
    Scores:        456.0
    Win Rate:      1/1 (1.00)
    Record:        Win

    A* expands the fewest nodes on openMaze (535). BFS and DFS expand the most nodes (682) on openMaze.
    DFS expands 576 nodes on openMaze with a total cost of 298 and a score of 212.

    A*, UCS, BFS and DFS have the best score of 54 on openMaze. 
    """

    """Search the node that has the lowest combined cost and heuristic first."""
    # we need a priority queue as fringe, because A* is quite the same as UCS, beside
    # that we use this heuristics in A*:
    # f(n) = g(n) + h(n) --> g(n) is the "UCS" portion
    fringe = util.PriorityQueue()
    # (5,5)
    startState = problem.getStartState()
    fringe.push((startState, []), heuristic)

    # to implement UCS as graph search, we need a list to store the already explored states
    visited = []

    # UCS is quite simular to BFS, so we can reuse the algorithm beside we have to use the update method from
    # util.PriorityQueue(). Furthermore, we have to calculate the costs of a path
    while not fringe.isEmpty():
        item = fringe.pop()
        node = item[0]
        path = item[1]
        """
        if a node is not in visited, it has to be explored. Then, it could be a successor of the current
        node.
        
        In case that the freshly popped node is already in visited, we must not explore it again because it
        was a successor of an already explored node
        """
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return path
            for s in problem.getSuccessors(node):
                newPath = path + [s[1]]
                # f(n) = getCostOfActions + heuristics(s[0], problem)
                #      = g(n) + h(n)
                cost = problem.getCostOfActions(newPath) + heuristic(s[0], problem)
                fringe.update((s[0], newPath), cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
