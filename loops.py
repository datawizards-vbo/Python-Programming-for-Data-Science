# For loop example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop example
i = 0
while i < 5:
    print(i)
    i += 1

# Break example
for i in range(10):
    if i == 4:
        break
    print(i)

# Continue example
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Enumerate example
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


# Using a for loop and an if-else statement to print only even or odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


# Advanced Examples
def is_prime(number):
    """
    Given an integer, return True if the number is prime, and False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = 17
if is_prime(number):
    print(number, "is prime")
else:
    print(number, "is not prime")


def nth_prime(n):
    """
    Given an integer n, return the n-th prime number.
    """
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            prime_count += 1
            if prime_count == n:
                return num
        num += 1

n = 10
print(nth_prime(n))



