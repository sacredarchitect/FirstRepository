# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:45:30 2019

@author: Joshua Rhodes
"""
import EulerPhi

def gcd(x,y):
    return EulerPhi.gcd(x,y)

class fraction(object): 
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        newNumer = self.getNumer()*other.getDenom() + self.getDenom()*other.getNumer()
        newDenom = self.getDenom()*other.getDenom()
        
        factor = gcd(newNumer, newDenom)
        if factor != 1:
            newNumer /= factor
            newDenom /= factor
        
        return fraction(int(newNumer),int(newDenom))
    def __sub__(self, other):
        newNumer = self.getNumer()*other.getDenom() - self.getDenom()*other.getNumer()
        newDenom = self.getDenom()*other.getDenom()
        
        factor = gcd(newNumer, newDenom)
        if factor != 1:
            newNumer /= factor
            newDenom /= factor
        
        return fraction(int(newNumer),int(newDenom))
    def convert(self):
        return self.getNumer() / self.getDenom()
    
new = fraction(37,17) + fraction(3,4) 

import datetime

def timeYM(time):
    ''' input time in days and return years, months'''
    years = int(time/365)
    months = int((time - years*365)/30)
    
    return years, months

class Person(object):
    def __init__(self, name):
        '''create a person called name'''
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    
    def getLastName(self):
        '''return self's last name'''
        return self.lastName
    
    def setBirthday(self, month, day, year):
        '''set self's birthday to birthDate'''
        self.birthday = datetime.date(year,month,day)
        
    def __str__(self):
        '''return self's name'''
        return self.name
    
    def getAge(self):
        '''return self's current age in days'''
        if self.birthday == None:
            raise ValueError
        bdayDays = (datetime.date.today() - self.birthday).days
        
        return str(timeYM(bdayDays)[0]) + ' years, ' + str(timeYM(bdayDays)[1]) + ' months'

    def __lt__(self, other):
        ''' return True if self's name is lexicographically \
        less than other's name and False otherwise'''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,1984)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,1983)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,1955)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

#for e in personList:
#    print(e)
#
#personList.sort()
#
#for e in personList:
#    print(e)

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign
    
    def __init__(self, name):
        Person.__init__(self, name) #initiate Person attributes
        self.idNum = MITPerson.nextIdNum # MITPErson attribute: unique ID number
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    # sorting MIT people uses their ID number, not name:
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
    
q1 = MITPerson('Eric')
q2 = MITPerson('John')
q3 = MITPerson('John')
q4 = Person('John')

MITPerson.setBirthday(q1,10,2,1998)

# add a useful subclass of MITPerson for isStudent()
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

class Grad(Student):
    pass

class Transfer(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department 
        
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
       return self.speak('It is obvious that ' + topic)
   
class Gradebook(object):
    '''A mapping from students to a list of grades'''
    def __init__(self):
        '''Create an empty gradebook'''
        self.students = [] # list of Student objects
        self.grades = {} # maps idNum --> list of grades
        self.isSorted = True # true if self.students is sorted
        
    def addStudent(self, student):
        '''Assumes student is of type Student;
        Add Student to gradebook'''
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        '''Assumes grade is float;
        Add grade to the list of grades for a student'''
        try: 
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in gradebook')
    
    def getGrades(self, student):
        '''Return a list of grades for a student'''
        try:    # return a copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in gradebook')
    
    def allStudents(self):
        '''Return a list of the students in the gradebook'''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        # return copy of list of students
    
def gradeReport(course):
    '''Assumes course is of type grades'''
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


            
        
    
        
        