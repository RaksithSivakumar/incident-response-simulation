import json
import os

SCENARIO_PATH = "scenarios/"

def load_scenario(scenario_id):
    try:
        with open(os.path.join(SCENARIO_PATH, f"scenario{scenario_id}.json"), 'r') as file:
            scenario = json.load(file)
        return scenario
    except FileNotFoundError:
        return None

def check_actions(user_actions, correct_actions):
    correct = [action for action in user_actions if action in correct_actions]
    incorrect = [action for action in user_actions if action not in correct_actions]
    return correct, incorrect
