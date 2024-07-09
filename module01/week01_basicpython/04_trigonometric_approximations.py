def factorial(number: int) -> int:
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def approx_sin(x: float, n: int) -> float:
    return pow(-1, n) * pow(x, 2 * n+1) / factorial(2 * n+1)


def approx_cos(x: float, n: int) -> float:
    return pow(-1, n) * pow(x, 2*n) / factorial(2*n)


def approx_sinh(x: float, n: int) -> float:
    return pow(x, 2 * n+1) / factorial(2 * n+1)


def approx_cosh(x: float, n: int) -> float:
    return pow(x, 2*n) / factorial(2*n)


def calculate(x: float, n: int) -> None:
    sin = sum(approx_sin(x, i) for i in range(n))
    cos = sum(approx_cos(x, i) for i in range(n))
    sinh = sum(approx_sinh(x, i) for i in range(n))
    cosh = sum(approx_cosh(x, i) for i in range(n))
    
    print(f"sin({x}) = {sin}")
    print(f"cos({x}) = {cos}")
    print(f"sinh({x}) = {sinh}")
    print(f"cosh({x}) = {cosh}")


if __name__ == "__main__":
    try:
        x = float(input("x: "))
        n = int(input("n: "))

        if n < 0:
            raise ValueError("n must be a positive integer")

        calculate(x, n)
    except ValueError  as e:
        print(f"Invalid input: {e}")
