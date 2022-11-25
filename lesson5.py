class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):
        return "I can walk"

person_1 = Person('alex', 'baker')
print(person_1.name)
print(person_1.surname)

person_2 = Person('alona', 'kuts')

print(person_2.name)



print(person_1.walk())


class Developer(Person):
    def __init__(self, name, surname, language):
        super().__init__(name, surname)
        self.language = language

    def coding(self):
        return 'i am coding'

dev1 = Developer('Michal', 'Sunny', 'python')
print(dev1.walk())
print(dev1.name)
print(dev1.coding())


class Tester(Person):
    def __init__(self, name, surname, language, test_framework):
        super().__init__(name, surname)
        self.language = language
        self.test_framework = test_framework

    def testing(self):
        return'I can test'

tester1= Tester('Alona', 'Kuts', 'Java', 'TestNG')
print(tester1.name)


print(tester1.testing())
print(tester1.walk())

