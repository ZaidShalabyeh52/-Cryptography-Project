# -------------------------------------------------------------
# CY261 - Cryptography
# Phase 3 - Task 1
# Fermat Primality Test
#
# The algorithm is based on Fermat's Little Theorem:
#
#       a^(p-1) ≡ 1 (mod p)
#
# If the equation fails for any random value of a,
# the number is definitely composite.
#
# If the number passes all tests, it is considered
# "probably prime".
#
# NOTE:
# Some composite numbers called Carmichael numbers
# can still pass the Fermat test.
# Example: 561
# -------------------------------------------------------------

import random
import time


# -------------------------------------------------------------
# FUNCTION: modular_exponentiation()
#
# This function efficiently computes:
#
#       (base ^ exponent) mod modulus
#
# Instead of calculating huge powers directly,
# it uses the Square-and-Multiply algorithm.
#
# This is important because the project requires
# testing numbers up to 10^10.
# -------------------------------------------------------------
def modular_exponentiation(base, exponent, modulus):

    result = 1

    # Reduce base initially to keep numbers smaller
    base = base % modulus

    # Continue until exponent becomes 0
    while exponent > 0:

        # If exponent is odd,
        # multiply result by current base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Square the base
        base = (base * base) % modulus

        # Divide exponent by 2
        exponent = exponent // 2

    return result


# -------------------------------------------------------------
# FUNCTION: fermat_test()
#
# Parameters:
#   n -> number being tested
#   k -> number of iterations
#
# Returns:
#   True  -> probably prime
#   False -> composite
#
# The test is repeated k times using random values.
# More iterations increase confidence in the result.
# -------------------------------------------------------------
def fermat_test(n, k):

    # Numbers <= 1 are not prime
    if n <= 1:
        return False

    # 2 and 3 are prime
    if n == 2 or n == 3:
        return True

    # Even numbers greater than 2 are composite
    if n % 2 == 0:
        return False

    # Repeat test k times
    for i in range(k):

        # Choose random base:
        # 2 <= a <= n-2
        a = random.randint(2, n - 2)

        # Compute:
        # a^(n-1) mod n
        fermat_value = modular_exponentiation(a, n - 1, n)

        # If result is not 1,
        # n is definitely composite
        if fermat_value != 1:
            return False

    # Passed all iterations
    return True


# -------------------------------------------------------------
# FUNCTION: test_number()
#
# Runs the Fermat test on a number,
# measures execution time,
# and prints the result.
# -------------------------------------------------------------
def test_number(n, k):

    print("-" * 60)
    print("Testing Number:", n)
    print("Iterations (k):", k)

    # Start timing
    start_time = time.perf_counter()

    # Run Fermat test
    result = fermat_test(n, k)

    # End timing
    end_time = time.perf_counter()

    # Calculate total execution time
    execution_time = end_time - start_time

    # Display result
    if result:
        print("Result: Probably Prime")
    else:
        print("Result: Composite")

    # Display execution time
    print(f"Execution Time: {execution_time:.6f} seconds")


# -------------------------------------------------------------
# MAIN PROGRAM
#
# Required test cases from the project:
#
#   1. 561      -> Carmichael number
#   2. 104729   -> Known prime
#   3. 104723   -> Known prime
#   4. 104725   -> Composite number
#
# -------------------------------------------------------------
if __name__ == "__main__":

    print("\nFermat Primality Test\n")

    # Number of iterations
    k = 10

    # Test case 1
    test_number(561, k)

    # Test case 2
    test_number(104729, k)

    # Test case 3
    test_number(104723, k)

    # Test case 4
    test_number(104725, k)

    print("-" * 60)
    print("Testing Completed.")