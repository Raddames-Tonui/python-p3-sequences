def print_fibonacci(length):
    # Check if the length is valid (non-negative and an integer)
    if length <= 0:
        print("[]")
        return

    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the specified length
    for i in range(2, length):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # Print the sequence up to the specified length
    print(fibonacci_sequence[:length])
