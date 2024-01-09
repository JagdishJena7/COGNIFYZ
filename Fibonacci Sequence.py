def generate_fibonacci_sequence(n):
    # Check if the input is valid
    if n <= 0:
        return []

    # Initialize the Fibonacci sequence with the first two terms
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth term
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Get the number of terms from the user
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    
    if num_terms < 0:
        print("Please enter a non-negative integer.")
    else:
        # Generate and print the Fibonacci sequence
        fibonacci_sequence = generate_fibonacci_sequence(num_terms)
        print("Fibonacci Sequence:")
        print(fibonacci_sequence)

except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
