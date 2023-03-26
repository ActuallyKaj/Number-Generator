import random

lowerBound = int(input("Please enter the lower bound: "))
upperBound = int(input("Please enter the upper bound: "))

low = lowerBound
high = upperBound + 1

result = random.randint(low, high)
print(result)