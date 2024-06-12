from typing import List


def find_max_in_sublists(num_list: List[int], k: int) -> List[int]:
    max_values = []
    for i in range(len(num_list) - k + 1):
        max_values.append(max(num_list[i:i+k]) )
    return max_values


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    max_values = find_max_in_sublists(num_list, k)
    print(max_values)
