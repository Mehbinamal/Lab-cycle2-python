def string_conversion(a):
    b = ''.join(a)
    c = b.split()
    d = []
    for i in c:
        d.append(int(i))
    print(f"List of integers =\n{d}")
    return d


def list_position(c, k):
    k = k % len(c)
    new_list = c[-k:]+c[:-k]
    print(f"New list after Rotation of {k} Position =\n{new_list}")
    return new_list


def tuple_(a):
    b = tuple(a)
    print(f"Converted Tuple : {b}")


def duplicates(d):
    new_tuple = tuple(set(d))
    new_list = list(new_tuple)
    print(f"Converted list(after deleting duplicates) =\n{new_list}")
    return new_list


def function(e):
    function_list = []
    for x in e:
        k = ((x**2)-x)
        function_list.append(k)
    print(f"Results of function = \n{function_list}")
    return function_list


def sorting(a, b):
    a.sort()
    print(f"Sorted list of numbers : {a}")
    b.sort()
    print(f"Sorted list of function images : {b}")
    a.extend(b)
    a.sort()
    print(f"sorted list after combining : {a}")


string = input("Enter a String of Numbers with spaces :")
list_int = string_conversion(string)

rotation = int(input("How many position needs to be Rotated :"))
rotated_list = list_position(list_int, rotation)

tuple_(list_int)

p = duplicates(list_int)

q = function(p)
sorting(p, q)
