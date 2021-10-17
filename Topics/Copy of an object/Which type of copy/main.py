import copy


def detect_copy():
    obj = [[1, 2], [3, 4]]
    copy_obj = copying_machine(obj)
    is_deep = False
    for item_1, item_2 in zip(obj, copy_obj):
        if id(item_1) != id(item_2):
            is_deep = True
    return "deep copy" if is_deep else "shallow copy"
