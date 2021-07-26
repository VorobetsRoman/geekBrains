#p1
print("printing someting")
fName = "Sasha"
lName = "Gray"
age = 18
print("Hello, %s %s, you are %d allready" % (fName,lName, age))
# user = input("and what is your name? :")

#p2
"""
Пользователь вводит время в секундах. 
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк
"""
time = int(input("Время в секундах:"))
timeHours = time // 3600
timeMinutes = (time - timeHours * 3600) // 60
timeSeconds = time - timeHours * 3600 - timeMinutes * 60
print("Введённое число делится на %s часов %s минут %s секунд" % (timeHours, timeMinutes, timeSeconds))
#3
"""
Узнайте у пользователя число n. 
Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369
"""
var = str(input("Число: "))
ivar = int(var)
ivarvar = int("%s%s"%(var, var))
ivarvarvar = int("%s%s%s"%(var, var, var))
print(ivar, ivarvar, ivarvarvar, ivarvarvar + ivarvar + ivar)
#4
"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""
var = str(input("Целое положительное число: "))
length = len(var)
index = 0
letter = 0
while index < length:
    nextLetter = int(var[index])
    if letter < nextLetter:
        letter = nextLetter
    index = index + 1
print(letter)
#5
"""
Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма. 
Например, прибыль — выручка больше издержек, 
или убыток — издержки больше выручки. 
Выведите соответствующее сообщение.

Если фирма отработала с прибылью, 
вычислите рентабельность выручки. 
Это отношение прибыли к выручке. 
Далее запросите численность сотрудников фирмы 
и определите прибыль фирмы в расчёте на одного сотрудника.
"""
costs = int(input("Введите размер издержек :"))
revenue: int = int(input("Введите размер выручки :"))
if (revenue > costs) :
    print("Фирма работает с прибылью")
    print("Рентабельность работы :%f" % (float(revenue) / float(costs)))
    employes = int(input("Количество работников :"))
    print("В среднем один работник приносит %f прибыли" % float((revenue - costs) / employes))
else :
    print("Фирма работает с убытком")
#6
"""
Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. 
Требуется определить номер дня, 
на который результат спортсмена составит не менее b километров. 
Программа должна принимать значения параметров a и b 
и выводить одно натуральное число — номер дня.
"""
start = float(input("Километраж первого дня: "))
finish = float(input("Километраж требуемый: "))
daysCount: int = 0
while (finish > start) :
    start = start * 1.1
    daysCount = daysCount + 1
print("Нужный результат будет достигнут через %d дней" % (daysCount))
