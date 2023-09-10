class Person:
  def __init__(self, name, age, hobby, nationality):
    self.name = name
    self.age = age
    self.hobby = hobby
    self.nationality = nationality
  def myfunc(self):
    print("Hello I am " + self.name + " and I am "+self.nationality)

p1 = Person("John", 36, "golf", "French")

#del p1.age

print(p1.age)
p2 = Person("Andreas", 14, "basketball", "Greek")
p2.myfunc()

class mathimata:
  def __init__(self, mathimatika, fysiki):
    self.mathimatika= mathimatika
    self.fysiki = fysiki
p1 = mathimata(11,12)
print(p1.mathimatika)
print(p1.fysiki)