#1 список
list_car =["BMW", "MB", "LADA", "KIA", "HONDA"]
#2 цикл for
#3 целочисленная переменная
cars_count = 0
step_ = 0
for i in list_car:
    print("Я езжу на автомабиле марки ", i)
    cars_count += 10
    step_+= 1
    print("Проход №", step_, ",", "cars_count = ", cars_count)
print("Общее кол-во проходов: ", len(list_car))
print("За", len(list_car), "проходов переменная cars_count увеличивалась на 10 каждый раз и теперь равна =", cars_count)
