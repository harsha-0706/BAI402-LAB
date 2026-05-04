import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, h=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.h = h

    def __lt__(self, other):
        return (self.cost + self.h) < (other.cost + other.h)


def astar(start, goal):
    def heuristic(s):
        return {"A":3,"B":2,"C":1,"D":0}[s]

    def successors(s):
        graph = {
            "A":[("B",1),("C",3)],
            "B":[("C",1),("D",2)],
            "C":[("D",1)]
        }
        return graph.get(s, [])

    pq = []
    heapq.heappush(pq, Node(start, None, 0, heuristic(start)))

    visited = set()

    while pq:
        node = heapq.heappop(pq)

        if node.state == goal:
            print("Goal reached:", goal)
            return

        visited.add(node.state)

        for nxt, cost in successors(node.state):
            if nxt not in visited:
                heapq.heappush(pq, Node(nxt, node, node.cost + cost, heuristic(nxt)))


astar("A", "D")
