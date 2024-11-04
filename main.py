import Utils
# utils has theses class = ['NeuralNetwork', 'InputNeuron', 'HiddenNeuron', 'OutputNeuron', 'Layer']


def main():

    # Create a new instance of the Utils class
    InputNeural = Utils.Layer(3, isInputLayer=True)
    HiddenNeural = Utils.Layer(3)
    OutputNeural = Utils.Layer(1, isActivationLayer=True)


    HiddenNeural.Nodes[0].weights = [0.8, -0.5, 1.2]
    HiddenNeural.Nodes[0].bias = 0.2

    HiddenNeural.Nodes[1].weights = [-0.4, 1.0, 0.6]
    HiddenNeural.Nodes[1].bias = -0.1

    HiddenNeural.Nodes[2].weights = [0.5, -0.8, 0.9]
    HiddenNeural.Nodes[2].bias = 0.5


    OutputNeural.Nodes[0].weights = [0.9, -0.7, 1.3]
    OutputNeural.Nodes[0].bias = 0.1


    # Create a new instance of the NeuralNetwork class
    NeuralNetwork = Utils.NeuralNetwork(InputNeural, [HiddenNeural], OutputNeural)

    NeuralNetwork.start([0.5, -1.2, 0.3])

    pass


if __name__ == "__main__":
    main()
