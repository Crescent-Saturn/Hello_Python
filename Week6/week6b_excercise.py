# Ex.1
# Implementation of Person class


#################################################
# Student adds code where appropriate

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.fn = first
        self.ln = last
        self.bir = year
    def full_name(self):
        return self.fn +" "+ self.ln
    def age(self, current_year):
        return	current_year - self.bir
    def __str__(self):
        return "The person's name is "+ str(self.fn) +" "+ str(self.ln)+ ". Their birth year is "+str(self.bir)
    
###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

print joe
print john
print stephen
print scott

print joe.age(2013)
print scott.age(2013)   # yeah, right ;)
print john.full_name()
print stephen.full_name()


####################################################
# Output of testing code - results of __str__ method may vary

#The person's name is Joe Warren. Their birth year is 1961
#The person's name is John Greiner. Their birth year is 1966
#The person's name is Stephen Wong. Their birth year is 1960
#The person's name is Scott Rixner. Their birth year is 1987
#52
#26
#John Greiner
#Stephen Wong


#########
## Ex. 2

# Use of Person class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)

#################################################
# Student adds code where appropriate    
    
# implementation of average_age
def average_age(person_list, current_year):
    av = 0
	for p in person_list:
		av + = p.age(current_year)
	return av/float(len(person_list)


###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

instructors = [joe, john, stephen, scott]
print average_age(instructors, 2013)

instructors.pop() # get rid of Scott and his bogus age
print average_age(instructors, 2013)


####################################################
# Output of testing code 

#44.5
#50.6666666667



######  Ex.3
# Implementation of Student class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)


#################################################
# Student adds code where appropriate

# definition of Student class
class Student:
    
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.stu = person
        self.cde = pwd
        self.pro = []
    # use the full_name method for Person    
    def get_name(self):
        return self.stu.full_name()
    def check_password(self, pwd):
        return (self.cde == pwd)
    def get_projects(self):
        return self.pro
    def add_project(self, project):
        return self.pro.append(project) 
 
    
###################################################
# Testing code

joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print joe_student.get_name()
print joe_student.check_password("qwert")
print joe_student.check_password("TopSecret")

print joe_student.get_projects()
joe_student.add_project("Create practice exercises")
print joe_student.get_projects()
joe_student.add_project("Implement Minecraft")
print joe_student.get_projects()


####################################################
# Output of testing code 

#Joe Warren
#False
#True
#[]
#['Create practice exercises']
#['Create practice exercises', 'Implement Minecraft']


#####
## Ex.4
# Use of the Student class

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)


# definition of Student class
class Student:
    
    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []
    
    # use the full_name method for Person    
    def get_name(self):
        return self.person.full_name()
    
    def check_password(self, pwd):
        return self.password == pwd
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)
        
        
#################################################
# Student adds code where appropriate
        
# definition of function assign
def assign(students, name, pwd, project):    
    for p in students:
        if p.get_name() == name and p.password == pwd:
            if p.get_projects().count(project) == 0:
                p.projects.append(project)
    
        
 
    
###################################################
# Testing code

# create some Student objects using Person object
joe = Student(Person("Joe", "Warren", 52), "TopSecret")
joe.add_project("Create practice exercises")
joe.add_project("Implement Minecraft")

scott = Student(Person("Scott", "Rixner", 29), "CodeSkulptor")
scott.add_project("Beat Joe at RiceRocks")

john = Student(Person("John", "Greiner", 47), "outdoors")


# create a list of students
profs = [joe, scott, john]

# test assign
print joe.get_projects()
assign(profs, "Joe Warren", "TopSecret", "Practice RiceRocks")
print joe.get_projects()

print john.get_projects()
assign(profs, "John Greiner", "OUTDOORS", "Work on reflexes")
print john.get_projects()
assign(profs, "John Greiner", "outdoors", "Work on reflexes")
print john.get_projects()



####################################################
# Output of testing code 

#['Create practice exercises', 'Implement Minecraft']
#['Create practice exercises', 'Implement Minecraft', 'Practice RiceRocks']
#[]
#[]
#['Work on reflexes']




