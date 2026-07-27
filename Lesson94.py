class india():
    def capital(self):
        print("now delhi is the capital of india")

    def language(self):
        print("hindi is the most widely spoken language of india")

    def type(self):
        print("india is a developing country")

class USA():
    def capital(self):
        print("washington D.C. is the capital of USA")

    def language(self):
        print("english is the primary language of USA")

    def type(self):
        print("USA is developed country")

obj_ind = india()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()