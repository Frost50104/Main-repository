def otstup():
    print()
    print("---")
    print()

otstup()

def print_2_add_2():
    result = 2+2
    print(result)

print_2_add_2()

otstup()

def hello_world():
    print("Hello World")

hello_world()

otstup()

def delitel(a, n):
    if a % n == 0:
        print("True")
    else:
        print("False")

delitel(10, 5)

otstup()
def lesenka(n):
    for i in range(n, 0, -1):
        print("*" * i)

lesenka(3)

otstup()

def count_delitel(a):
    count = 0
    for i in range(1, a+1):
        if a % i == 0:
            count += 1
    print(count)

count_delitel(5)

otstup()

def polindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False
print(polindrome("Кит на море не романтик"))


