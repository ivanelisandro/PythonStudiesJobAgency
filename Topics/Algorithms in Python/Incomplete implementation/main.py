def startswith_capital_counter(names):
    count = 0
    for name in names:
        if 'A' <= name[0] <= 'Z':
            count += 1
    return count
