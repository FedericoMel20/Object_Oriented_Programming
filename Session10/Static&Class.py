class Person:
    species = "Homo sapiens"  # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import date
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        return age >= 18


# Using the class
person1 = Person("Alice", 25)
person1.greet()

# Using the class method
person2 = Person.from_birth_year("Bob", 2005)
person2.greet()

# Using the static method
print("Is Alice an adult?", Person.is_adult(person1.age))
print("Is Bob an adult?", Person.is_adult(person2.age))
