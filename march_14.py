"""MARCH 14, 2021"""

# def smth(a, b:str, c):
#     """
#     Description
#     :param a: a really cool 1st element
#     :param b: table name
#     :param c: year of mankind creation
#     :return: None
#     """
#
# smth()

def sum_nums(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

num1 = int(input('ВВедите первое число: '))
num2 = int(input('Введите второе число: '))
operator = input('Введите операцию: ')

if operator == "+":
    print(sum_nums(num1, num2))
elif operator == "-":
    print(sum_nums(num1, num2))
