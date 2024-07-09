import math
import torch


class SoftmaxCalculator:
    def __init__(self, data: torch.Tensor) -> None:
        self.data = data

    def _softmax(self, x: float) -> float:
        exp_values = [math.exp(j) for j in self.data]
        return math.exp(x) / sum(exp_values)

    def _stable_softmax(self, x: float, max_val: float) -> float:
        exp_values = [math.exp(j - max_val) for j in self.data]
        return math.exp(x - max_val) / sum(exp_values)

    def compute_softmax(self) -> torch.Tensor:
        result = [self._softmax(i) for i in self.data]
        return torch.Tensor(result)

    def compute_stable_softmax(self) -> torch.Tensor:
        max_val = max(self.data)
        result = [self._stable_softmax(i, max_val) for i in self.data]
        return torch.Tensor(result)


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax_instance = SoftmaxCalculator(data)

    softmax_result = softmax_instance.compute_softmax()
    print(f"Softmax: {softmax_result}")

    stable_softmax_result = softmax_instance.compute_stable_softmax()
    print(f"Stable softmax: {stable_softmax_result}")
