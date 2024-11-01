from Utils import *


def main():
    inputNeuron = Layer(2, isInputLayer=True)
    inputNeuron.Nodes[0].set_value(0.5)
    inputNeuron.Nodes[1].set_value(-0.3)
    hiddenLayer = Layer(2)
    hiddenLayer.Nodes[0].addWeight([0.8, -0.5])
    hiddenLayer.Nodes[0].set_bias(0.2)

    hiddenLayer.Nodes[1].addWeight([-0.6, 0.9])
    hiddenLayer.Nodes[1].set_bias(-0.2)

    outputLayer = Layer(1, isActivationLayer=True)
    outputLayer.Nodes[0].addWeight([1.2, -1.0])
    outputLayer.Nodes[0].set_bias(-1.0)

    NeuralNetwork(inputNeuron, hiddenLayer, outputLayer).start()



if __name__ == "__main__":
    main()