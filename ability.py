class Ability:
    def __init__(self, name, target, cost, effect, description, reward):
        self.name = name
        self.target = target
        self.cost = cost
        self.effect = effect
        self.description = description
        self.reward = reward
        self.usability = False

    def is_able(self, hero):
        usable = [self.cost <= hero.base_action_points]
        return usable

    def process_usability(self, usable):
        if not usable[0]:
            return False
        return True

    def update_usability(self, hero):
        self.usability = self.process_usability(self.is_able(hero))

    def process_cost(self, hero):
        hero.base_action_points -= self.cost

    def process_rewards(self, hero):
        for i in range(len(hero.basic_actions)):
            hero.skill_points[i] += self.reward[i]


class Skills(Ability):

    def __init__(self, name, target, cost, effect, description, reward):
        super().__init__(name, target, cost, effect, description, reward)

    def process_usability(self, usable):
        count = 0
        for i in range(len(usable)):
            if not usable[i]:
                continue
            else:
                count += 1
                continue
        return True if count == len(usable) else False

    def is_able(self, hero):
        usable = {}
        for i in range(0, 4):
            usable[i] = self.cost[i] <= hero.skill_points[i]
        return usable

    def process_cost(self, hero):
        for i in range(0, 4):
            hero.skill_points[i] -= self.cost[i]


class Specials(Ability):
    def __init__(self, name, target, cost, effect, description, reward):
        super().__init__(name, target, cost, effect, description, reward)

    def is_able(self, hero):
        usable = [self.cost <= hero.special_action_points]
        return usable

    def process_cost(self, hero):
        hero.special_action_points -= self.cost


class Intensive(Ability):
    def __init__(self, name, target, cost, effect, description, reward):
        super().__init__(name, target, cost, effect, description, reward)

    def is_able(self, hero):
        usable = [self.cost <= hero.intensive_force_points]
        return usable

    def process_cost(self, hero):
        hero.intensive_force_points -= self.cost
