from dataclasses import dataclass, field

"""
    Dataclass explanation:
        -> frozen=True makes the object read only
    Field explanation:
        -> sort_idx included to enable sorting, this will affect the gt comparison
        -> init = False allows the field to be ignored in __init__
        -> repr = False removes the field from being printed
"""


@dataclass(order = True, frozen = True)
class Person:
    sort_index: int = field(init = False, repr = False)
    name: str
    age: int
    job: str
    strength: int = 100

    # Function executed after data has been populated
    def __post_init__(self):
        # When frozen, issue with changing attribute value
        # self.sort_index = self.age
        # Fix
        object.__setattr__(self, "sort_index", self.strength)

    def __str__(self) -> str:
        return f"{self.name} {self.job} ({self.age})"


person1 = Person("Leon", 53, "Programmer", 99)
person3 = Person("Elzah", 42, "Coach")
person2 = Person("Elzah", 42, "Coach")

# Print the object neatly -> (name='Leon', age=53, job='Programmer')
print(f"Person One {person1}")

# Notice the default value for person one
print(f"Person One {person2}")
print(f"Person One {person2}")

print(f"ID Person One {id(person1)}")
print(f"ID Person Two {id(person2)}")

print(f"Person Two eq Person Three {person2 == person3}")

# Enabled by flag order=True
print(f"Person One gt Person Three {person1<person3}")
