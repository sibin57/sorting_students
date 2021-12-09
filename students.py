#отсортировать список из различных студентов различных групп

class Student:

    def __init__(self, surname="nosurname", name="noname", fathername="nofathername", group="nogroup", num="nonum"):
        self.surname = surname
        self.name = name
        self.fathername = fathername
        self.group = group
        self.num=num

    def __str__(self):
        return f"{self.surname} {self.name} {self.fathername} {self.group} {self.num}"

    def get_group():
        return self.group

    def get_fullname():
        return f"{self.surname} {self.name} {self.fathername}"


students = []


file = open("students.txt", 'r')

for line in file:
    surname, name, fathername, group, num = line.split()
    cur_student = Student(surname, name, fathername, group, num)
    students.append(cur_student)


#разбиваем список на группы


groups = {}#Ключ - группа, значение - список студентов в алфавитном порядке 

for student in students(): #добавляем студента в память
    if student.get_group() not in groups.keys():
        groups[student.get_group()]=[student]
    else:
        for i in range(len(groups[student.get_group()])):#пытаемся вставить его в правильное место
            
    
print(*students, sep='\n')

file.close()
