"""
Class for progress bar

"""


class ProgressBar:
    def __init__(self, name, hours):  # constructor
        self.name = name
        self.hours = hours

    def __str__(self):
        return f'You have {self.hours} hours left of {self.name} studying to do.'


test_2 = ProgressBar('test class 2', 16)  # test object of the ProgressBar class
print(test_2)

#test_1 = ProgressBar('test 1', 10)  # object of the test class
#print(test_1.name)  # test prints the name of the object
#print(test_1.hours)  # test prints the hours of the object   