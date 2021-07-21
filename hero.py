import buildData


class Hero:
    def __init__(self, name, job, health, element):
        self.name = name
        self.job = job
        self.skill_points = buildData.build_skill_point_costs(0, 0, 0, 0)
        self.health = health
        self.element = element
        self.special_action_points = 0
        self.intensive_force_points = 0
        self.base_action_points = 2
        self.basic_actions = buildData.build_data_basic_actions(self)
