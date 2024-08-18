my_list = ["Python", 1, 2, 3, 9, 9, True]
my_list_element = my_list[0]
my_list.append("test")
my_list.remove("Python")
my_list_counter = my_list.count(9)
my_tuple = (1, 8, 11, "Python", False)
my_tuple_element = my_tuple[1]
print(f"Wybrany elementy listy: {my_list_element}, wszystkie elementy listy: {my_list} / {my_list_counter} / {my_tuple_element}")