def unpack(input_tuple):
    unpacked = ()
    for item in input_tuple:
        if isinstance(item, tuple):
            unpacked += item
        else:
            unpacked += (item,)
    return unpacked
