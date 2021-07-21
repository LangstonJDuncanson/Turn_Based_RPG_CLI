class BattleState:
    def __init__(self):
        self.rounds = 0


class group:
    def __init__(self, team):
        self.team = team
        self.size = len(team)
        self.turns = 0
        self.acts = 0

    def acts_complete(self):
        return self.acts == self.size


class team_member:
    def __init__(self, hero):
        self.hero = hero
        self.steps = 0
