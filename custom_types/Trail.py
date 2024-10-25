class TrailNode:
    def __init__ (self, value, reason, map_snapshot=None, predecessor=None, both_paths_killed=False, son_node=None, daughternode=None):
        self.value = value
        self.reason = reason
        self.map_snapshot = map_snapshot
        self.predecessor = predecessor
        self.dead = both_paths_killed
        self.son = son_node
        self.daughter = daughternode

    def printNode(self):
        if (self.reason == "DECISION"):
            print(self.value, " ", self.reason)


def get_decision_level(trail_node):
    decision_level = 0
    while trail_node is not None:
        if (trail_node.reason == "DECISION"):
            decision_level += 1
        trail_node = trail_node.predecessor
    return decision_level