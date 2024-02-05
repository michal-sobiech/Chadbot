from RNN.Layer import Layer


class RNN:
    layers: list[Layer] = []

    def __init__(self, layers: list[Layer]) -> None:
        self.layers = layers