# class Employee:
#     name = name
#     surname = surname
# employee1 = Employee('Alex', 'Smith')

class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):
        return 'i can walk'


class Developer(Employee):
    def __init__(self, name, surname, language):
        super().__init__(name, surname)
        self.language = language

    def coding(self):
        return 'i am coding'

# class Junior(Developer)

class Tester(Employee):
    def __init__(self, name, surname, language, test_framework):
        super().__init__(name, surname)
        self.language = language
        self.test_framework = test_framework
    def testing(self):
        return 'i can test'

dev1 = Developer('al', 'ku', 'python')
print(dev1.walk())
print(dev1.name)
print(dev1.coding())

tester1 = Tester('alona', 'kuts', 'phyton', 'testNG')
print(tester1.name)
print(tester1.testing())


employee1 = Employee('alex', 'smith')
print(employee1.name)
print(employee1.surname)
print(employee1.walk())

print(isinstance(dev1, Developer))
print(type(dev1))
print(issubclass(Developer, Employee))


#
# employee2 = Employee('andrii', 'kuts')
