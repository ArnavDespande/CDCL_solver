class Trail:
    def __init__ (self, value, reason, predecessor=None):
        self.value = value
        self.reason = reason
        self.predecessor = predecessor


def get_decision_level(trail_node):
    decision_level = 0
    while trail_node is not None:
        if (trail_node.reason == "DECISION"):
            decision_level += 1
        trail_node = trail_node.predecessor
    return decision_level