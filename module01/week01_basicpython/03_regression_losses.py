import math
import random


def mae(predict: float, target: float) -> float:
    return abs(predict - target)


def mse(predict: float, target: float) -> float:
    return (predict - target) ** 2


def rmse(predict: float, target: float) -> float:
    return math.sqrt(mse(predict, target))


def calculate_loss(num_samples: int, loss_name: str) -> None:
    loss_func = {'MAE': mae, 'MSE': mse, 'RMSE': rmse}[loss_name]
    
    total_loss = 0.0
    for i in range(num_samples):
        predict, target = random.uniform(0, 10), random.uniform(0, 10)
        loss = loss_func(predict, target)
        total_loss += loss
        print(f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")
    print(f"Final {loss_name}: {total_loss / num_samples}")


if __name__ == "__main__":
    num_samples = input("Input number of samples (integer number) which are generated: ")
    loss_name = input("Input loss name (MAE|MSE|RMSE): ")

    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
    elif loss_name not in ["MAE", "MSE", "RMSE"]:
        print(f"{loss_name} is not supported")
    else:
        calculate_loss(int(num_samples), loss_name)
