"""
1.Реализовать скрипт, в котором должна быть предусмотрена
функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""


def employesalary(workhours, hoursalary, reward):
    print(int(workhours) * int(hoursalary) + int(reward))


from sys import argv
print(argv)
try:
    scriptname, workhours, hoursalary, reward = argv
    employesalary(workhours, hoursalary, reward)
except ValueError:
    print("Необходимо ввести все параметры")
