import Utils
# utils has theses class = ['NeuralNetwork', 'InputNeuron', 'HiddenNeuron', 'OutputNeuron', 'Layer']

def main():
    # Create a new instance of the Utils class
    InputNeural = Utils.Layer(2, isInputLayer=True)
    HiddenNeural = Utils.Layer(2)
    OutputNeural = Utils.Layer(1, isActivationLayer=True)

    InputNeural.Nodes[0].outputValue = 0.1
    InputNeural.Nodes[1].outputValue = 0.2

    HiddenNeural.Nodes[0].weights = [0.1, 0.2]
    HiddenNeural.Nodes[0].bias = 0.1

    HiddenNeural.Nodes[1].weights = [0.1, 0.2]
    HiddenNeural.Nodes[1].bias = 0.1
    

    # Create a new instance of the NeuralNetwork class
    NeuralNetwork = Utils.NeuralNetwork(InputNeural, HiddenNeural, OutputNeural)

    pass

if __name__ == "__main__":
    main()