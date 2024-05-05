# Данные оценок учеников
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество учеников
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Преобразование множества в список и сортировка по алфавиту
students = list(students)
students = sorted(students)
print("Имена учеников: ", *students)
# Создаем пустой список для хранения средних значений
list_sr_zn = []
# Подсчет среднего значения  и добавление в новый список
for i in grades:
    count = sum(i)
    #    print("сумма по следующим оценкам :",i,"=", count)
    num = len(i)
    sr_zn = count/num
    print("сумма по следующим оценкам :",*i,"=", count,", среднее значение :","=",sr_zn)
    list_sr_zn.append(sr_zn)
    print("добавляем среднее значение в новый список :", list_sr_zn)
# Создаем словари
student_grades = dict(zip(students, grades))
student_sr_zn = dict(zip(students, list_sr_zn))
print("Имена учеников и их оценки:",student_grades)
print("Имена учеников и их средний бал:", student_sr_zn)
