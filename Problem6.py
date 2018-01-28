"""
							* Problem 6 *
	Find the difference between the sum of the squares of the first one
	hundred natural numbers and the sqaures of the sum of the first one
	hundred natural numbers
"""

# Variables for the sum of squares and squared sum
squares = 0
sums = 0

# Iterates through the first hundred numbers to add to the sum of squares
for n in range(1,100):
	squares += n**2

# Iterates through the first hundred numbers to add to the squared sum
for n in range(1,100):
	sums += n

# Finds the difference between the two
diff = squares - sums

# Prints out the difference
print(diff)
