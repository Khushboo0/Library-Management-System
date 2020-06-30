import getpass
class Admin:
    def getp(self):
        password = getpass.getpass("Enter the Password:")
        if(password=="ABC"):
            return 1
        
        
