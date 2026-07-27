from abc import ABC, abstractmethod

class ABsclass(ABC):

    def print(self,x):
        print("Passed value: ", x)

    @abstractmethod
    def tasks(self):
        print("we are inside ABsclass task")

class test_class(ABsclass):
    def tasks(self):
        print("We are inside test_class task")

test_obj = test_class()
test_obj.tasks()
test_obj.print(100)