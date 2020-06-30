import pickle
import datetime
class Book:
    def addb(self):
        
        self.name=input("Enter the title of the book:")
        self.isbn=int(input("Enter the isbn number of the book:"))
        self.year=int(input("Enter the year of publishing of the book:"))
        self.author=input("Enter the Author of the book:")
        self.cp=int(input("Enter number of copies:"))
        
        while(True):
            if(self.cp==0):
                print("You have to enter more than 0 copy")
                self.cp=int(input("Enter number of copies:"))
            else:
                break
        
    def display(self):
        return(f"Name of the Book: {self.name}\tISBN: {self.isbn}\tYear:{self.year}\tAuthor: {self.author}\tCopies:{self.cp}")
        
    def Booki(self,x,y,copy,isbn):
        with open(x,"rb") as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.enroll == y:
                            
                            if(isbn not in i.book):
                                
                                i.book[isbn]=copy
                            else:
                                i.book[isbn]+=copy
                                
                            
                                
                            o=datetime.datetime.now()
                            i.datetime=o
                            
                           
                except EOFError:
                    break
        with open(x,"wb") as f:
                pickle.dump(obj,f)
        

