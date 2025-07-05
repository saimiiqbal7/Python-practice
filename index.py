

class Person:

    total = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total += 1

    def hi(self):
        return("hello")

class Student(Person):

    def __init__(self, name, age):
        Person.__init__(self,name,age)
    


saim = Person("saim", 1997)
obaid = Student("obaid", 1999)

print(obaid.hi())



        
        