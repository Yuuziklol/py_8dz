import data_base
def add_student():
    student = input('Введите фамилию, имя, класс через пробел ').split()
    data_base.set_student(student)
def add_grade():
    last_name = input('Введите фамилию ')
    subject = input('Введите предмет ')
    grade = input('Введите оценку ').split()
    data_base.set_grade(last_name, subject, grade)
