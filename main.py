# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import battle_state
import buildData


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def translate_action_list(actor, first_choice):
    action_list = 0
    if first_choice == 1:
        action_list = actor.basic_actions
    if first_choice == 2:
        action_list = actor.job.skills
    if first_choice == 3:
        action_list = actor.job.specials
    if first_choice == 4:
        action_list = actor.job.intensives

    return action_list


def check_valid(action, validity_choice):
    return action[validity_choice - 1].usability


def get_action(actor, first_choice, second_choice):
    return translate_action_list(actor, first_choice)[second_choice - 1]


def list_actions(actor, action_type):
    spacer = "\n   "
    switcher = {
        1: "Basic Actions",
        2: "Skills",
        3: "Special Actions",
        4: "Intensive Force"
    }
    action_list = translate_action_list(actor, action_type)

    txt = switcher.get(action_type, "Invalid Choice")

    for i in range(0, len(action_list)):
        usable_txt = '-!- '
        action_list[i].update_usability(actor)
        if action_list[i].usability:
            usable_txt = "-+- "
        num_txt = str(i + 1) + ". "
        txt = txt + spacer + usable_txt + num_txt + action_list[i].name
    return txt + "\n"


def new_round(group):
    for j in range(len(group.team)):
        group.team[j].steps = 0
        group.team[j].hero.base_action_points = 2
    group.turns += 1


def next_act(group):
    # load next actor
    main_group.acts += 1
    print("Steps are up next actor is up.")
    if group.acts_complete():
        new_round(group)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello welcome to the battle tester\n")
    print("Battle Start\n")
    i = 0
    main_hero = buildData.build_job_swordmaster()
    member_one = battle_state.team_member(main_hero)
    main_group = battle_state.group([member_one])
    while True:
        choice = int(input("Choose an action:" +
                           "\n   1. Basic \n   2. Skill\n   3. Special \n   4. Intensive Force\n"))
        choice2 = int(input(list_actions(main_hero, choice)))
        if check_valid(translate_action_list(main_hero, choice), choice2):
            print("Executed")
            main_group.team[i].steps += 1
            action = get_action(main_hero, choice, choice2)
            action.process_cost(main_hero)
            action.process_rewards(main_hero)
            if main_group.team[i].steps == 3:
                next_act(main_group)
        else:
            print("Failure")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
