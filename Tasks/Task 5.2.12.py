a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a.split()), set(b.split()) # используем множественное присваивание

a_and_b = a_set.symmetric_difference(b_set)

print(a_and_b)

# 1 2 3 4 5 6 7 8
# 2 4 6 8 10 12