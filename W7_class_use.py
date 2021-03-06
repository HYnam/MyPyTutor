"""
            Using Classes
This problem relates to the pre-loaded class Person.

Using the Person class, write a function print_friend_info(person) which accepts a single argument, of type Person, and:

prints out their name
prints out their age
if the person has any friends, prints 'Friends with {name}'
Write a function create_fry() which returns a Person instance representing Fry. Fry is 25 and his full name is 'Philip J. Fry'

Write a function make_friends(person_one, person_two) which sets each argument as the friend of the other.
"""
class Person(object):
    def __init__(self, name, age, gender):
        """Construct a person object given their name, age and gender

        Parameters:
            name(str): The name of the person
            age(int): The age of the person
            gender(str): Either 'M' or 'F' for male or female
            
        """

        self._name = name
        self._age = age
        self._gender = gender
        self._friend = None

    def __eq__(self, person):
        return str(self) == str(person)

    def __str__(self):
        if self._gender == 'M':
            title = 'Mr'
        elif self._gender == 'F':
            title = 'Miss'
        else:
            title = 'Ms'

        return title + ' ' + self._name + ' ' + str(self._age)

    def __repr__(self):
        return 'Person: ' + str(self)

    def get_name(self):
        """
        (str) Return the name
        
        """
        return self._name

    def get_age(self):
        """
        (int) Return the age
        
        """
        return self._age

    def get_gender(self):
        """
        (str) Return the gender
        
        """
        return self._gender

    def set_friend(self, friend):
        self._friend = friend

    def get_friend(self):
        """
        (Person) Return the friend
        
        """
        return self._friend
    
def print_friend_info(person):
    print (person._name)
    print(person.get_age())
    if person.get_friend() == None:
        return None
    else: 
        print("Friends with",person.get_friend().get_name())

def create_fry():
    fry = Person("Philip J. Fry", 25, "M")
    return fry

def make_friends(person_one,person_two):
    Person.set_friend(person_one, person_two)
    return person_one.set_friend(person_two), person_two.set_friend(person_one)
    
