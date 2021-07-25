my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

second_list = my_list.copy()
second_list.sort()
print(second_list)

third_list = my_list.copy()
third_list.sort(reverse = True)
print(third_list)


my_even_list = second_list[1::2]
print(my_even_list)

my_odd_list = second_list[0::2]
print(my_odd_list)

multiple_of_three_list = second_list[2::3]
print(multiple_of_three_list)





