from RNN.Node import Node


class Connection:
    weight: float = None
    bias: float = None
    src_node: Node = None
    dest_node: Node = None

    def __init__(self, weight: float, bias: float,
                 src_node: Node, dest_node: Node) -> None:
        self.weight = weight
        self.bias = bias
        self.src_node = src_node
        self.dest_node = dest_node