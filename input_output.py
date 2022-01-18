# Приветствие:
def print_name():
    print("Введите имя")
    name = input()
    print("Привет,", name)
# Куб - площадь и объём:
def cube():
    a = int(input())
    v = a ** 3  # a * a * a
    s = 6 ** 2  # 6 * a * a
    print("Объем =", v)
    print("Площадь полной поверхности =", s)
# Арифметическая прогрессия:
def arithmetic_progression():
    a1 = int(input())
    d = int(input())  # разность прогрессии
    n = int(input())
    an = a1 + d * (n - 1)
    print(an)
# Геометрическая прогрессия:
def geometric_progression():
    b1 = int(input())
    q = int(input())  # знаменатель прогрессии
    n = int(input())
    bn = b1 * q ** (n - 1)
    print(bn)
# Расстояние в метрах:
def cm_to_m():
    cm = int(input())
    m = cm // 100
    print(m)
# Мандарины:
'''
n школьников делят k мандаринов поровну, 
неделящийся остаток остается в корзине. 
Сколько целых мандаринов достанется каждому школьнику? 
Сколько целых мандаринов останется в корзине?
'''
def tangerines():
    n = int(input())
    k = int(input())
    st = k // n
    basket = k % n
    print(st)
    print(basket)
# Tanos and половина населения*:
'''
Безумный титан Танос собрал все 6 камней бесконечности 
и намеревается уничтожить половину населения Вселенной по щелчку пальцев. 
При этом если население Вселенной является нечетным числом, 
то титан проявит милосердие и округлит количество выживших в большую сторону. 
Помогите Мстителям подсчитать количество выживших.
'''
def tanos():
    n = int(input())
    surv = n - n // 2
    print(surv)
# Номер купе*:
'''
В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. 
Напишите программу, которая определяет номер купе, в котором находится место с заданным номером 
(нумерация мест сквозная, начинается с 1).
'''
def train():
    n = int(input())
    print((n + 3) // 4)  # или -(-n // 4)
# Перевод минут в часы и минуты
def min_to_hm():
    minutes = int(input())
    hours = minutes // 60
    remain_minutes = minutes % 60
    print(minutes, "мин - это", hours, "час", remain_minutes, "минут.")
# Четырёхзначное число:
def four_digits():
    num = int(input())
    first = num // 10 ** 3
    second = (num // 10 ** 2) % 10
    third = (num // 10) % 10
    fourth = num % 10
    d_in_pos = "Цифра в позиции"
    eq = "равна"
    print(d_in_pos, "тысяч", eq, first)
    print(d_in_pos, "сотен", eq, second)
    print(d_in_pos, "десятков", eq, third)
    print(d_in_pos, "единиц", eq, fourth)
# Перестановка цифр (трёхзначного числа)
def rearrange_digits():
    abc = int(input())
    a = abc // 100
    b = (abc // 10) % 10
    c = abc % 10
    acb = a * 100 + c * 10 + b
    bac = b * 100 + a * 10 + c
    bca = b * 100 + c * 10 + a
    cab = c * 100 + a * 10 + b
    cba = c * 100 + b * 10 + a
    print(abc, acb, bac, bca, cab, cba, sep="\n")
