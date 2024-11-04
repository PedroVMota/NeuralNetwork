import random

class Neuron:
    def sigmoid(x: float) -> float:
        return 1 / (1 + pow(2.71828, -x))

        
    def __init__(self):
        self.outputValue: float = 0
        self.bias: float = random.uniform(-1, 1)  # Initialize bias with a random value between -1 and 1
        self.weights: list[float] = []

        
    def setWeights(self, weights: list[float]):
        self.weights = weights
    def setBias(self, bias: float):
        self.bias = bias
    def setOuputValue(self, value: float):
        self.outputValue = value

    def forwardPropagation(self, input_vector: list[float]):
        z = sum(weight * input_value for weight, input_value in zip(self.weights, input_vector)) + self.bias
        self.output_value = Neuron.sigmoid(z)
        return self.output_value


class InputNeuron(Neuron):
    def __init__(self):
        super().__init__()
    def set_value(self, value: float):
        self.outputValue = value
    def forwardPropagation(self, inputVector: list[Neuron]):
        return self.outputValue
    

    
class HiddenNeuron(Neuron):
    def __init__(self):
        super().__init__()
    
class OutputNeuron(Neuron):
    def __init__(self):
        super().__init__()
    

    def back_propagation(self, input_vector: list['Neuron']):
        raise NotImplementedError("Back Propagation not implemented")
