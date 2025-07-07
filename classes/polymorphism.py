#method overloading
#polymorphism in python
# Absraction
# Encapsulation done
# Inheritance, Overriding, Polymorphism

class Speaker:
  def speak(self):
    pass

  def shout(self):
    pass

class Eater:
  def eat(self):
    pass

class Human (Speaker, Eater):
  def speak(self):
    print("hi how are you")

  def eat(self):
    print('ate macrona')

class Duck (Speaker, Eater):
  def speak(self):
    print('Quack quack')

  def eat(self):
    print('Ate fish')

me = Human()

def make_them_eat(eater):
  eater.eat()

def make_them_speak(speaker):
  speaker.speak()

make_them_eat(me)
make_them_speak(me) 

# Absraction
# Encapsulation done
# Inheritance, Overriding, Polymorphism

class Exercise:
  def task(self):
    pass

  def quiz(self):
    pass

class Lecture:
  def subject(self):
    pass

class Teacher (Exercise, Lecture):
  def task(self):
    print("write Essey")

  def quiz(self):
    print('10 Questions')

  def subject(self):
      print("The python session")


you = Teacher()

def make_them_do(exercise):
  exercise.task()

def make_the_subject(student):
  student.subject()
def make_the_quiz(stu):
  stu.quiz()

make_them_do(you)
make_the_subject(you)
make_the_quiz(you)