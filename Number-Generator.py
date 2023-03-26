import numpy

lowerBound = int(input("Please enter the lower bound: "))
upperBound = int(input("Please enter the upper bound: "))

low = lowerBound
high = upperBound + 1

result = np.random.randint(low, high)
print(result)