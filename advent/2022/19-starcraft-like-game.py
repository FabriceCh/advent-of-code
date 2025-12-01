from functools import cache
from enum import Enum
from typing import List, Tuple
import copy

lines = []

file = open("/home/fab/AOC/2022/input", "r")
for l in file.readlines():
    lines.append(l.rstrip())

class Choice(Enum):
    BUILD_ORE_ROBOT = 1
    BUILD_CLAY_ROBOT = 2
    BUILD_OBS_ROBOT = 3
    BUILD_GEODE_ROBOT = 4

class Config:
    def __init__(self, config_line):
        self.id = config_line[0]
        self.ore_robot_cost = {"ore": config_line[1]}
        self.clay_robot_cost = {"ore": config_line[2]}
        self.obs_robot_cost = {"ore": config_line[3], "clay": config_line[4]}
        self.geode_robot_cost = {"ore": config_line[5], "obs": config_line[6]}
        self.MAX_TIME = 32
        self.MAX_FOUND = 0


class GameData:
    def __init__(self, arr_repr=None):
        if arr_repr is None:
            self.current_time = 1
            self.ore = 0
            self.clay = 0
            self.obs = 0
            self.geode = 0
            self.ore_robots = 1
            self.clay_robots = 0
            self.obs_robots = 0
            self.geode_robots = 0
        else:
            self.current_time = arr_repr[0]
            self.ore = arr_repr[1]
            self.clay = arr_repr[2]
            self.obs = arr_repr[3]
            self.geode = arr_repr[4]
            self.ore_robots = arr_repr[5]
            self.clay_robots = arr_repr[6]
            self.obs_robots = arr_repr[7]
            self.geode_robots = arr_repr[8]
            
    def get_arr_repr(self):
        return (
            self.current_time,
            self.ore,
            self.clay,
            self.obs,
            self.geode,
            self.ore_robots,
            self.clay_robots,
            self.obs_robots,
            self.geode_robots,
        )

def lines_to_game_configs(lines):
    configs = []
    for line in lines:
        config_line = []
        words = line.split(" ")
        config_line.append(int(words[1].split(":")[0]))
        config_line.append(int(words[6]))
        config_line.append(int(words[12]))
        config_line.append(int(words[18]))
        config_line.append(int(words[21]))
        config_line.append(int(words[27]))
        config_line.append(int(words[30]))
        configs.append(Config(config_line=config_line))
    return configs

def get_resources_from_choice(choice, config):
        if choice == Choice.BUILD_ORE_ROBOT:
            return config.ore_robot_cost
        elif choice == Choice.BUILD_CLAY_ROBOT:
            return  config.clay_robot_cost
        elif choice == Choice.BUILD_OBS_ROBOT:
            return config.obs_robot_cost
        elif choice == Choice.BUILD_GEODE_ROBOT:
            return config.geode_robot_cost

def can_be_built(choice, config, game_data):
        required = get_resources_from_choice(choice, config)
        for k, v in required.items():
            if k == "ore":
                if v > game_data.ore:
                    return False
            elif k == "clay":
                if v > game_data.clay:
                    return False
            elif k == "obs":
                if v > game_data.obs:
                    return False
        return True

def mine(game_data):
    game_data.ore += game_data.ore_robots
    game_data.clay += game_data.clay_robots
    game_data.obs += game_data.obs_robots
    game_data.geode += game_data.geode_robots

def build(game_data, choice, config):
    res = get_resources_from_choice(choice, config)
    if choice == Choice.BUILD_ORE_ROBOT:
        game_data.ore_robots += 1
    elif choice == Choice.BUILD_CLAY_ROBOT:
        game_data.clay_robots += 1
    elif choice == Choice.BUILD_OBS_ROBOT:
        game_data.obs_robots += 1
    elif choice == Choice.BUILD_GEODE_ROBOT:
        game_data.geode_robots += 1
    for k, v in res.items():
            if k == "ore":
                game_data.ore -= v
            elif k == "clay":
                game_data.clay -= v
            elif k == "obs":
                game_data.obs -= v

def generate_choices(game_data, config):
    choices = []

    max_ore_cost = max([
        config.ore_robot_cost["ore"],
        config.clay_robot_cost["ore"],
        config.obs_robot_cost["ore"],
        config.geode_robot_cost["ore"],
        ])

    if game_data.ore_robots < max_ore_cost:
        choices.append(Choice.BUILD_ORE_ROBOT)
    if game_data.clay_robots < config.obs_robot_cost["clay"]:
        choices.append(Choice.BUILD_CLAY_ROBOT)
    if game_data.clay_robots >= 1 and game_data.obs_robots < config.geode_robot_cost["obs"]:
        choices.append(Choice.BUILD_OBS_ROBOT)
    if game_data.obs_robots >= 1:
        choices.append(Choice.BUILD_GEODE_ROBOT)

    return choices


def get_remaining_time(config, game_data):
    return (config.MAX_TIME - game_data.current_time) + 1

def get_potential(config, game_data):
    remaining_time = get_remaining_time(config, game_data)
    potential = sum([i + game_data.geode_robots for i in range(remaining_time)]) + game_data.geode
    return potential > config.MAX_FOUND

@cache
def get_max_geodes(gd: Tuple, conf: Config, choice: Choice = None):
    data = GameData(arr_repr=gd)

    if not get_potential(conf, data):
        return 0

    if choice is None:
        return gen_choices_max([Choice.BUILD_CLAY_ROBOT, Choice.BUILD_ORE_ROBOT], data, conf)

    if data.current_time == conf.MAX_TIME + 1:
        return data.geode
    building = can_be_built(choice, conf, data)
    mine(data)
    data.current_time += 1
    if building:
        build(data, choice, conf)
        choices = generate_choices(data, conf)
        return gen_choices_max(choices, data, conf)
    else:
        return get_max_geodes(data.get_arr_repr(), conf, choice)



def gen_choices_max(choices: List, gd, conf):
    scores = []
    for c in choices:
        scores.append(get_max_geodes(copy.deepcopy(gd.get_arr_repr()), conf, c))
    conf.MAX_FOUND = max(conf.MAX_FOUND, max(scores))
    return max(scores)


def part1():
    answer = 0
    configs = lines_to_game_configs(lines)
    for c in configs:
        gd = GameData()
        geodes = get_max_geodes(gd.get_arr_repr(), c)
        print("found", geodes, "geodes for id", c.id)
        answer += geodes * c.id
    print(answer)
#part1()


def part2():
    answer = 1
    configs = lines_to_game_configs(lines)
    for c in configs[:3]:
        gd = GameData()
        geodes = get_max_geodes(gd.get_arr_repr(), c)
        print("found", geodes, "geodes for id", c.id)
        answer *= geodes
    print(answer)
part2()

