#zadanie 2.1
class Animal:
  def __init__(self,name,age,species,weight):
    self.name = name
    self.age = age
    self.species = species
    self.weight = weight
    self.height = 1 #wzrost zwierzecia, domyslnie 1 metr

  @staticmethod
  def oldest_animal(animals):
    if not animals:
      return None, None
    oldest = max(animals, key=lambda animal: animal.age)
    return f'{oldest.name} is the oldest animal at {oldest.age} years old.'

  def is_endangered(self):
    return self.species.lower() == "tiger"

  def calculate_bmi(self):
    return self.weight / (self.height**2)

#dla zadania 2:
  def __repr__(self):
    return self.__str__()

  def __str__(self):
    return f"{self.name} the {self.species} ({self.age} years old, {self.weight}kg)"

lion = Animal("Simba", 5, "lion", 200)
tiger = Animal("Shere Khan", 8, "tiger", 150)
elephant = Animal("Dumbo", 3, "elephant", 400)
animals = [lion, tiger, elephant]

print(Animal.oldest_animal(animals))
print(lion.is_endangered())
print(tiger.is_endangered())
print(lion.calculate_bmi())
print(tiger.calculate_bmi())

#zadanie 2.2
class Farm:
  def __init__(self):
    self.animals = []

  def __str__(self):
    result = 'Farm with animals:\n'
    for i, animal in enumerate(self.animals, 1):
      result += f'{i}. {animal.name} the {animal.species}, {animal.age} years old, {animal.weight} kg\n'
    return result

  def __repr__(self):
    return f"Farm with animals: {' | '.join(repr(animal) for animal in self.animals)}"

  def add_animal(self,animal):
    if isinstance(animal, Animal):
      self.animals.append(animal)
    else:
      raise ValueError("Only objects of type Animal can be added to the farm.")

  def feed_all(self, food):
    if not self.animals:
      return "No animals to feed."
    else:
      result = f'\nFeeding all animals on farm with {food}'
      for animal in self.animals:
        result += f'\n{animal.name} the {animal.species} is being fed.'
      result += '\nAll animals have been fed.\n'
      return result

  @classmethod
  def create_farm_with_animals(cls, animals_list):
    farm = cls()
    for animal in animals_list:
      farm.add_animal(animal)
    return farm

farm = Farm()
cow = Animal("Berta", 5, "cow", 400)
farm.add_animal(cow)

chicken1 = Animal("Chirpy", 1, "chicken", 1)
farm.add_animal(chicken1)

chicken2 = Animal("Cluck", 2, "chicken", 1.2)
farm.add_animal(chicken2)

print(farm)
print(farm.animals)
print(farm.feed_all('corn'))

animals = [
  Animal("Berta2",5,"cow",400),
  Animal("Chirpy2", 1, "chicken", 1),
  Animal("Cluck2", 2, "chicken", 1.2)
]
farm1 = Farm.create_farm_with_animals(animals)
print(farm1.animals)

#zadanie 2.3
class Student:
  def __init__(self,first_name,last_name,age,year,gpa):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.year = year
    self.gpa = gpa

  def get_full_name(self):
    return f'{self.first_name} {self.last_name}'

  def is_on_probation(self):
    if self.gpa <= 3.0:
      return True
    else:
      return False
  @staticmethod
  def get_average_age(students):
    total_age = sum(student.age for student in students)
    return total_age / len(students)

  @staticmethod
  def get_students_by_year(students):
    students_by_year = {year: [] for year in range(1, 6)}
    for student in students:
      students_by_year[student.year].append(student)
    return students_by_year

  @staticmethod
  def print_students_by_year(students):
    students_by_year = Student.get_students_by_year(students)
    for year, student_list in students_by_year.items():
      print(f"{year} rok:")
      if not student_list:
        print('BRAK')
      else:
        for student in student_list:
          print(f"- {student.get_full_name()} ({student.age} lat, ́srednia ocen: {student.gpa})")

s1 = Student("Jan", "Kowalski", 20, 2, 3.5)
s2 = Student("Anna", "Nowak", 22, 3, 2.8)
s3 = Student("Piotr", "Czerwinski", 19, 1, 2.1)
s4 = Student("Katarzyna", "Wójcik", 21, 4, 4.0)
print(s1.is_on_probation())
print(s2.is_on_probation())
students = [s1, s2, s3, s4]
print(Student.get_average_age(students))
students_by_year = Student.get_students_by_year(students)
Student.print_students_by_year(students)

#zadanie 2.4
class Athlete:
  team = "No team"
  country = 'No country'

  def __init__(self,name,age,height,weight,sport):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
    self.sport = sport
    self._team = None
    self._country = None

  def get_bmi(self):
    bmi = self.weight / ((self.height/100) ** 2)
    return round(bmi,2)

  def get_info(self):
    team = self._team if self._team else Athlete.team
    country = self._country if self._country else Athlete.country
    return f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm, Weight: {self.weight}kg, Sport: {self.sport}, Team: {team}, Country: {country}"

  @classmethod
  def set_team(cls, obj, team):
    obj._team = team

  @classmethod
  def set_country(cls, obj, country):
    obj._country = country

athlete1 = Athlete("Adam Nowak", 25, 175, 75, "football")
athlete2 = Athlete("Ewa Kowalska", 30, 180, 68, "tennis")

Athlete.set_team(athlete1, "Real Madrid")
Athlete.set_country(athlete2, "Poland")

print(athlete1.get_bmi())
print(athlete1.get_info())
print(athlete2.get_info())
