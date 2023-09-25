#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """A function that divides element by element 2 lists.

    Args:
        my_list_1 (list): The first element list.
        my_list_2 (list): The second element list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list (length = list_length) with all divisions
    """
    new_list = []
    for num in range(0, list_length):
        try:
            div = my_list_1[num] / my_list_2[num]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
