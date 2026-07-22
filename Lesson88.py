class myclass:

    __privateVar = 27;

    def __privmeth(self):
        print("im inside class myclass")

    def hello(self):
        print("private Variable value: ",myclass.__privateVar)

foo = myclass()
foo.hello()
