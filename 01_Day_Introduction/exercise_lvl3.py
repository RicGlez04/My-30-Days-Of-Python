# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Find the Euclidean distance between (2, 3) and (10, 8)

print(type(91))                                                 # int
print(type(3.14159))                                            # float
print(type(1 - 3j))                                             # complex
print(type('''hahahaha understandable have a nice day'''))      # string
print(type(True))                                               # boolean
print(type([1, 2, 3, 4, 5]))                                    # list
print(type(('A', 'B', 'C')))                                    # tuple
print(type({6, 5, 4, 3, 2, 1}))                                 # set
print(type({'name': 'John', 'age': 30, 'city': 'New York'}))    # dictionary         

# Finding Euclidean distance between (2, 3) and (10, 8)
import math

point1 = (2, 3)
point2 = (10, 8)
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print("Euclidean distance between (2, 3) and (10, 8): ", distance)

print(math.dist((2, 3), (10, 8)))  # Using math.dist() function to find Euclidean distance
