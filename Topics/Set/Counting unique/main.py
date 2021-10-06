# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

subjects = set(Belov)
subjects.update(Smith)
subjects.update(Sarada)
print(len(subjects))
