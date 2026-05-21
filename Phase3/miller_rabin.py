import random
import time


# Miller-Rabin Primality Test
def miller_rabin(n, k=10):

    # Handle small cases
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    # Even numbers are composite
    if n % 2 == 0:
        return False

    # Write n-1 as 2^s * d
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    # Perform the test k times
    for _ in range(k):

        # Choose random base
        a = random.randint(2, n - 2)

        # Compute a^d mod n
        x = pow(a, d, n)

        # Check first condition
        if x == 1 or x == n - 1:
            continue

        # Repeat squaring
        for _ in range(s - 1):

            x = pow(x, 2, n)

            # If x becomes n-1, test passes
            if x == n - 1:
                break

        # If no condition passed, number is composite
        else:
            return False

    # Number is probably prime
    return True


# Function to test numbers
def test_number(n, k):

    print("-" * 50)

    print(f"\nTesting Number: {n}")
    print(f"Iterations (k): {k}")

    # Start timing
    start = time.time()

    # Run test
    result = miller_rabin(n, k)

    # End timing
    end = time.time()

    # Print result
    if result:
        print("Result: Probably Prime")
    else:
        print("Result: Composite")

    # Print execution time
    print(f"Execution Time: {end - start:.6f} seconds")


# Main program
if __name__ == "__main__":

    print("\nMiller-Rabin Primality Test\n")

    # Number of iterations
    k = 10

    # Test cases
    test_number(561, k)
    test_number(104729, k)
    test_number(104723, k)
    test_number(104725, k)

    print("-" * 50)
    print("Testing Completed.")