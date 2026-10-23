
values = [2, 4, 4, 4, 5, 5, 7, 9]

# def mean(values):
#     return sum(values) / len(values)

# def median(values):
#     sorted_values = sorted(values)
#     n = len(sorted_values)
#     mid = n // 2
#     if n % 2 == 0:
#         return (sorted_values[mid - 1] + sorted_values[mid]) / 2
#     else:
#         return sorted_values[mid]

# def std_dev(values):
#     mean_value = mean(values)
#     return sum((x - mean_value) ** 2 for x in values) / len(values) ** 0.5


def min_max(values):
    low = high = values[0]
    for n in values[1:]:
        if n < low:
            low = n
        else:
            n > high:
            high = n
    return low, high
minmax = min_max(values)
print(minmax)

# def summary(values):
#     return {
#         "mean": mean(values),
#         "median": median(values),
#         "std_dev": std_dev(values),
#         "min": min(values),
#         "max": max(values)
#     }