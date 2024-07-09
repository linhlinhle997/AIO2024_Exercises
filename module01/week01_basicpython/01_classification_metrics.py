from typing import Dict


def validate_input(counts_dict: Dict[str, int]) -> bool:
    for key, value in counts_dict.items():
        if not isinstance(value, int):
            print(f"Error: {key} must be an integer")
            return False
        if value <= 0:
            print(f"Error: {key} must be zero or greater")
            return False
    return True


def calculate_metrics(tp: int , fp: int , fn: int) -> None:
    counts_dict = {'tp': tp, 'fp': fp, 'fn': fn}
    
    if not validate_input(counts_dict):
        return

    # Calculate precision, recall, and F1 score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F1 Score: ", f1_score)


if __name__ == "__main__":
    calculate_metrics(tp=2, fp=3, fn=4)
