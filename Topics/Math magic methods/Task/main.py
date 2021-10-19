class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, other):
        new_description = f'{self.description}\n{other.description}'
        new_team = f'{self.team}, {other.team}'
        return Task(new_description, new_team)
