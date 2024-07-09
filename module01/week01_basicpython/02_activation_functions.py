import math


def is_number(n: str) -> bool:
    try:
        float(n)
        return True
    except ValueError:
        return False


def valid_activation(activation: str) -> bool:
    return activation in ["sigmoid", "relu", "elu"]


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def relu(x: float) -> float:
    return max(0, x)


def elu(x: float, alpha: float = 0.01) -> float:
    return x if x > 0 else alpha * (math.exp(x) - 1)


def calculate_activations(x: float, activation: str) -> None:    
    if not valid_activation(activation):
        print(f"{activation} is not supported")
        return
    
    # Dictionary mapping activation functions
    activation_func = {"sigmoid": sigmoid, "relu": relu, "elu": elu}
    result = activation_func[activation](x)
    print(f"{activation}({x}) = {result}")


if __name__ == "__main__":
    x = input("Input x: ")
    if not is_number(x):
        print("x must be a number")
    else:
        activation = input("Input activation Function (sigmoid|relu|elu ): ")
        calculate_activations(float(x), activation)
