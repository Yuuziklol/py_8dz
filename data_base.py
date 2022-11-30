import json, os
def set_student(list):
    student_db[list[0]] = list[1:],{}

def set_grade(last_name, subject, grade):
    if student_db.get(last_name) is None:
        print(f'Ученик не найден')
        print(student_db)
    else:
        if subject in student_db[last_name][1]:
            student_db[last_name][1][subject].extend(grade)
        else:
            student_db[last_name][1][subject] = grade

def get_student(last_name_student):
    if student_db.get(last_name_student) is None:
        print('Ученик не найден')
    else:
        data = student_db[last_name_student]
        print(f'{last_name_student}{", ".join(data[0])}:')
        print(*[f'{key}: {", ".join(value)}' for key, value in data[1].items()], sep='\n')

def save_db():
    json.dump(student_db, open('data_base.json','w',encoding='utf=8'))

def load_db():
    global student_db
    if os.stat('data_base.json').st_size == 0:
        student_db = {}
    else:
        student_db = json.load(open('data_base.json', encoding='utf=8'))