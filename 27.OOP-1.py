"""
class Lehrer:

    lehrer = []

    def __init__(self, name, alter, ort):
        self.name = name
        self.alter = alter
        self.ort = ort
        #print('mein name ist ', self.name, 'ich bin', self.alter, 'jahre alt')

    def sag_name(self):
        return self.name

    def sag_alter(self):
        return self.alter

    def sag_ort(self):
        return self.ort


    def addlehrer(self):
        self.lehrer.append(self.name)
        self.lehrer.append(self.alter)
        self.lehrer.append(self.ort)


l1= Lehrer('hans', 45, 'Hamburg')
l2= Lehrer('claudia', 32, 'Berlin')
l3= Lehrer('alex', 32, 'Bremen')
l4= Lehrer('sebastian', 32, 'Hessen')

print(l1.sag_name())

"""


class Student:

    student = []

    def __init__(self, name, alter, ort):
        self.name = name
        self.alter = alter
        self.ort = ort
    

    def gib_alter(self):
        return self.alter

class Kurs:
    def __init__(self, name):
        self.name = name
        self.is_active = True
        self.student_liste = []

    def add_student(self, student):
        self.student_liste.append(student)


    def get_durchschnitt_alter(self):
        age = 0
        for student in 
        
        return age / len(self.get_durchschnitt_alter())


s1= Student('hans', 12, 'Hamburg')
s2= Student('simon', 13, 'Berlin')
s3= Student('dirk', 21, 'Bremen')
s4= Student('luis', 16, 'Hessen')
s4= Student('laura', 16, 'Koln')

print(s1.gib_name())