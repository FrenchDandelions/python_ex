def all_thing_is_obj(object: any) -> int:
    object_type = type(object).__name__
    if object_type == 'list':
        print("List : ", end='')
    elif object_type == 'tuple':
        print("Tuple : ", end='')
    elif object_type == 'set':
        print("Set : ", end='')
    elif object_type == 'dict':
        print("Dict : ", end='')
    elif object_type == 'str':
        print(f"{object} is in the kitchen : ", end='')
    else:
        print("Type not found")
        return 42
    print(type(object))
    return 42
