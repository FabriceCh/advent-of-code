from utils import read_file
from enum import Enum
import copy

lines = read_file("/home/fabrice/advent-of-code/2022/input")

lines = [
    "1 4 2 3 14 2 7",
    "2 2 3 3 8 3 12",
]

ar = [[int(a) for a in line.split(" ") if a != ""] for line in lines]


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
        self.MAX_TIME = 24

    def __str__(self):
        string = f"""Config Id: {self.id}
    ore_robot_cost: {self.ore_robot_cost}
    clay_robot_cost: {self.clay_robot_cost}

    obs_robot_cost: {self.obs_robot_cost}
    geode_robot_cost: {self.geode_robot_cost}"""
        return string

class GameData:
    def __init__(self):
        self.current_time = 1
        # resources
        self.ore = 0
        self.clay = 0
        self.obs = 0
        self.geode = 0
        # robots
        self.ore_robots = 1
        self.clay_robots = 0
        self.obs_robots = 0
        self.geode_robots = 0

    def __str__(self):
        string = f"""current_time: {self.current_time}
        ore: {self.ore}
        clay: {self.clay}
        obs: {self.obs}
        geode: {self.geode}
        ore_robots: {self.ore_robots}
        clay_robots: {self.clay_robots}
        obs_robots: {self.obs_robots}
        geode_robots: {self.geode_robots}"""
        return string


class Game:

    max_found = 0

    def __init__(self, game_data: GameData = None, config: Config = None, choice: Choice = "begin", depth = 0, bo = []):
        self.game_data : GameData = game_data
        if self.game_data is None:
            self.game_data = GameData()
        self.config: Config = config
        self.choice: Choice = choice
        self.depth = depth
        self.building = False
        self.choice_generator = self._generate_choices
        self.bo = bo

    def sanity_check(self):
        problem = self.game_data.ore < 0
        problem = problem or self.game_data.clay < 0
        problem = problem or self.game_data.obs < 0
        #problem = problem or self.game_data.ore_robots + self.game_data.clay_robots + self.game_data.obs_robots + self.game_data.geode_robots > self.game_data.current_time
        problem = problem or self.game_data.current_time > self.config.MAX_TIME
        if problem:
            print("problem")

    def _get_resources_from_choice(self):
        if self.choice == Choice.BUILD_ORE_ROBOT:
            return self.config.ore_robot_cost
        elif self.choice == Choice.BUILD_CLAY_ROBOT:
            return self.config.clay_robot_cost
        elif self.choice == Choice.BUILD_OBS_ROBOT:
            return self.config.obs_robot_cost
        elif self.choice == Choice.BUILD_GEODE_ROBOT:
            return self.config.geode_robot_cost

    def _can_be_built(self):
        required = self._get_resources_from_choice()
        for k, v in required.items():
            if k == "ore":
                if v > self.game_data.ore:
                    return False
            elif k == "clay":
                if v > self.game_data.clay:
                    return False
            elif k == "obs":
                if v > self.game_data.obs:
                    return False
        return True

    def _start_build(self):
        if not self._can_be_built():
            print("problem")
        required = self._get_resources_from_choice()
        for k, v in required.items():
            if k == "ore":
                self.game_data.ore -= v
            elif k == "clay":
                self.game_data.clay -= v
            elif k == "obs":
                self.game_data.obs -= v
        self.building = True

    def _mine(self, n_turns):
        self.game_data.ore += self.game_data.ore_robots * n_turns
        self.game_data.clay += self.game_data.clay_robots * n_turns
        self.game_data.obs += self.game_data.obs_robots * n_turns
        self.game_data.geode += self.game_data.geode_robots * n_turns

    def _end_build(self):
        if self.choice == Choice.BUILD_ORE_ROBOT:
            self.game_data.ore_robots += 1
        elif self.choice == Choice.BUILD_CLAY_ROBOT:
            self.game_data.clay_robots += 1
        elif self.choice == Choice.BUILD_OBS_ROBOT:
            self.game_data.obs_robots += 1
        elif self.choice == Choice.BUILD_GEODE_ROBOT:
            self.game_data.geode_robots += 1
        self.bo.append((self.game_data.current_time, self.choice))

    def _get_remaining_time(self):
        return (self.config.MAX_TIME - self.game_data.current_time) + 1

    def _get_potential(self):
        remaining_time = self._get_remaining_time()
        return sum([i for i in range(remaining_time)]) + self.game_data.geode

    def _generate_choices(self):
        choices = []
        if self._get_potential() < Game.max_found:
            return choices

        max_ore_cost = max([
            self.config.ore_robot_cost["ore"],
            self.config.clay_robot_cost["ore"],
            self.config.obs_robot_cost["ore"],
            self.config.geode_robot_cost["ore"],
            ])
        if self.game_data.ore_robots < max_ore_cost:
            choices.append(Choice.BUILD_ORE_ROBOT)
        if self.game_data.clay_robots < self.config.obs_robot_cost["clay"]:
            choices.append(Choice.BUILD_CLAY_ROBOT)
        if self.game_data.clay_robots >= 1 and self.game_data.obs_robots < self.config.geode_robot_cost["obs"]:
            choices.append(Choice.BUILD_OBS_ROBOT)
        if self.game_data.obs_robots >= 1:
            choices.append(Choice.BUILD_GEODE_ROBOT)
        return choices

    def _get_scores_on_split(self):
        new_choices = self.choice_generator()
        if len(new_choices) == 0:
            return 0
        for c in new_choices:
            g = Game(game_data=copy.deepcopy(self.game_data), config=self.config, choice=c, depth=self.depth + 1, bo = copy.deepcopy(self.bo))
            g.execute_turns()

    def _gg_n_turns_crisse(self, cost, current_amt, n_robots):
        missing_amt = cost - current_amt
        if missing_amt % n_robots == 0:
            return missing_amt // n_robots + 1
        else:
            return missing_amt // n_robots + 2

    def _get_n_turns_until_build(self):
        required = self._get_resources_from_choice()
        n_turns = 1
        for k, v in required.items():
            if k == "ore":
                if v > self.game_data.ore:
                    n_turns = max(n_turns, self._gg_n_turns_crisse(v, self.game_data.ore, self.game_data.ore_robots))
            elif k == "clay":
                if v > self.game_data.clay:
                    n_turns = max(n_turns, self._gg_n_turns_crisse(v, self.game_data.clay, self.game_data.clay_robots))
            elif k == "obs":
                if v > self.game_data.obs:
                    n_turns = max(n_turns, self._gg_n_turns_crisse(v, self.game_data.obs, self.game_data.obs_robots))
        return n_turns

    def execute_turns(self):
        self.sanity_check()

        if self.choice == "begin":
            return self._get_scores_on_split()

        n_turns = self._get_n_turns_until_build()

        if self.game_data.current_time + n_turns >= self.config.MAX_TIME + 1:
            current_score = self.game_data.geode + self.game_data.geode_robots * (self._get_remaining_time())
            if current_score > Game.max_found:
                Game.max_found = current_score
                print("SCORE:", current_score)
                print(self.bo)
                #print(self.game_data)
            return
        self.game_data.current_time += n_turns
        self._mine(n_turns)
        self._start_build()
        self._end_build()
        self._get_scores_on_split()
            
def part2():
    answer = 1
    print(ar[:3])
    for l in ar[:3]:
        geodes = 0
        config = Config(l)
        game = Game(config=config)
        Game.max_found = 0
        game.execute_turns()
        geodes = Game.max_found
        answer *= geodes
        print("geodes: ", geodes)
    print(answer)

#def part1():
#    # change config to 24
#    answer = 0
#    for l in ar:
#        config = Config(l)
#        gd = GameData(config)
#        game = Game(gd)
#        game.max_found = 0
#        game.execute_turns()
#        geodes = Game.max_found
#        print(Game.best_build_order)
#        answer += geodes * game.config.id
#        print("geodes: ", geodes)
#    print(answer)

part2()
