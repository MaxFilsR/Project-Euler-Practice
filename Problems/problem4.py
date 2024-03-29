def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_largest_palindrome():
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):  # Avoid duplicate pairs
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

result = find_largest_palindrome()
print("The largest palindrome made from the product of two 3-digit numbers is:", result)
