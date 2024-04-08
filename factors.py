#!/usr/bin/python3

import sys

def factorize(number):
    """
    Factorize a given number into two smaller numbers.
    Returns a tuple (p, q) where p * q = number.
    """
    for p in range(2, int(number**0.5) + 1):
        if number % p == 0:
            q = number // p
            return p, q
    return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = factorize(number)
                if p is not None and q is not None:
                    print(f"{number} = {p} * {q}")
                else:
                    print(f"Unable to factorize {number}.")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
 
