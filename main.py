
#функция без параметров (аргументов)
#объявление функции
def test():
    a = "без"
    b = "параметров"
    print(a, b)
print ("1-ая функция:")
test()
#функция c параметрами
#объявление функции
def test2(a2, b2, c2):
    print(a2, b2, c2)
print("2-ая функция")
test2("функция test2", "c позиционными", "параметрами")

def test3(*, a3, b3, c3):
    print(a3, b3, c3)
print("3-я функция")
test3(a3 = "функция test3", b3 = "c именованными", c3 = "параметрами")

def test4(a4=1, b4=2, c4=3):
    print(a4, b4, c4)
print("4-я функция")
test4(c4 = "параметр «с» сделаем строкой")

