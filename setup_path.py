from __future__ import annotations
import numpy as np
import config

# It's a type hint that tells the IDE that the variable `Path` is a list of tuples of integers.
Path = list[tuple[int, int]]

# It's loading a text file that contains a grid of numbers.
grid = np.loadtxt("./board.txt", delimiter=" ")

# A list of tuples that represent the four directions that the algorithm can move in.
delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # up, left, down, right


# A Node is a class that has a position, a goal, and a parent
class Node:
    def __init__(
        self, pos_x: int, pos_y: int, goal_x: int, goal_y: int, parent: Node | None
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.parent = parent


# It takes a start and goal position, and returns a path from the start to the goal.
class BreadthFirstSearch:

    def __init__(self, start: tuple[int, int], goal: tuple[int, int]):
        #It's creating a Node object with the start position, the goal position, and a parent of None.
        self.start = Node(start[1], start[0], goal[1], goal[0], None)
        # It's creating a Node object with the goal position, the goal position, and a parent of None.
        self.target = Node(goal[1], goal[0], goal[1], goal[0], None)

        # It's creating a list with the start node.
        self.node_queue = [self.start]
        # It's a boolean variable that tells the algorithm if it has reached the goal.
        self.reached = False

    def get_successors(self, parent: Node) -> list[Node]:
        successors = []
        for action in delta:
            pos_x = parent.pos_x + action[1]
            pos_y = parent.pos_y + action[0]
            if not (0 <= pos_x <= len(grid[0]) - 1 and 0 <= pos_y <= len(grid) - 1):
                continue
            if grid[pos_y][pos_x] != 0:
                continue
            successors.append(
                Node(pos_x, pos_y, self.target.pos_y, self.target.pos_x, parent)
            )
        return successors

    def retrace_path(self, node: Node | None) -> Path:
        current_node = node
        path = []
        while current_node is not None:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        return path


# It's a bidirectional breadth first search that uses two BreadthFirstSearch objects to search from
# the start and goal nodes simultaneously
class BidirectionalBreadthFirstSearch:

    def __init__(self, start, goal):
        self.fwd_bfs = BreadthFirstSearch(start, goal)
        self.bwd_bfs = BreadthFirstSearch(goal, start)

    def search(self) -> Path | None:
        for i in range(10):
            new_queue = []
            for node in self.fwd_bfs.node_queue:
                childs = self.fwd_bfs.get_successors(node)
                for child in childs:
                    # Comparison
                    for bwd_node in self.bwd_bfs.node_queue:
                        if child.pos == bwd_node.pos:
                            return self.retrace_bidirectional_path(
                                child, bwd_node
                            )
                    ##
                    new_queue.append(child)
            self.fwd_bfs.node_queue = new_queue
                
            new_queue = []
            for node in self.bwd_bfs.node_queue:
                childs = self.bwd_bfs.get_successors(node)
                for child in childs:
                    # Comparison
                    for fwd_node in self.fwd_bfs.node_queue:
                        if child.pos == fwd_node.pos:
                            return self.retrace_bidirectional_path(
                                fwd_node, child
                            )
                    ##
                    new_queue.append(child)
            self.bwd_bfs.node_queue = new_queue
        # The case that there is no solution at the established depth is handled. 
        return

    def viewList(self, list):
        for node in list:
            print(node.pos)

    def retrace_bidirectional_path(self, fwd_node: Node, bwd_node: Node) -> Path:
        fwd_path = self.fwd_bfs.retrace_path(fwd_node)
        bwd_path = self.bwd_bfs.retrace_path(bwd_node)
        bwd_path.pop()
        bwd_path.reverse()
        path = fwd_path + bwd_path
        print(path)
        print("Intersect: ", fwd_node.pos)
        return path


# all coordinates are given in format [y,x]
init = config.playerCoords
goal = config.metaCoords

# It's creating a BidirectionalBreadthFirstSearch object with the start and goal positions, and
# then it's calling the `search` method of the object.
bd_bfs = BidirectionalBreadthFirstSearch(init, goal)
bd_path = bd_bfs.search()

# It's saving the path to a text file.
np.savetxt("./path.txt",bd_path, fmt='%i')

print("The path was found. Executing display window. Log in path.txt")