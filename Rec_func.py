def rec_fibb(n):
   if n == 1:
       return 1
   if n == 2:
      return 1
   return rec_fibb(n - 1) + rec_fibb(n - 2)

print(rec_fibb(10))


# С помощью рекурсивной функции найдите сумму чисел от 1 до n.

def rec_sum(n):
    if n == 1:
        return 1
    return n + rec_sum(n-1)

print(rec_sum(10))

# С помощью рекурсивной функции развернуть строку.

def rec_str(n):
    if len(n) == 0:
        return ""
    return n[-1] + rec_str(n[:-1])

print(rec_str("test"))

# Дано натуральное число N. Вычислите сумму его цифр

def n_sum(n):
    if n < 10:
        return n
    return n % 10 + n_sum(n//10)

print(n_sum(123))

def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a+b
        yield b

