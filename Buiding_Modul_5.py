class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        else:
            return False
floors1 = input("Введите количество этажей в вашем доме: ")
Type1 = input("Введите тип вашего здания: ")
My_Building = Building(floors1,Type1)
floors2 = input("Введите количество этажей соседнего дома: ")
Type2 = input("Введите тип здания соседнего дома: ")
Your_Building = Building(floors2,Type2)
if My_Building == Your_Building:
    print(My_Building == Your_Building, "Это одинаковые постройки")
else:
    print(My_Building == Your_Building, "Это разные постройки")