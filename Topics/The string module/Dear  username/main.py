import string

parts = ["Dear $username!",
         "It was really nice to meet you.",
         "Hopefully, you have a nice day!",
         "See you soon, $username!"]

template = string.Template(' '.join(parts))

name = input()
print(template.substitute(username=name))
