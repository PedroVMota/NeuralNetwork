from .Neurons import Neuron, InputNeuron, HiddenNeuron, OutputNeuron



class Layer:
    def __init__(self, NumberOfNeurons: int, isInputLayer: bool = False, isActivationLayer: bool = False ):
        self.Nodes: list[Neuron] = []
        self.isInputLayer = isInputLayer
        self.isActivationLayer = isActivationLayer
        for i in range(NumberOfNeurons):
            if isInputLayer:
                self.Nodes.append(InputNeuron())
            elif isActivationLayer:
                self.Nodes.append(OutputNeuron())
            else:
                self.Nodes.append(HiddenNeuron())
                 
    
