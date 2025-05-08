# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.

def fizz_buzz(number):
   
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)
print(fizz_buzz(3))   # Output: 'Fizz'
print(fizz_buzz(5))   # Output: 'Buzz'
print(fizz_buzz(15))  # Output: 'FizzBuzz'
print(fizz_buzz(7))   # Output: '7'

# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

# Example usage:
print(sum_of_squares([1, 2, 3]))  # Output: 14
print(sum_of_squares([2, 4, 6]))  # Output: 56


# Question 3

# Write a function that counts the number of vowels in a string.

def count_vowels(string):
    vowels = 'aeiou'  # Include just lowercase
    count = 0
    for char in string:
        if char in vowels:  # Check if the character is a vowel
            count += 1
    return count

print(count_vowels("hello"))  # Output: 2
print(count_vowels("aeiou"))  # Output: 5
print(count_vowels("crypt"))  # Output: 0



# Question 4

# Write a function that counts the number of repeated characters in a string.

def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
    return len([letter for letter in string if string.count(letter) > 1])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
