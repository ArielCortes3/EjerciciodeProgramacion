"""Module to read numbers from a file and compute basic statistical measures."""
# pylint: disable=invalid-name

import sys
import time

def read_numbers_from_file(filename):
    """Reads a list of numbers from a file, ignoring invalid entries."""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid data found and skipped: {line.strip()}")
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    return numbers

def compute_mean(numbers):
    """Computes the mean (average) of a list of numbers."""
    total = sum(numbers)
    return total / len(numbers)

def compute_median(numbers):
    """Computes the median of a list of numbers."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def compute_mode(numbers):
    """Computes the mode(s) of a list of numbers."""
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_freq]
    return modes

def compute_variance(numbers, mean):
    """Computes the variance of a list of numbers."""
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def compute_std_dev(variance):
    """Computes the standard deviation of a list of numbers."""
    return variance ** 0.5

def main():
    """Main function to handle file input and output processing."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("No valid data to process.")
        sys.exit(1)

    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = compute_std_dev(variance)
    elapsed_time = time.time() - start_time

    results = (
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {std_dev}\n"
        f"Execution Time: {elapsed_time:.5f} seconds\n"
    )

    print(results)
    with open("StatisticsResults.txt", "w", encoding="utf-8") as output_file:
        output_file.write(results)

if __name__ == "__main__":
    main()
