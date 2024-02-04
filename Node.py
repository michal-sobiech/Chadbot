class Node:
    prev_node: Node = None
    next_node: Node = None

    def __init__(self, prev_node: Node, next_node: Node) -> None:
        self.prev_node = prev_node
        self.next_node = next_node