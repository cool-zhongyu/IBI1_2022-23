# What does this piece of code do?
# Answer:select a number in the range of 1-100 for 10 times and impport the biggest number among them.


# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# store both 0 in two varibles "progress" and "stored_random_number"
progress=0
stored_random_number=0

# under the condition that "prgress"<10, increse the variables one by one.
while progress<10:
	progress+=1

# select a random number and store it in variables n
	n = randint(1,100)

# use if to compare the stored_random_number to n and store the bigger numbers in stroed_random_number
	if n > stored_random_number:
		stored_random_number = n

# import the stored_random_number
print(stored_random_number)
