class person:
  def __init__(self, Name, Number):
    self.Name = Name
    self.Number = Number

class student(person):
  def __init__(self, Name,Score, Number):
    person.__init__(self, Name, Number)
    self.Name = Name
    self.Score = Score

  def display(self):
    print("The student name is " + self.Name)
    print("The student score is",self.Score)
    print("The student name is " + self.Number)
s1=student("Edwin", 80,"01")
s1.display()
s2=student("Njoroge", 83,"02")
s2.display()