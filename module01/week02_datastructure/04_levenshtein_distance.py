from typing import List


def levenshtein_distance(str1: str, str2: str) -> int:
    matrix: List[List[int]] = []
    for _ in range(len(str1) + 1):
        matrix.append([0] * (len(str2) + 1) )

    for i in range(len(str1) + 1):
       for j in range(len(str2) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                if str1[i-1] == str2[j-1]:
                    cost = 0
                else:
                    cost = 1

                matrix[i][j] = min(matrix[i-1][j] + 1,
                                   matrix[i][j-1] + 1,
                                   matrix[i-1][j-1] + cost)
    return matrix[-1][-1]


if __name__ == "__main__":
    str1, str2 = 'kitten', 'sitting'
    distance = levenshtein_distance(str1, str2)
    print("Levenshtein distance: ", distance)
