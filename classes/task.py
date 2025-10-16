class Library:
    def __init__(self , title ,author , copies ):
        self.title = title
        self.author = author
        self.copies = copies
    
    def Barrow(self):
        if (self.copies > 0):
           print(f"you barrowed the book {self.title}  the author {self.author} the copies remaining {self.copies}")
           self.copies = self.copies - 1
        else:
            print("there is no copies")
            
            
my_library = Library("the power " , "Hana Aden" , 3)

my_library.Barrow()
my_library.Barrow()
my_library.Barrow()
my_library.Barrow()
        
        