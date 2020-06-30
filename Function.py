from Book import *
from datetime import *
import pickle
class Function:
    def Show(self,x):
        with open(x,'rb') as f:
                while(1):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            print("\n")
                            print(i.display())
                            
                    except EOFError:
                        break
    def Showbook(self,x):
        with open(x,'rb') as f:
                while(1):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.cp>0):
                                print("Books:\n")
                                print(i.display())
                            
                            
                    except EOFError:
                        break
                            
                        
                        
    def Search(self,x,t):
        C=0
        
        with open(x,'rb') as f:
                while(1):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.enroll==t):
                                C=1
                                print("\n")
                                i.display()
                        if(C==0):
                            print("Can't find it!!")
                               
                    except EOFError:
                        break
                        
    def search(self,x,t):
        C=0
        #print("Details of the student:")
        with open(x,'rb') as f:
                while(1):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.enroll==t):
                                C=1
                                return '1'
                        
                            return '0'
                                
                    except EOFError:
                        break
    def Showd(self,x,t):
        C=0
        #print("Details of the student:")
        with open(x,'rb') as f:
                while(1):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.enroll==t):
                                print("\n")
                                i.display()
                    except EOFError:
                        break
                        
    def dumpb(self,x,t,y):
        
        C=0
        with open(x,'rb') as f:
                while(1):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i==t):
                                C=C+1
                                with open(x,'ab') as f:
                                    pickle.dump(y,f)
                                    print("Book added successfully!!")
                        if(C=='0'):
                            print("Can't find it!!")
                               
                    except EOFError:
                        break
    def Showb(self,x,t):
        print("Details of the student:")
        with open(x,'rb') as f:
                while(1):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if(i.enroll==t):
                                print("\n")
                                i.display()
                    except EOFError:
                        break
                        
    def modify(self,x,y,z):
        t=int(input("Enter the ISBN number of the book you want to issue:"))
            
        with open(x,"rb") as f:

            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.isbn == t:
                            p=int(input("Enter the number of copies:" ))
                            
                            if(i.cp>=p):
                                i.cp=i.cp-p
                                b=Book()
                                b.Booki(z,y,p,t)
                                
                            else:
                                print("Dont have enough copies!")
                                
                        else:
                            print("Invalid ISBN There is no book")
                        
                        
                except EOFError:
                    break
        with open(x,"wb") as f:
                pickle.dump(obj,f)
                
    def remove(self,x,t):
        
        with open(x,"rb") as f:
            
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.enroll == t:
                            obj.remove(i)
                except EOFError:
                    print("Data read is removed")
                    break
        with open(x,"wb") as f:
                pickle.dump(obj,f)
                
    def removeb(self,x,t):
        with open(x,"rb") as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        
                        if i.isbn == t:
                            obj.remove(i)
                except EOFError:
                    print("Data is removed")
                    break
        with open(x,"wb") as f:
                pickle.dump(obj,f)
                

                
    def update(self,x,t):
        with open(x,"rb") as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.enroll == t:
                            q=input("1.Name\n2.Branch\n3.Enrollment number:")
                            if(q=='1'):
                                t=input("\nEnter the name of the student:")
                                i.name=t
                            if(q=='2'):
                                t=input("\nEnter the branch of the student:")
                                i.branch=t
                            if(q=='3'):
                                t=input("\nEnter the enrollment of the student:")
                                i.enroll=t
                except EOFError:
                    print("Data is updated")
                    break
        with open(x,"wb") as f:
                pickle.dump(obj,f)
                
    def fine(self,x,t):
        with open(x,"rb") as f:
            while(1):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.enroll == t:
                            if((date.today()-date(2018, 6, 29))>timedelta(days = 25)):
                                z=(date.today()-date(2018, 6, 29))
                                t=(z.days)
                                fine=t*3
                        print(f"\nName of the Student: {i.name}\nEnrollment number: {i.enroll}\nBranch: {i.branch}\nBooks:{i.book}\nFine:{fine}")
                except EOFError:
                    
                    break
        with open(x,"wb") as f:
                pickle.dump(obj,f)
                

                
              

        