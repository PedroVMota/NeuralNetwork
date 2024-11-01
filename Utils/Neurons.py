import numpy as np


class Neuron:
    def sigmoid(x: float) -> float:
        return 1 / (1 + np.exp(-x))
    
    def __init__(self):
        self.outputValue: float = 0
        self.bias: float = 0
        self.weights: list[float] = []

    def setWeights(self, weights: list[float]):
        self.weights = weights
    
    def setBias(self, bias: float):
        self.bias = bias
    
    def setOuputValue(self, value: float):
        self.outputValue = value


class InputNeuron(Neuron):
    def __init__(self):
        super().__init__()
    
    def set_value(self, value: float):
        self.outputValue = value

    
class HiddenNeuron(Neuron):
    def __init__(self):
        super().__init__()
    
    def forwardPropagation(self, inputVector: list[Neuron]):
        raise NotImplementedError("Forward Propagation not implemented")
    
    def backPropagation(self, inputVector: list[Neuron]):
        raise NotImplementedError("Back Propagation not implemented")
    
class OutputNeuron(Neuron):
    def __init__(self):
        super().__init__()
    
    def forwardPropagation(self, inputVector: list[Neuron]):
        raise NotImplementedError("Forward Propagation not implemented")
    
    def backPropagation(self, inputVector: list[Neuron]):
        raise NotImplementedError("Back Propagation not implemented")
    