#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Student import *
from Admin import *
from Faculty import *
from Book import *
from Function import *
import pickle
from time import sleep
l=[]
ba=[]
fa=[]
print("\n\n\t\t\t****DIGITAL LIBRARY****\n\n")
print("1.Student\n2.Faculty\n3.Admin\n4.Book\n5.Exit\n")
ch=input("Enter your choice:")
while(True):
    if(ch=='1'):
        print("Enter your choice:")
        c=input("a.Login \nb. Sign up\nc.Exit")
        while(True):
            
            if(c=='b'):
                s=Student()
                s.getd()
                l.append(s)

                with open("student.pkl",'wb') as f:
                    pickle.dump(l,f)
            if(c=='a'):
                p=input("Enter the enrollemnt number:")
                q=Function()
                w=q.search("student.pkl",p)
                
                if(w=='1'):
                    print("\n\t------YOU HAVE ENTERED TO THE STUDENT'S MENU----------\n")
                    book=input("Enter your choice:\tI.Issue Book\tS.Show details \tE. Exit")
                    while(book!='Exit'):
                        if(book=='I'):
                            s=Student()
                            s.book_i()
                        if(book=='S'):
                            en=input("Enter the enrollment number of the student:")
                            q=Function()
                            print("\n")
                            q.Showb("student.pkl",en)

                        book=input("Enter your choice:\tI.Issue Book\tS.Show details E. Exit")

                else:
                    print("YOU ARE NOT SIGNED IN")
                    print("1. Sign in\n 2. Exit")
                    kl=int(input("Enter your choice:"))
                    if(kl=='1'):
                        s=Student()
                        s.getd()
                        l.append(s)

                        with open("student.pkl",'wb') as f:
                            pickle.dump(l,f)

                    elif(kl=='2'):
                        break

                    
                        
            if(c=='c'):
                break
            
                
            print("Enter your choice:")
            c=input("a.Login \nb. Sign up\nc.Exit")
                
    if(ch=='2'):
        print("Enter Your Choice(Faculty)")
        c=input("a.Login \nb. Sign up\nc.Exit")
        while(True):
            if(c=='b'):
                fl=Faculty()
                fl.getd()
                fa.append(fl)
                with open("faculty.pkl",'ab') as f:
                    pickle.dump(fa,f)
            if(c=='a'):
                p=input("Enter the Faculty ID:")
                q=Function()
                w=q.search("faculty.pkl",p)
                if(w!='0'):
                    print("\n\t------YOU HAVE ENTERED TO THE FACULTY'S MENU----------\n")
                    book=input("Enter your choice:\tI.Issue Book\tS.Show details\n")
                    if(book=='I'):
                        s=Faculty()
                        s.book_i()
                    if(book=='S'):
                        en=input("Enter the Faculty ID:")
                        q=Function()
                        q.Showb("faculty.pkl",en)
                
                    else:
                        print("YOU ARE NOT SIGNED IN")
            elif(c=='c'):
                break
                
            print("Enter your choice:\n")
            c=input("a.Login \nb. Sign up\nc.Exit")
                
            
    if(ch=='3'):
        
        a=Admin()
        p=a.getp()
        
        if(p==1):
            print("********YOU HAVE ENTERED TO THE ADMIN'S PAGE*******")
            w=input("1.Show whole details :\n2.Show detail via enroll \n3.Delete Record \n4.Update record  \n5.Show fine\n6.Exit from the admin menu")
            while(True):
                if(w=='1'):
                    print("Which Record do you want to see:")
                    u=input("1.Student's record\t2.Faculty's Record\t3.Book Record \t4.Exit\n")
                    while(u!='4'):
                        if(u=='1'):
                            q=Function()
                            q.Show("student.pkl")
                        if(u=='2'):
                            q=Function()
                            q.Show("faculty.pkl")
                        if(u=='3'):

                            q=Function()
                            q.Show("book.pkl")
                        u=input("1.Student's record\t2.Faculty's Record\t3.Book Record \t4.Exit\n")


                if(w=='2'):

                    print("Which Record do you want to see:\n")
                    u=input("\n1.Student's record\t2.Faculty's Record\t3.Book Record\t 4.Exit\n")
                    while(u!='4'):
                        if(u=='1'):
                            q=Function()
                            t=input("Enter the enrollment number:")
                            q.Showd("student.pkl",t)
                            if(u=='2'):
                                q=Function()
                                t=input("Enter the Faculty ID:")
                                q.Showd("faculty.pkl",t)
                        if(u=='3'):

                            q=Function()
                            t=input("Enter the ISBN:")
                            q.Showd("book.pkl",t)
                        u=input("\n1.Student's record\t2.Faculty's Record\t3.Book Record\t 4.Exit\n")
                        
                
                if(w=='3'):
                    print("Which Record do you want to delete:\n")
                    u=input("1.Student's record\t2.Faculty's Record\t3.Book Record\t4.Exit\n")
                    while(u!='4'):
                        if(u=='1'):
                            q=Function()
                            t=input("Enter the enrollment number:")
                            q.remove("student.pkl",t)
                        if(u=='2'):
                            q=Function()
                            t=input("Enter the Faculty ID:")
                            q.remove("faculty.pkl",t)
                        if(u=='3'):

                            q=Function()
                            t=input("Enter the ISBN:")
                            q.removeb("book.pkl",t)
                        u=input("1.Student's record\t2.Faculty's Record\t3.Book Record\t4.Exit\n")
                        
                if(w=='4'):

                    q=Function()
                    t=input("Enter the enrollment number:")
                    q.update("student.pkl",t)

                if(w=='5'):

                    p=input("Enter the enrollment number of the student:")
                    q=Function()
                    q.fine("student.pkl",p)

                elif(w=='6'):
                    break
                w=input("1.Show whole details :\n2.Show detail via enroll \n3.Delete Record \n4.Update record  \n5.Show fine\n6.Exit from the admin menu")

            else:
                print("!!!INCORRECT PASSWORD!!!")
            
    if(ch=='4'):
        w=input("1.Add Book\n2.Show Books\n3.Exit")
        while(True):
            
            if(w=='1'):
                r=int(input("Enter the number of books:"))
                for i in range(r):
                    
                    b=Book()
                    b.addb()
                    ba.append(b)
                    with open("book.pkl",'ab') as f:
                        pickle.dump(ba,f)
            if(w=='2'):
                q=Function()
                q.Showbook("book.pkl")
            if(w=='3'):
                break
            w=input("1.Add Book\n2.Show Books\n3.Exit")
    if(ch=='5'):
        print("\n\n**************THANK YOU FOR USING DIGITAL LIBRARY**************\n\n")
        sleep(1.0)
        break
    print("\n\n1.Student\n2.Faculty\n3.Admin\n4.Book\n5.Exit\n")
    ch=input("Enter your choice:")
    




