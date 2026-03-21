def max_window_sum(values, k):
    if k > len(values):
        return 0

    window_sum = sum(values[:k])
    best = window_sum

    for i in range(k, len(values)):
        window_sum += values[i] - values[i - k]
        best = max(best, window_sum)
    return best


values = [2, 1, 5, 1, 3, 2]
print("Maximum sum of window size 3:", max_window_sum(values, 3))
