from typing import Dict


def character_count(s: str) -> Dict[str, int]:
    char_count = {}
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count


if __name__ == "__main__":
    input = input("Enter a string: ")
    counts = character_count(input)
    print(counts)
