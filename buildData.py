from typing import List

from hero import Hero
from ability import Ability, Skills, Specials, Intensive
from job import Job


def base_action_point_cost(element):
    switcher = {
        "Energy": [0, 1, 1, 2],
        "Control": [1, 0, 2, 1],
        "Flow": [1, 2, 0, 1],
        "Rest": [2, 1, 1, 0],
    }
    return switcher.get(element, [0, 0, 0, 0])


def build_data_basic_actions(hero):
    bapc = base_action_point_cost(hero.element)
    basic_ability_list: List[Ability] = [
        Ability("Attack", "SE", bapc[0], "1DMG", "Basic Attack", [1, 0, 0, 0]),
        Ability("Defend", "SA", bapc[1], "1SHD", "Simple Block", [0, 1, 0, 0]),
        Ability("Move", "Self", bapc[2], "1MOV", "Basic Move", [0, 0, 1, 0]),
        Ability("Flee", "Self", bapc[3], "EXIT", "Basic Escape", [0, 0, 0, 1])]
    return basic_ability_list


def build_skill_point_costs(energy, control, flow, rest):
    skill_point_costs = {
        0: energy,
        1: control,
        2: flow,
        3: rest
    }
    return skill_point_costs


def build_job_swordmaster():
    skills = [Skills("Pummel", "SE", [1, 1, 0, 0], "1DMG", "Basic Attack", "+E"),
              Skills("Strike", "SE", [2, 0, 0, 0], "1DMG", "Basic Attack", "+E"),
              Skills("Critical Strike", "SE", [1, 0, 1, 0], "1DMG", "Basic Attack", "+E"),
              Skills("Double Slash", "SE", [3, 0, 1, 0], "1DMG", "Basic Attack", "+E")]
    specials = [Specials("Provoke", "SE", 1, "1DMG", "Basic Attack", "+E"),
                Specials("Sword Stance", "SE", 2, "1DMG", "Basic Attack", "+E"),
                Specials("Sharpen", "SE", 3, "1DMG", "Basic Attack", "+E"),
                Specials("Two Handed Grip", "SE", 4, "1DMG", "Basic Attack", "+E")]
    intensives = [Intensive("Sword Play", "SE", 2, "1DMG", "Basic Attack", "+E"),
                  Intensive("X-Slash", "SE", 4, "1DMG", "Basic Attack", "+E")]
    job = Job("Sword Master", skills, specials, intensives)
    hero = Hero("Edge", job, 5, "Energy")
    return hero
