import random
# todo задание 1
first_name = "oleg"
last_name = 'makarenkov'
# todo задание 2
a = 3
b = 5
c = 17
d = 32
# todo задание 3
i = 4.5
f = 24.8
g = 47.7
# todo задание 4
comp_1 = a < b
comp_2 = d < c
comp_3 = b < d
comp_4 = d > c
comp_5 = b > d
comp_6 = a > b
comp_7 = a <= d
comp_8 = b <= c
comp_9 = a <= c
comp_10 = b >= a
comp_11 = d >= c
comp_12 = a >= c
comp_13 = a != a
comp_14 = b != c
comp_15 = c != d
print('comp_1 =', comp_1)
print('comp_2 =', comp_2)
print('comp_3 =', comp_3)
print('comp_4 =', comp_4)
print('comp_5 =', comp_5)
print('comp_6 =', comp_6)
print('comp_7 =', comp_7)
print('comp_8 =', comp_8)
print('comp_9 =', comp_9)
print('comp_10 =', comp_10)
print('comp_11 =', comp_11)
print('comp_12 =', comp_12)
print('comp_13 =', comp_13)
print('comp_14 =', comp_14)
print('comp_15 =', comp_15)
# todo задание 5
comp_16 = f < g
comp_17 = g != g
comp_18 = i > g
comp_19 = f <= g
comp_20 = i <= g
comp_21 = g >= f
comp_22 = i >= g
comp_23 = f != g
comp_24 = i != i
print('comp_16 =', comp_16)
print('comp_17 =', comp_17)
print('comp_18 =', comp_18)
print('comp_19 =', comp_19)
print('comp_20 =', comp_20)
print('comp_21 =', comp_21)
print('comp_22 =', comp_22)
print('comp_23 =', comp_23)
print('comp_24 =', comp_24)
# todo задание 6
comp_25 = a != c and b < d
comp_26 = c > d or a > b
comp_27 = not b != b
comp_28 = c >= b and not a > d
comp_29 = b > c or not d >= c
comp_30 = d != a or c < d
comp_31 = not d >= b and b != a
comp_32 = d <= c or a < c
comp_33 = not b > a
comp_34 = not a != b and c > d or c <= d
print('comp_25 =', comp_25)
print('comp_26 =', comp_26)
print('comp_27 =', comp_27)
print('comp_28 =', comp_28)
print('comp_29 =', comp_29)
print('comp_30 =', comp_30)
print('comp_31 =', comp_31)
print('comp_32 =', comp_32)
print('comp_33 =', comp_33)
print('comp_34 =', comp_34)
# todo задание 7
age = int(input('введите число: '))
if age > 30:
    print('вы ввели число =', age, 'которое больше 30')
elif age < 30:
    print('вы ввели число =', age, 'которое меньше 30')
elif age == 30:
    print('вы ввели число =', age, 'которое равно 30')
# todo задание 8 и 9
rand = random.randint(1, 100)
apr = int(input('введите число: '))
if apr > rand:
    print('вы ввели число =', apr, 'которое больше сгенерированного числа ', rand)
elif apr < rand:
    print('вы ввели число =', apr, 'которое меньше сгенерированного числа ', rand)
else:
    print('вы ввели число =', apr, 'которое равно сгенерированному числу ', rand)