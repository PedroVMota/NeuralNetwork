from Layer import Layer



class NeuralNetwork:
    def __init__(
            self,
            inputLayer: Layer,
            hiddenLayer: Layer,
            outputLayer: Layer
    ):
        self.inputLayer = inputLayer
        self.hiddenLayer = hiddenLayer
        self.outputLayer = outputLayer

    def start(self):
        raise NotImplementedError("Start method not implemented")
    
    def end(self):
        raise NotImplementedError("End method not implemented")
    
    def train(self):
        raise NotImplementedError("Train method not implemented")
    
    def test(self):
        raise NotImplementedError("Test method not implemented")
        