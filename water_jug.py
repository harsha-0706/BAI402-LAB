class WaterJugState:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))


def dfs(state, visited, j1, j2, target):
    if state.jug1 == target or state.jug2 == target:
        print("Target reached!")
        return True

    visited.add(state)

    operations = [
        (j1, state.jug2),
        (state.jug1, j2),
        (0, state.jug2),
        (state.jug1, 0),
        (max(0, state.jug1 + state.jug2 - j2),
         min(j2, state.jug1 + state.jug2)),
        (min(j1, state.jug1 + state.jug2),
         max(0, state.jug1 + state.jug2 - j1))
    ]

    for nj1, nj2 in operations:
        new_state = WaterJugState(nj1, nj2)
        if new_state not in visited:
            if dfs(new_state, visited, j1, j2, target):
                return True
    return False


j1 = int(input("Jug1: "))
j2 = int(input("Jug2: "))
target = int(input("Target: "))

dfs(WaterJugState(0, 0), set(), j1, j2, target)
