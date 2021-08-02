
## problema 3

# user_input = input('type an integer: ')
#
# try:
#     user_input = int(user_input)
#     print(user_input)
#
# except ValueError as e:
#     print(0)



## problema 1

# def my_function(*x, **y):
#     return sum(filter(lambda n: isinstance(n, (int, float)), x))
#
# print(my_function(5, 'sdfg', 2.65, -45, sd=545))


## problema 2

### functia care face suma tuturor numerelor de la [0, n]:

# def my_sum(n):
#
#     x = 0
#     if n == 0:
#         return x
#
#     return n + my_sum(n-1)
#
# print(my_sum(0))


### functia care face suma tuturor numerelor pare si impare de la [0, n]


### -nu am reusit sa combin cele trei functii:
### -functia ce face suma numerelor pare/impare e impropriu spus pentru ca depinde de variabila n (para sau impara)
### si nu stie sa faca suma numerelor pare daca n e impar, si viceversa.


def my_sum_even(n):

    if n <= 0:
        return 0

    return n + my_sum_even(n-2)


print(my_sum_even(4))



