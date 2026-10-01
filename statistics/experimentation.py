import math


def compute_mean(values):
    return sum(values) / len(values)


def compute_stddev(values):
    mean = compute_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)


def z_score(value, mean, stddev):
    if stddev == 0:
        return 0
    return (value - mean) / stddev


def confidence_interval(mean, stddev, n, z=1.96):
    margin = z * (stddev / math.sqrt(n))
    return mean - margin, mean + margin


if __name__ == "__main__":
    values_a = [100, 110, 105, 98, 102]
    values_b = [115, 110, 120, 118, 109]

    mean_a = compute_mean(values_a)
    mean_b = compute_mean(values_b)
    std_a = compute_stddev(values_a)
    std_b = compute_stddev(values_b)

    print(f"Mean A: {mean_a}")
    print(f"Mean B: {mean_b}")
    print(f"Std dev A: {std_a}")
    print(f"Std dev B: {std_b}")

    ci_a = confidence_interval(mean_a, std_a, len(values_a))
    ci_b = confidence_interval(mean_b, std_b, len(values_b))
    print(f"95% CI A: {ci_a}")
    print(f"95% CI B: {ci_b}")
