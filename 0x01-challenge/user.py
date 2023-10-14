#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Documentation """

    def __init__(self):
        """ Documentation """
        self.__email__ = None


    @property
    def email(self):
        """ Documentation """
        return self.__email__
    #setter for email
    @email.setter
    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email__ = value
   
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
