# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
    def __init__(self,max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
# Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = 'repaired'
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def boost(self):  
        self.max_speed *= 2
# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def flame_jet(self):
        self.condition = 'trashed'
    
Anakin = AnakinsPod(2, 'good', 1400)
Sebulba = SebulbasPod(130, 'poor', 200)

# Given a pod created from your defined Podracer class, running pod.repair() and printing the pod.condition afterwards should display "repaired" in the console.
Podracer.repair(Anakin)
print(Anakin.condition)
# Given another new_pod created from your defined AnakinsPod class with a max_speed of 2, running new_pod.boost() and printing the new_pod.max_speed afterwards should display "4".
print(Anakin.max_speed)
Anakin.boost()
print(Anakin.max_speed)
# Given a third_pod created from your defined SebulbasPod class, running third_pod.flame_jet() and printing the third_pod.condition afterwards should display "trashed" in the console.
SebulbasPod.flame_jet(SebulbasPod)
print(SebulbasPod.condition)


# How does this solution demonstrate the four pillars of OOP?
# Encapsulation: The solution encapsulates the data and functionality of a podracer.
# Abstraction:By using classes that create representations of real world items like the podracers, that is how abstraction is shown
# Inheritance:The classes of AnakinsPod and ShelbulbasPod inherited from the Podracer class making it apparanet in my code.
# Polymorphism: There were no example shown in my code.
# object oriented programming helps solve problmes by showing clear structure for organizing the attributes of the podracers.