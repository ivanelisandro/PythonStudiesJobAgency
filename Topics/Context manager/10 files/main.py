for i in range(1, 11):
    with open(f'file{i}.txt', mode='w') as file:
        file.write(str(i))
