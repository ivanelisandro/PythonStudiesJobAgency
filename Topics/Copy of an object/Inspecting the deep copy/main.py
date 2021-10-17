import copy


def solve(obj):
    new_object = copy.deepcopy(obj)
    return id(obj) != id(new_object)
