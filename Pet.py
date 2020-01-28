__author__ = "Nelson Acosta"

#    Class Pet
#        Private String _name
#        Private String _type
#        Private real _age
#
#        Public Module set_name(String n)
#            set_name = n
#
#        Public Function get_name()
#            Return _name
#
#        Public Module set_type(String t)
#            set_name = t
#
#        Public Function get_type()
#            Return _type
#
#        Public Module set_age(Real a)
#            set_age = a
#
#        Public Function get_age()
#            Return _age
#
#        End Module
#
#    End Class


class Pet():
    _name = ""
    _type = ""
    _age = 0.0

    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t

    def get_age(self):
        return self._age

    def set_age(self, a):
        self._age = a

#    Module main():
#       Declare String n
#       Declare String t
#       Declare String a
#       Declare Pet animal1
#       Declare Pet animal2
#
#        Display "Enter your first pet's name"
#       Input n
#       Display "Enter the type of animal that you have"
#       Input t
#       Display "Enter your pet's age"
#       Input a
#       Set animal1 = New Pet()
#       Call animal.set_name(n)
#       Call animal.set_type(t)
#       Call animal.set_age(a)
#
#       Display "Enter your second pet's name"
#       Input n
#       Display "Enter the type of animal that you have"
#       Input t
#       Display "Enter your pet's age"
#       Input a
#       Set animal2 = New Pet()
#       Call animal2.set_name(n)
#       Call animal2.set_type(t)
#       Call animal2.set_age(a)
#       Display "your first pet's name is", animal1.get_name(), "type is a"
#       Display "animal1.get_type(), "and is", animal1.get_age(), "years old"
#
#       Display "your second pet's name is", animal2.get_name(), "type is a"
#       Display "animal2.get_type(), "and is", animal2.get_age(), "years old"
#
def main():
    n = ""
    t = ""
    a = ""
    animal1 = None
    animal2 = None
    message = ""


    n = input("Enter your first pet's name ")
    t = input("Enter the type of animal that you have ")
    a = input("Enter your pet's age ")
    animal1 = Pet()
    animal1.set_name(n)
    animal1.set_type(t)
    animal1.set_age(a)
    n = input("Enter your second pet's name ")
    t = input("Enter the type of animal that you have ")
    a = input("Enter your pet's age ")
    animal2 = Pet()
    animal2.set_name(n)
    animal2.set_type(t)
    animal2.set_age(a)

    print("your first pet's name is", animal1.get_name(), "type is a", end=" ")
    print(animal1.get_type(), "and is", animal1.get_age(), "years old")

    print("your second pet's name is", animal2.get_name(), "type is a", end=" ")
    print(animal2.get_type(), "and is", animal2.get_age(), "years old")
main()