class Movie:
    def __init__(self,name,year):
        self.name= name 
        self.year = year
        
    def movie_name(self):
        name = "the movie name is : " , self.name
        return name 
    
    def movie_year(self):
        year = "the year created is: " , self.year
        return year
        
my_movie = Movie("fox",2003)

print(my_movie.movie_name())
print(my_movie.movie_year())


class Student:
    def __init__(self , name , age):
       self.name = name 
       self.age = age
       
    def student_name(self):
        Student_name = "the student name is: ", self.name
        return Student_name
    
    def student_age(self):
        student_age = "the age of student is: " , self.age
        return student_age
    
my_student = Student("Hana" ,20 )
print(my_student.student_name())
print(my_student.student_age())
    

        
    