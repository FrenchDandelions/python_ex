import math


def NULL_not_found(object: any) -> int:
    o_type = type(object).__name__
    if o_type == 'NoneType' and object is None:
        print(f"Nothing : {object} ", end='')
    elif o_type == 'float' and math.isnan(object):
        print(f"Cheese : {object} ", end='')
    elif o_type == 'int' and object == 0:
        print(f"Zero : {object} ", end='')
    elif o_type == 'str' and object == '':
        print(f"Empty : {object} ", end='')
    elif o_type == 'bool' and object is False:
        print(f"Fake : {object} ", end='')
    else:
        print("Type not Found")
        return 1
    print(type(object))
    return 0
