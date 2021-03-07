from pip._internal import self_outdated_check
class Computer:
    # init is a constructor.
    def __init__(self, cpu, ram):
        print('in init')
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print('CPU', self.cpu)
        print('Config is', self.ram)
        
        
comp1 = Computer('i5', 16)
comp1.config();
comp1 = Computer('Ryzen 3', 8)
comp1.config();

class Car:
    wheels = 4 # static declaration
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'
        
        
c1= Car()        
c2= Car()

c1.mil = 8

print(c1.com, c1.mil, c1.wheels, Car.wheels)        
print(c2.com, c2.mil, c2.wheels, Car.wheels)        

class Student:
    
    # Static class field
    school = 'Sai School'
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.laptop = self.Laptop()
        
    # Instance methods
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
        
        
    def getLaptop(self):
        print(self.laptop.brand, self.laptop.cpu, self.laptop.ram)
        
    # cls argument and the annotation elevates the method to be a class method    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    # static method
    @staticmethod
    def info():
        print('This is student class.. in sai module')
        
    # Inner classes
    class Laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'
    
            
s1 = Student(34, 67, 32)
s2 = Student(89, 32, 13)

print(s1.avg())
print(s2.avg())
s1.getLaptop()
s2.getLaptop()

print(Student.getSchool())
Student.info()

lap1 = Student.Laptop()





























