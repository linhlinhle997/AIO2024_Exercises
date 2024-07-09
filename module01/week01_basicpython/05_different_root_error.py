def nth_root_error(y: float, y_hat: float, n: int, p: int) -> None:
    error = pow(pow(y, 1/n) - pow(y_hat, 1/n), p)
    print(error)


if __name__ == "__main__":
    y, y_hat = 100, 99.5
    n, p = 2, 1

    nth_root_error(y, y_hat, n, p)
