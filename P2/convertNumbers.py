"""Module to read numbers from a file and convert them to binary and hexadecimal."""
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
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Invalid data found and skipped: {line.strip()}")
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    return numbers

def to_binary(number):
    """Converts a number to its binary representation as a string."""
    if number == 0:
        return "0"
    is_negative = number < 0
    numb_temp = abs(number)
    binary = ""
    while numb_temp > 0:
        binary = str(numb_temp % 2) + binary
        numb_temp //= 2
    if is_negative:
        binary = "-" + binary
    return binary


def to_hexadecimal(number):
    """Converts a number to its hexadecimal representation as a string."""
    if number == 0:
        return "0"
    is_negative = number < 0
    numb_temp = abs(number)
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while numb_temp > 0:
        hexadecimal = hex_chars[numb_temp % 16] + hexadecimal
        numb_temp //= 16
    if is_negative:
        hexadecimal = "-" + hexadecimal
    return hexadecimal


def main():
    """Main function to handle file input and output processing."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("No valid data to process.")
        sys.exit(1)

    results = ""
    for num in numbers:
        binary = to_binary(num)
        hexadecimal = to_hexadecimal(num)
        results += f"Number: {num} | Binary: {binary} | Hexadecimal: {hexadecimal}\n"

    elapsed_time = time.time() - start_time
    results += f"Execution Time: {elapsed_time:.5f} seconds\n"

    print(results)
    with open("ConvertionResults.txt", "w", encoding="utf-8") as output_file:
        output_file.write(results)

if __name__ == "__main__":
    main()
