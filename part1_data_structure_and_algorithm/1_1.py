# 将序列分解为单独的变量
p = (4, 5)
x, y = p
print("x = ", x)
print("y = ", y)

s = "Hello"
a, b, c, d, e = s
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)
print("e = ", e)


data = ["A", 50, 89.1, (2020, 11, 23)]
name, age, grand, date = data
print("name = ", name)
print("age =", age)
print("grand = ", grand)
print("date = ", date)

name_1, age_1, grand_1, (year, mon, day) = data
print("name_1 = ", name_1)
print("age_1 ", age_1)
print("grand_1 = ", grand_1)
print("year, mon, day = ", year, mon, day)

_, age_2, grand_2, _ = data
print("_ = ", _)
print("age_2 ", age_2)
print("grand_2 = ", grand_2)
print("_ = ", _)
