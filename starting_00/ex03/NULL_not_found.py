import math


def NULL_not_found(object: any) -> int:
    object_type = type(object).__name__
    if object_type == 'NoneType' and object is None:
        print(f"Nothing : {object} ", end='')
    elif object_type == 'float' and math.isnan(object):
        print(f"Cheese : {object} ", end='')
    elif object_type == 'int' and object == 0:
        print(f"Zero : {object} ", end='')
    elif object_type == 'str' and object == '':
        print(f"Empty : {object} ", end='')
    elif object_type == 'bool' and object is False:
        print(f"False : {object} ", end='')
    else:
        print("Type not found")
        return 1
    print(type(object))
    return 0
