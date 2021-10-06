def translate(**kwargs):
    for english, spanish in kwargs.items():
        print(english, ":", spanish)


words = {"mother": "madre",
         "father": "padre",
         "grandmother": "abuela",
         "grandfather": "abuelo"}

translate(**words)
