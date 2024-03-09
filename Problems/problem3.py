"""
Project Euler - Problem 3: Largest Prime Factor

Description:
What is the largest prime number of 60085147543

Author:
Max Fils Remfort
"""

target = 84

def prime_factors(target_num):
    starting_factor = 2
    factors = []
    while starting_factor <= target_num:
        if target_num % starting_factor == 0:
            factors.append(starting_factor)
            target_num = target_num/starting_factor
        else:
            starting_factor += 1
    return factors

prime = prime_factors(target)

print(prime)
    
        
