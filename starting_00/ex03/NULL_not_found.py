def NULL_not_found(object: any) -> int:
    object_type = type(object).__name__
    if object_type == 'NoneType':
        print(f"Nothing : {object} ", end='')
    elif object_type == 'tuple':
        print(f"Cheese : {object} ", end='')
    elif object_type == 'set':
        print(f"Zero : {object} ", end='')
    elif object_type == 'dict':
        print(f"Empty : {object} ", end='')
    elif object_type == 'str':
        print(f"False : {object} ", end='')
    else:
        print("Type not found")
        return 1
    print(type(object))
    return 0