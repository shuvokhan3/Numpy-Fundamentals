import numpy as np

score = [
    [1,3,4],
    [2,4,6],
    [3,5,7],
    [4,6,8]
]

def normalize_scores(scores: list[list[int]]) -> float:
    # Convert input list to NumPy array
    test_score = np.array(scores, dtype=float)

    # Calculate column-wise mean
    sub_mean = test_score.mean(axis=0, keepdims=True)

    # Normalize using broadcasting
    normalized_score = test_score - sub_mean

    # Final result
    final_result = round(float(normalized_score.mean()), 2)
    return final_result

value = normalize_scores(score)
print(value)