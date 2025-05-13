# Collatz Sequence
# The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:
# If n is even, the next number n is n/2.
# If n is odd, the next number n is n*3 + 1.
# If n is 1, the sequence stops.

# Limited to natural numbers only, no float numbers

# Ace ~ 2025-02-12

def collatz():

    while True:
        try:
            n = int(input("Enter a whole number: \n")) # Makes sure a positive integer is used
            if n < 1:
                raise ValueError
            break

        except ValueError:
            print("Please pick a whole number.")

    while n != 1:   # Nothing will happen if you input '1', because the collatz sequence will loop indefinitely

        if n % 2 == 0:
            n /= 2
            print(int(n))

        else:
            n = n * 3 + 1
            print(int(n))
    
collatz()
