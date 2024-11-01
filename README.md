Here's a README focused solely on the concepts, math, and definitions that make up a basic neural network:

---

# Neural Network Fundamentals

This README covers the essential components and math behind a simple neural network. This includes understanding what neurons, layers, activation functions, and backpropagation are, along with the formulas that govern each part of the network.

---

## 1. Neuron (Node)
- **Definition**: A neuron is a fundamental unit in a neural network that receives one or more inputs, processes them, and produces an output.
- **Mathematical Representation**:
  \[
  z = W \cdot x + b
  \]
  where:
  - \( W \): Weight of each input connection.
  - \( x \): Input vector.
  - \( b \): Bias term.
- **Purpose**: Neurons process inputs by adjusting weights and biases to minimize the error in predicting outcomes.

## 2. Layers
- **Input Layer**: Receives the initial data and passes it to the next layer.
- **Hidden Layer(s)**: Layers between the input and output layers that transform input data through weights, biases, and activations.
- **Output Layer**: Produces the final prediction or classification based on the transformed inputs.

## 3. Activation Function
- **Purpose**: Activation functions introduce non-linearity to allow the network to learn complex patterns.
- **Common Activation Functions**:
  - **Sigmoid**: Squeezes input values to a range between 0 and 1.
    \[
    \sigma(z) = \frac{1}{1 + e^{-z}}
    \]
  - **ReLU (Rectified Linear Unit)**: Outputs zero for negative values and identity for positive values.
    \[
    \text{ReLU}(z) = \max(0, z)
    \]

## 4. Forward Propagation
- **Concept**: The process of passing input data through the network, layer by layer, to generate predictions.
- **Formula** (for each neuron):
  \[
  a = \text{Activation}(W \cdot x + b)
  \]
  where \( a \) is the activated output.

## 5. Loss Function
- **Purpose**: Measures how well the network's predictions match the target values.
- **Examples**:
  - **Mean Squared Error (MSE)** (used in regression):
    \[
    L = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
    \]
  - **Cross-Entropy Loss** (used in classification):
    \[
    L = -\sum_{i} y_i \log(\hat{y}_i)
    \]
  where \( y_i \) is the true label, and \( \hat{y}_i \) is the predicted probability.

## 6. Backpropagation
- **Concept**: The method of computing the gradient of the loss function with respect to each weight by applying the chain rule.
- **Formula** (Gradient Descent Update):
  \[
  w = w - \eta \cdot \frac{\partial L}{\partial w}
  \]
  where:
  - \( \eta \): Learning rate.
  - \( \frac{\partial L}{\partial w} \): Gradient of the loss with respect to weight \( w \).

## 7. Gradient Descent
- **Purpose**: Optimization algorithm used to update weights and biases to minimize the loss.
- **Formula** (Gradient Descent Update for each weight and bias):
  \[
  w = w - \eta \cdot \frac{\partial L}{\partial w}
  \]
  \[
  b = b - \eta \cdot \frac{\partial L}{\partial b}
  \]
  where \( \eta \) is the learning rate that controls how big each step is.

---

