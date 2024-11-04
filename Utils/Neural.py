from Utils.Layer import Layer


class NeuralNetwork:
    def __init__(
            self,
            inputLayer: Layer,
            hiddenLayers: list[Layer],
            outputLayer: Layer
    ):
        self.inputLayer = inputLayer
        self.hiddenLayers = hiddenLayers
        self.outputLayer = outputLayer

    def start(self, inputs: list[float]) -> list[float]:

        print("Starting Neural Network")

        # Set input values to input layer neurons
        for i, value in enumerate(inputs):
            self.inputLayer.Nodes[i].set_value(value)
        
        print("All input values: ", [neuron.outputValue for neuron in self.inputLayer.Nodes])

        # Forward propagate through input layer
        current_outputs = [neuron.outputValue for neuron in self.inputLayer.Nodes]


        print("All Weight of each neuron in the hidden layer: ", [neuron.weights for neuron in self.hiddenLayers[0].Nodes])
        print("All Bias of each neuron in the hidden layer: ", [neuron.bias for neuron in self.hiddenLayers[0].Nodes])
        
        # Forward propagate through hidden layers
        for hidden_layer in self.hiddenLayers:
            current_outputs = hidden_layer.forwardPropagation(current_outputs)


        print("All Weight of each neuron in the output layer: ", [neuron.weights for neuron in self.outputLayer.Nodes])


        
        # Forward propagate through output layer
        final_outputs = self.outputLayer.forwardPropagation(current_outputs)

        print("All output values: ", list(final_outputs))
        return [neuron.outputValue for neuron in self.outputLayer.Nodes]
    
    def __iter__(self):
        yield self.inputLayer
        yield from self.hiddenLayers
        yield self.outputLayer
    
    def end(self):
        raise NotImplementedError("End method not implemented")
    
    def train(self):
        raise NotImplementedError("Train method not implemented")
    
    def test(self):
        raise NotImplementedError("Test method not implemented")

