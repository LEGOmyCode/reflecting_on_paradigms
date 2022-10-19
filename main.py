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
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price) -> None:
        super().__init__(max_speed, condition, price)
    def flame_jet(condition):
        super().condition = 'trashed'

#Q How does this solution demonstrate the four pillars of OOP? 
# (It may not demonstrate all of them, describe only those that apply)
#A -Encapsulation: The methods can be accessed however not the attributes is some cases.
# -Abstraction: N/A
# -Inheritance: The other pod racers use the default constructor from podracer class using recycled code.
# -Polymorphism: The parent shares behaviors of its class to its children.
#Q Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#A No, I think this fits appropriately. It makes things easier when configuring multiple "Podracers". It recycles code that would otherwise be repetitive.
#Q How in particular did Object Oriented Programming assist in the solving of this problem?
#A Most importantly the inheritance and polymorphism pillars.


#REFLECTION
#Q Is one of these coding paradigms "better" than the other? Why or why not?
#A No, They both serve a purpose that is beneficial in its own way from small scale to large scale. 
#Q Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
#A I would lean towards the functional prompt. It allows clear dry code with little errors and easy debugging.
#Q Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
#A Functional programming is useful for quick operations or task handling. I believe OOP is better for larger scale manipulation and structural coding.
#Q Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
#A It might be because I'm new but I would bet using functional coding takes more work to understand to make clear effect coding that is pure and 
# elegant.