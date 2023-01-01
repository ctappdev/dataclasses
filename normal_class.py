class Person:
    # name: str
    # age: int
    # job: str

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


person1 = Person("Leon", 53, "Programmer")
person2 = Person("Elzah", 42, "Coach")
person3 = Person("Elzah", 42, "Coach")

print(f"Person One {person1}")

print(f"ID Person One {id(person1)}")
print(f"ID Person Two {id(person2)}")

print(f"Person Two vs Person Three {person2 == person3}")
