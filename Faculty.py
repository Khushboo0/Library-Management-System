from Function import * 
class Faculty:
    def getd(self):
        self.name=input("Ënter the name of the Faculty:")
        self.enroll=input("Enter the Faculty Id:")
        while(True):
            if(self.enroll[0]!='F'):
                print("Invalid Faculty(should be started with 'F')!!")
                self.enroll=input("Re-enter the Faculty Id:")
            else:
                break
        while(True):

            q=Function()
            w=q.search("faculty.pkl",self.enroll)
            if(w=='1'):

                    print("Faculty ID number already exists!!")
                    self.enroll=input("Re-enter the Faculty ID:")
            else:
                break
        
        
    def display(self):
        print(f"Name of the Faculty: {self.name}\tFaculty Id: {self.enroll}")
        
    def book_i(self):
        
        self.enroll=input("Enter the enrollement number:")
        q=Function()
        q.Showbook("book.pkl")
        q.modify("book.pkl",self.enroll,"faculty.pkl")
            
      
