
# 5.3.11
# на вход принимает последовательность целых чисел, и возвращает True,
# если все числа ненулевые, и False, если хотя бы одно число равно 0.

L = list(map(int, input().split()))

print(all(L))

#5.3.12

L = list(map(int, input().split()))

print(not any(L))
