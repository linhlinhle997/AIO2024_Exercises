from collections import Counter
from typing import Dict


def count_words_in_file(file_path: str) -> Dict[str, int]:
    with open(file_path, "r") as file:
        contents  = file.read().lower()
        words = contents.split()
    word_counter = Counter([word for word in words])
    return dict(word_counter)


if __name__ == "__main__":
    file_path = "./content/P1_data.txt"
    word_counts  = count_words_in_file(file_path)
    print(word_counts)
