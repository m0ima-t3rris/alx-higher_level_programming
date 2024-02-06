#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_lst = []
    for item in range(list_length):
        try:
            divide = my_list_1[item] / my_list_2[item]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            new_lst.append(div)
    return new_lst
