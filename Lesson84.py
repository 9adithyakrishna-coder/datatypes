class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.breed}."
    

dog1 = dog("buddy", "labrador")
dog2 = dog("rocky", "bulldog")
print(dog1.info())
print(dog2.info())