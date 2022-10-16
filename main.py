# Functional Promt
# Implement a function that will flatten and sort an array of integers in ascending order, 
# and which adheres to a functional programming paradigm.
# Remember, when writing in a functional style:
# Keep variables immutable
# Write only pure functions
# Remember, functions may be higher order

list = [[5, 2], [6, 1], [3, 8], [7, 0]]

def pure_func(list):
    solution = sorted([j for i in list for j in i])
    return solution 

print(pure_func(list))

#Q How does this solution ensure data immutability?
#A It only returns a solution.
#Q Is this solution a pure function? Why or why not?
#A Yes, It is a pure function. The function will always produce the same output for the same arguments and
# It does not change or modifies the input variable
#Q Is this solution a higher order function? Why or why not?
#A No, because it doens't return a function nor can it take in a function as a argument
#Q Would it have been easier to solve this problem using a different programming style?
#A No, I think it is easy to read and work with.
#Q Why in particular is functional programming a helpful paradigm when solving this problem?
#A makes debugging and unit testing easier



# Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

class Podracer:
    def __init__(self, max_speed, condition, price) -> None:
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = 'repaired'

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price,) -> None:
        super().__init__(max_speed, condition, price)
    def boost(max_speed):
        pass

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price) -> None:
        super().__init__(max_speed, condition, price)
    def flame_jet(condition):
        super().condition = 'trashed'