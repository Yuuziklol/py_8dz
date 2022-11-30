import student,teacher,data_base

def button_click():
    data_base.load_db()
    flag = int(input('Выберите 1, если вы учитель\nВыберите 2, если вы ученик '))
    if flag == 1:
        help = 1
        while help == 1:
            key = int(input('Выберите 1, если хотите добавить ученика\nВыберите 2, если хотите выставить оценку\nВыберите 0, чтобы выйти из программы '))
            if key == 1:
                teacher.add_student()
            elif key ==2:
                teacher.add_grade()
            elif key == 0:
                help = 0
        else:
            data_base.save_db()
    elif flag == 2:
        last_name = input('Введите фамилию ')
        student.see_grade(last_name)
