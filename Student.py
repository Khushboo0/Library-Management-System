from Function import *
from Book import *

class Student:
   
    def getd(self):
        self.name=input("Enter the name of the student:")
        self.enroll=input("Enter the enrollment number:")
        while(True):
            if(self.enroll[0]!='A'):
                print("Invalid enrollment number!!")
                self.enroll=input("Re-enter the enrollment number:")
            else:
                break             
        
        while(True):
            q=Function()
            w=q.search("student.pkl",self.enroll)
            if(w=='1'):
                print("Enrollment number already exists!!")
                self.enroll=input("Re-enter the enrollment number:")
            else:
                break


 
        self.branch=input("Enter the branch of the student:")
        self.book={}
        self.date=None
        
        
        
    def display(self):
        print(f"Name of the Student: {self.name}\nEnrollment number: {self.enroll}\nBranch: {self.branch}\nBooks:{self.book}")
        
    
    def book_i(self):
        
        self.enroll=input("Enter the enrollement number:")
        print("\n")
        q=Function()
        q.Showbook("book.pkl")
        q.modify("book.pkl",self.enroll,"student.pkl")
            
         

               